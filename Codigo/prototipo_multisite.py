import requests
import lxml.html

url = 'https://www.saraiva.com.br/dark-souls-o-suspiro-de-andolus-9727636/p'

res = requests.get(url, headers={'user-agent':'bot by glados'})

while(res.status_code == 503):
    html = requests.get(url)

if res.status_code == 200:
    print("Conexao bem sucedida")

x = url.split(".")

if(x[1] == "amazon"):
    corpo_xpath = './/*[@id="dp"]'
    nome_xpath = './/*[@id="productTitle"]/text()'
    preco_xpath = './/*[@id="priceblock_ourprice"]/text()'
elif(x[1] == "submarino"):
    corpo_xpath = './/*[@id="content"]'
    nome_xpath = './/*[@id="product-name-default"]/text()'
    preco_xpath = '//*[@id="offer-5b1e80c9b492dcdc1c8b97cc"]/div/div[2]/div/div/p[2]/span'
elif(x[1] == "saraiva"):
    corpo_xpath = '/html/body'
    nome_xpath = './/*[@id="app"]/main/section[1]/div/div/div[2]/header/div[1]/h1/div/text()'
    preco_xpath = './/*[@id="tab1"]/section/div[1]/div[1]/div[1]/div/div/p[1]/em[2]/strong'
   
doc = lxml.html.fromstring(res.content)

corpo = doc.xpath(corpo_xpath)[0]

nome_produto = corpo.xpath(nome_xpath)
separador = ""
separador = separador.join(nome_produto)

preco_produto = corpo.xpath(preco_xpath)

print('Nome: ', separador.strip())
print('Preco: ', preco_produto)