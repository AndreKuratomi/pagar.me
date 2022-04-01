from rest_framework import serializers

from payments.models import PaymentInfo

import ipdb


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = "__all__"

        extra_kwargs = {
            "is_active": {'read_only': True},
            "cvv": {'write_only': True},
            "customer": {'read_only': True}
        }

    def validate(self, attrs):
        card_expiring_date = attrs["card_expiring_date"]
# Caso a data informada em card_expiring_date já tenha passado, o campo is_active será setado para False.
# Por questões de simplificação, em card_expiring_date deverá ser informada a data completa.
# Não será possível o cadastro de cartões de crédito vencidos.
# Caso haja a tentativa de cadastro de um cartão que esteja vencido, essa deverá ser a resposta:
# STATUS - 400 - { "error": ["This card is expired"]}
        card_number = attrs["card_number"]
        final_result = ""
        counter = 0
        for digits in card_number:
            counter = counter + 1
            if counter > 12:
                final_result = final_result + digits


# Somente serão retornados para o usuário os últimos 4 dígitos do cartão de crédito.
# Caso o cartão a ser criado já esteja cadastrado para o usuário, a resposta deverá ser:
# STATUS 422 - {"error": ["This card is already registered for this user"]}
        payment_method = attrs["payment_method"]

        return super().validate(attrs)
# Não será possível o cadastro do mesmo cartão para o usuário, exceto, caso o método de pagamento seja
#  diferente, ou seja, 2 cartões iguais porém um é de crédito e o outro é de débito.
