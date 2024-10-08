# PAGAR.ME

- [Traduções](#traduções)
- [Sobre](#sobre)
- [Instalação](#instalação)
- [Diagrama](#diagrama)
- [Descrição](#Description)
- [Documentação](#documentação)
- [Referências](#referências)
- [Termos de uso](#termos-de-uso)

<br>

## Traduções

- [English / Inglês](https://github.com/AndreKuratomi/pagar.me)
- [Português brasileiro](./README_pt-br.md)

<br>

## Sobre

<p>A API <strong>Pagar.me</strong> é uma versão simplificada de um market place e também um sistema de pagamentos, onde é possível comprar produtos e processar transações. Esta aplicação utiliza o framework <strong>Django</strong> e suas <strong>Generic Views</strong>.</p>

<br>

## Descrição

A API <b>Pagar.me</b> possui 4 tabelas  base: Usuários (Accounts), produtos (Product), taxas por transação (Fee), e informações de pagamento (PaymentInfo). Seguem as descrições sucintas de cada uma e suas regras de cadastro:

USUÁRIOS:
    
    Tipos:

        Existem 3 tipos de usuários: Vendedor (seller), Administrador (admin) e o usuário comum (aquele que não é nem vendedor nem administrador):
    
    Permissões:
        - Apenas usuários administradores logados podem cadastrar outro usuário e listá-los.
        - Todos os usuários logados podem atualizar seus prórios dados.

PRODUTOS:
    
    Permissões:

        - Apenas usuários vendedores logados podem cadastrar produtos e listá-los por id. 
        - Um vendedor pode ver todos os produtos que listou.
    
    Regras de cadastro:

        Os produtos a serem cadastrados devem ter a quantidade mínima de 1 exemplar.

TAXAS POR TRANSAÇÃO:
    
    Permissões:
        Apenas usuários administradores logados podem cadastrar taxas e listá-las.
    
    Outros:
        - As taxas padrões no sistema são:

            Cartão de crédito - 5%
            Cartão de débito - 3%

        - Não é possível a exclusão de taxas no sistema.

MEIOS DE PAGAMENTO:
    
    Permissões:
        Apenas usuários logados que não são nem administradores nem vendedores podem cadastrar cartões e listá-los.
    
    Regras de cadastro:
        - Não podem ser cadastrados cartões fora do prazo de validade.
        - Um cartão com o mesmo número pode ser registrado mais de uma vez se os métodos de pagamento forem diferentes (ex: crédito ou débito).
    
    Outros:
        - Só são exibidos os 4 últimos números do cartão
        - O número CVV é, assim como a senha do usuário, cadastrado mas não exibido.

A seguir, o diagrama das tabelas:
<br>

## Diagrama

<figure>
    <img src="../pagar_me.drawio.png" alt="diagrama de tabelas">
    <figcaption style="text-align: center">Relacionamento das tabelas</figcaption>
</figure>

<br>

## Instalação

<h3>0. Primeiramente, é necessário já ter instalado na própria máquina:</h3>

- O versionador de codigo <b>[Git](https://git-scm.com/downloads)</b>.

- A linguagem de programacao <b>[Python](https://www.python.org/downloads/)</b>.

- Um <b>editor de código</b>, conhecido também como <b>IDE</b>. Por exemplo, o <b>[Visual Studio Code (VSCode)](https://code.visualstudio.com/)</b>.

- <p> E versionar o diretório escolhido para receber o clone da aplicação:</p>

```
git init
```
<br>

<h3>1. Fazer o clone do repositório 'pagar.me' na sua máquina pelo terminal do computador ou pelo do IDE:</h3>

```
git clone https://github.com/AndreKuratomi/pagar.me.git
```

WINDOWS:

Obs: Caso apareca algum erro semelhante a este: 

```
unable to access 'https://github.com/AndreKuratomi/pagar.me.git': SSL certificate problem: self-signed certificate in certificate chain
```

Configure o git para desabilitar a certificação SSL:

```
git config --global http.sslVerify "false"
```

<p>Entrar na pasta criada:</p>

```
cd pagar.me
```
<br>

<h3>2. Após feito o clone do repositório, instalar:</h3>

<h4>O ambiente virtual e atualizar suas dependências com o seguinte comando:</h4>

LINUX:
```
python3 -m venv venv --upgrade-deps
```

WINDOWS:
```
py -m venv venv
```

<h4>Ative o seu ambiente virtual com o comando:</h4>

LINUX:
```
source/venv/bin/activate
```

WINDOWS:

No sistema operacional Windows é necessário antes configurar o Execution Policy do PowerShell:

```
Get-ExecutionPolicy # para verificar o tipo de política de execução
Set-ExecutionPolicy RemoteSigned # para alterar o tipo de política se o comando acima mostrar 'Restricted'
```
Obs: Eventualmente, pode ser necessário abrir o PowerShell como administrador.

```
.\env\Scripts\activate
```


<h4>Instalar suas dependências:</h4>

```
pip install -r dependencias.txt
```

WINDOWS:

Caso seja retornado algum erro semelhante a este:

```
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\andre.kuratomi\\OneDrive - Company\\Área de Trabalho\\pagar.me\\pagar.me\\env\\Lib\\site-packages\\jedi\\third_party\\django-stubs\\django-stubs\\contrib\\contenttypes\\management\\commands\\remove_stale_contenttypes.pyi'
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths
```

Rode no cmd como adminstrador o seguinte comando:

```
reg.exe add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f
```
<br>
<h3>3. Rodar a aplicação no seu IDE:</h3>

```
code .
```
<br>

<h3>4. E ativar o django:</h3>

LINUX:
```
python manage.py runserver
```

WINDOWS:
```
py manage.py runserver
```
<br>

<br>


## Documentação

Para ter acesso ao descrições detalhes das rotas e seus retornos, conferir documentação completa no link a seguir:

https://pagar-5frujasuz-abkuras-projects.vercel.app/

<br>

## Referências

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Generic views](https://www.django-rest-framework.org/api-guide/generic-views/)
- [Git](https://git-scm.com/downloads)
- [Insomnia-documenter](https://www.npmjs.com/package/insomnia-documenter)
- [Insomnia-documenter (quick tutorial)](https://www.youtube.com/watch?v=pq2u3FqVVy8)
- [Python](https://www.python.org/downloads/)
- [SQLite3](https://docs.python.org/3/library/sqlite3.html)
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/)

<br>

## Termos de uso

Esse projeto atende a fins exclusivamente didáticos sem nenhum intuito comercial.
