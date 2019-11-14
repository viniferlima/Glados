<div align="center">
    <img src="./glados.png" width="320" />
    <div height="50"></div>
</div>

<br>

# Gla o que?

Glados é um projeto de Web bot que será capaz de coletar dados de produtos variados a fim de mensurar a evolução de seu preço, comparando-o também em diferentes sites com o intuito de dar ao publico alvo a chance de pesquisar antes de realizar uma compra.

# Por que Glados?

> *"We're a lot alike, you and I. You tested me. I tested you. You killed me. I—oh, no, wait. I guess I haven't killed you yet. Well. Food for thought." (GLaDOS)*

[GLaDOS](https://half-life.fandom.com/wiki/GLaDOS) (Genetic Lifeform and Disk Operating System) é uma inteligência artificial criada pela Aperture Science do jogo Portal e Portal 2, e é a principal antagonista. Ela é responsável pela manutenção e pelos testes realizados na Aperture e tomamos como inspiração seu personagem para nomear o Web bot.

# O que esse tal Glados faz?

### Problema 😖

Devido a grande diversidade de sites e descontos, há cada vez mais uma grande dificuldade entre os usuários de encontrar o melhor preço de produtos on-line.

### Valor agregado 💸

Glados tem como objeto proporcionar uma economia financeira e satisfação pessoal ao usuário, auxiliando-o a realizar a compra do produto almejado pelo melhor preço de maneira mais eficiente. Um segundo objetivo é exibir avaliações de outros usuários sobre o produto para que o cliente se sinta seguro de que está realizando a compra certa.

### Segmento de mercado 💼

Clientes de e-commerce que visam a econômia e praticidade ao realizar suas compras on-line e clientes que monitoram suas listas de desejos para realizarem a compra no preço mais baixo.

### O que estamos usando?:thinking:

Estamos usando a linguagem de programação Python, escolhemos esta linguagem pois é a mais completa em questão de bibliotecas e afins usados para a raspagem de dados.<br>
Estamos tambem usando a as bibliotecas requests, lxml, pymsql e schedule para, respectivamente, fazer a conexão com o site a ser raspado, raspar o site, fazer a conexão com o banco e repetir o processo periodicamente.<br>
Para servidor Web local utilizamos uma plataforma a XAMPP que proporciona uma plataforma de testes, sendo que o mesmo oferece um modulo Apache e MySQL usados para supotar o banco de dados na maquina local.<br>

### Como usar:

Para o uso da aplicação e necessario instalar alguns programas e suas extensões: <br>
Primeiramente para que o bot Glados seja usado será necessário o download do arquivo do bot que se encontra página do gitlab, para isso siga os passos a seguir: <br>
    Instalação do git bash here. <br>
1. Inicie com o download do git bash acessando o link a seguir: https://git-scm.com/download/win <br>
2. Instale o arquivo assim que finalizar o download. <br>
    Uso do git Bash Here. <br>
1. Primeiro crie uma pasta na sua area de trabalho, esta será a pasta que você usará como servidor local do seu Git.<br>
2. Dentro da pasta clique com o botao direito e selecione a opção Git Bash Here, isto irá abrir o console do Git com a base nesta pasta.<br>
3. No console use o comando "git config --global user.email" para logar no seu gitbash, use o email cadastrado no GitLab.<br>
4. Também cadastre seu nome com "git config --global user.name".<br>
5. No console use o comando “git clone” e cole (Ctrl + V não funciona, use o botao direito + colar ou shift + botão insert) o link: https://gitlab.com/omnitron/glados.git .<br>
6. Em seguida use o comando “git pull” para puxar os arquivos do GitLab para a sua pasta local.<br>
Pronto agora temos todos os arquivos do Bot em seu computador. <br>
    Download do Python 3 e instalação: <br>
1. Iniciamos baixando a IDLE e o Python 3.7.4 pelo link para windows https://www.python.org/downloads/release/python-374/ . É necessario verificar o tipo de
sistema de seu computador, se ele e 64 bits ou 32 bits. <br>
2. Após essa verificação selecione o tipo correto de arquivo para download, assim que selecionado já iniciará o download. <br>
2º Assim que finalizado o download, execute o arquivo, que abrirá uma janela de instalação. <br>
3. Terá duas caixas de seleção é recomendável que deixe as duas marcadas.<br>
4. Clique em install now, será pedido uma autorização clique em sim, após isso iniciará a instalação. <br>
5. Ao terminar a instalação aparecerá uma nova janela é recomendável que desabilite a limitação do path, desta forma finalizando a instalação e clique em close. <br>
    Agora iniciaremos o download e a instalação da IDE do PyCharm. <br>
1. Para isso acesse o link a seguir: https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC Para windows. <br>
2. Após o final do download execute o arquivo, se caso peça alguma autorização clique em sim e depois em Next. <br>
3. A próxima janela é para escolher o caminho da pasta (é recomendável que deixe o mesmo caminho). <br>
4. Em seguida clique em Next, que iniciará a instalação.<br>
Pronto agora temos a  IDE do PyCharm insatalado e pronto para o uso. <br>
    Bibliotecas. <br>
Para o uso do bot é necessário instalar algumas bibliotecas: <br>
1. Abra o arquivo BotFlask.py <br>
2. Na parte de baixo da IDE do PyCharm procure por Terminal. <br>
3. Inicie a inslação das bibliotecas da seguinte forma: <br>
    Primeiro digite: pip install lxml <br>
    e espere ate o finalizar a instalação da biblioteca, repita o mesmo processo para as seguintes bibliotecas:<br>
    pip install requests <br>
    pip install datetime <br>
    pip install pymysql <br>
    Instalação do Flask: <br>
Será necesssário adicionar mais algumas configurações para que o Bot funcione no seu computador, desta forma siga as instruções a seguir: <br>
1. No buscador no menu inicial de seu computador busque por ' cmd ' ou ' Prompt de Comando ' (sem  as ''). <br>
2. Após feito isso abra o cmd ou Prompt de Comando, digite cd e o caminho para sua pasta local, onde baixou os arquivos. <br>
3. O próximo passo é executar o flask para isso continue no cmd e execute os seguintes comandos: <br>
    >set flask_app=BotFlask.py <br>
    flask run <br>
    Assim sendo BotFlask.py o nome do arquivo. <br>

# Integrantes:

:computer: André Luiz Dias Custodio <br>
:computer: Igor Carvalho <br>
:computer: Luciano Donizetti <br>
:computer: Perilo <br>
:computer: Vinícius <br>
