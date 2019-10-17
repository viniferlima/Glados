import lxml.html
import re
import requests


busca = input("Digite o nome do produto: ")
link = ('https://www.amazon.com.br/s?k=ProdutoPesquisado&i=stripbooks&__mk_pt_BR=ÅMÅŽÕÑ&ref=nb_sb_noss_2')
url = link.replace("ProdutoPesquisado",busca.strip())
res = requests.get(url, headers={'user-agent': 'glados'})

site = (re.findall("amazon", url) or re.findall("submarino", url) or re.findall("saraiva", url))
dominio = site[0].capitalize()

def maincode():
    while (res.status_code == 503):
        html = requests.get(url)

    doc = lxml.html.fromstring(res.content)

    corpo = doc.xpath('//*[@class="sg-row"]')[0]

    nome_produto = corpo.xpath('.//*[@class="a-size-medium a-color-base a-text-normal"]/text()')
    separador = "\n"
    nome = separador.join(nome_produto)

    preco_produto = corpo.xpath('.//*[@class="a-offscreen"]/text()')

    link_produto = corpo.xpath('.//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[2]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/@href')


    preco = separador.join(preco_produto)

    x = nome.split("\n")
    y = preco.split("\n")
    z = link_produto


    qtde = len(x)

    i = 0

    while(i < qtde):
        print(x[i])
        print(y[i], "\n")
        print(z[i])
        i = 1 + i

maincode()
