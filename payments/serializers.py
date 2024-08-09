from rest_framework import serializers, status
from rest_framework.response import Response

from payments.models import PaymentInfo
from accounts.models import User

import datetime
import ipdb


class PaymentSerializer(serializers.ModelSerializer):

    card_expiring_date = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = PaymentInfo
        fields = "__all__"

        extra_kwargs = {
            "is_active": {'read_only': True},
            "cvv": {'write_only': True},
            "customer": {'read_only': True}
        }

    def validate(self, attrs):
        # Expiring date:

        # Caso a data informada em card_expiring_date já tenha passado, o campo is_active será setado para False.
        # Por questões de simplificação, em card_expiring_date deverá ser informada a data completa.
        # Não será possível o cadastro de cartões de crédito vencidos.
        # Caso haja a tentativa de cadastro de um cartão que esteja vencido, essa deverá ser a resposta:
        # STATUS - 400 - 

        card_expiring_date = attrs["card_expiring_date"]
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        # ipdb.set_trace()
        if now > card_expiring_date.strftime('%Y-%m-%d'):
            raise serializers.ValidationError({ "error": "This card is expired"})

        # Card number:
        card_number_typed = attrs["card_number"]
        if len(card_number_typed) < 16:
            raise SyntaxError({"Error": "Verify card number digits! It needs to be 16."}) 
        # Payment method:

        # Não será possível o cadastro do mesmo cartão para o usuário, exceto, caso o método de pagamento seja
        #  diferente, ou seja, 2 cartões iguais porém um é de crédito e o outro é de débito.
        
        payment_method_typed = attrs["payment_method"]
        do_we_have_already_this_card = PaymentInfo.objects.filter(card_number=card_number_typed)
        is_this_card_already_used_with_this_method = PaymentInfo.objects.filter(payment_method=payment_method_typed)

        if do_we_have_already_this_card and is_this_card_already_used_with_this_method:
            raise ValueError({"error": "This card is already registered for this user"})
            # return Response({"error": "This card is already registered for this user"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            # return Response({"Error": "This card number is already registered!"}, status=status.HTTP_409_CONFLICT)
        # Caso o cartão a ser criado já esteja cadastrado para o usuário, a resposta deverá ser:
        # STATUS 422 - {"error": ["This card is already registered for this user"]}

        final_result = ""
        counter = 0
        for digits in card_number_typed:
            counter = counter + 1
            if counter > 12:
                final_result = final_result + digits

        # Do we have this cardholders_name already registered?:
        cardholders_name = str(attrs["cardholders_name"]).casefold()
        user = self.context.get('request').user
        if user:
            user_full_name = f"{user.first_name} {user.last_name}".casefold()
            if cardholders_name != user_full_name:
                raise serializers.ValidationError({"error": "The cardholders_name must be the same of the user credentials."})

        # List cards:
        # display cards with is-active False if card_expiring_date is gone:

        return super().validate(attrs)

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user:
            validated_data['customer'] = request.user
            # ipdb.set_trace()
        return super().create(validated_data)
