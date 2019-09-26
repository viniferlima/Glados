import requests
import lxml.html
import schedule
import time

def raspagem():
    url = 'https://www.amazon.com.br/Brinquedo-Carrinhos-Fric%C3%A7%C3%A3o-Sonic-Racing/dp/B07NLGM3MP/ref=sr_1_11?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sonic&qid=1569368826&sr=8-11'

    res = requests.get(url, headers={'user-agent':'bot by quakcduck'})

    while(res.status_code == 503):
        html = requests.get(url)

    if res.status_code == 200:
        print("Conexao bem sucedida")

    doc = lxml.html.fromstring(res.content)

    corpo = doc.xpath('//*[@id="dp"]')[0]

    nome_produto = corpo.xpath('.//*[@id="productTitle"]/text()')
    separador_nome = ""
    separador_nome = separador_nome.join(nome_produto)
    preco = ""
    preco_produto = corpo.xpath('.//*[@id="price_inside_buybox"]/text()')

    print('Nome: ', separador_nome.strip())
    print('Preco: ', preco.join(preco_produto).strip())

    f = open('file.txt', 'w')
    f.write(separador_nome.strip())
    f.write("\n")
    f.write(preco.join(preco_produto).strip())


schedule.every(5).seconds.do(raspagem)

while 1:
    schedule.run_pending()
    time.sleep(1)