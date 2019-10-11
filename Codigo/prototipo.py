import requests
import lxml.html

url = 'https://www.amazon.com.br/Action-Figure-Sonic-Hedgehog-Boom/dp/B01AKT1Y50/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sonic&qid=1569325718&s=gateway&sr=8-1'

res = requests.get(url, headers={'user-agent':'bot by quakcduck'})

while(res.status_code == 503):
    html = requests.get('https://www.amazon.com.br/Action-Figure-Sonic-Hedgehog-Boom/dp/B01AKT1Y50/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sonic&qid=1569325718&s=gateway&sr=8-1')

if res.status_code == 200:
    print("Conexao bem sucedida")

doc = lxml.html.fromstring(res.content)

corpo = doc.xpath('//*[@id="dp"]')[0]

nome_produto = corpo.xpath('.//*[@id="productTitle"]/text()')
separador = ""
separador = separador.join(nome_produto)

preco_produto = corpo.xpath('.//*[@id="priceblock_ourprice"]/text()')

print('Nome: ', separador.strip())
print('Preco: ', preco_produto)