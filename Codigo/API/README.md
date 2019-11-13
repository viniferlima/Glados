# Como utilizar

## Requisitos
 - Python 3
 - Ipython - Um terminal interativo (REPL)
 - virtualenv ou virtualenv wrapper - para criação de ambientes isolados
 - Um editor de código ou IDE de sua preferência - (Gedit, Notepad++, sublime, Emacs, VIM, Atom, VisualStudio Code, etc)
 - Um browser ou Postman (ou correlatos)
 - Dataset - Biblioteca para acesso a bancos de dados
 - Flask
 
## Primeiros passos
 - Subir o banco local 
    - sudo /opt/lampp/lampp start
    - verificar se o banco foi iniciado corretamente em http://localhost/phpmyadmin/
 - Subir o ambiente isolado
    - $ sudo apt-get install virtualenvwrapper
    - $ mkvirtualenv flasktest_env 
 - Instalar o Flask no ambiente - $ pip3 install flask
 - Instalar o ipython no ambiente - $ pip3 install ipython
 - Instalar o restante das Libs utilizadas
 - Iniciar a aplicação - $ python3 app.py
 - Acessar http://localhost:5000/ para que a aplicação inicie
    - Pode também ser acessado pelo postman para uma visualização mais limpa.
    - O terminal do virtualenv imprime alguns dados dos produtos! Pode ser utilizado para consultar o andamento do script! Note que alguns campos impressos, ainda não são utilizados na API.

## Observações importantes!
Esta é a primeira versão da API. Além de realizar a raspagem de varios produtos (o campo de pesquisa está chumbado no próprio código! Deve ser realizada a integração com o front para receber o campo que o usuário pesquisou e retornar com base no timestamp!), ela retorna **todos** os produtos salvos do banco!

## Exemplo de retorno de um produto

      {
        "categoria": "Livros",
        "data_consulta": "Fri, 18 Oct 2019 17:12:32 GMT",
        "disponibilidade": "Em estoque.",
        "id": 1,
        "nome": "Batman - O Longo Dia das Bruxas - Edição Definitiva",
        "porcentagem_desconto": 30.49,
        "preco_cheio": 99.0,
        "preco_desconto": 68.81,
        "site": "Amazon"
      } 