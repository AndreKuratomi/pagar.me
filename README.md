## PAGAR.ME

- [Sobre](#sobre)
- [Instalação](#instalação)
- [Documentação](#documentação)
- [Termos de uso](#termos-de-uso)

<br>

# Sobre

<p><strong>Pagar.me</strong> é uma versão simplificada de um market place e também um sistema de pagamentos, onde é possível comprar produtos e processar transações. Esta aplicação utiliza o framework <strong>Django</strong> e <strong>Generic Views</strong>.</p>
<br>

# Instalação

<h5>0. Primeiramente, é necessário já ter instalado na própria máquina:</h5>

- <p> Um <b>editor de código</b>, conhecido também como <strong>IDE</strong>. Por exemplo, o <b>[Visual Studio Code (VSCode)](https://code.visualstudio.com/)</b>.</p>

- <p> Uma <b>ferramenta cliente de API REST</b>. Por exemplo, o <b>[Insomnia](https://insomnia.rest/download)</b> ou o <b>[Postman](https://www.postman.com/product/rest-client/)</b>.</p>

- <p> E versionar o diretório para receber o clone da aplicação:</p>

```
git init
```

<br>
<h5>1. Fazer o clone do repositório <strong>Pagar.me</strong> na sua máquina pelo terminal do computador ou pelo do IDE:</h5>

```
git clone git@gitlab.com:ABKURA/pagar.me.git
```

<p>Entrar na pasta criada:</p>

```
cd pagar.me
```

Após feito o clone do repositório Pagar.me, instalar:

O ambiente virtual e atualizar suas dependências com o seguinte comando:

```
python -m venv venv --upgrade-deps
```

Ative o seu ambiente virtual com o comando:

```
source/venv/bin/activate
```

Instalar suas dependências:

```
pip install -r requirements.txt
```

E rodar a aplicação:

```
code .
```

# Documentação

Para ter acesso ao descrições detalhes das rotas e seus retornos, conferir documentação completa no link a seguir:

https://pagar-me-documentation.vercel.app/

# Termos de uso

Esse projeto atende a fins exclusivamente didáticos e sem nenhum intuito comercial.
