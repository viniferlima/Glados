import requests
import lxml.html

# Links para teste:
# url2 = 'https://www.amazon.com.br/gp/product/8562848107/ref=ox_sc_act_title_1?smid=A1ZZFT5FULY4LN&psc=1'
# url = 'https://www.amazon.com.br/Action-Figure-Sonic-Hedgehog-Boom/dp/B01AKT1Y50/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sonic&qid=1569325718&s=gateway&sr=8-1'
# url3 = 'https://www.amazon.com.br/Akira-5-Katsuhiro-Otomo/dp/8545712367/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=akira&qid=1569456784&sr=8-5'

url = input("Digite o link do produto: ")
res = requests.get(url, headers={'user-agent':'glados'})

while(res.status_code == 503):
    html = requests.get(url)

#if res.status_code == 200:
#    print("Conexao bem sucedida")

doc = lxml.html.fromstring(res.content)

corpo = doc.xpath('//*[@id="dp"]')[0]


nome_produto = corpo.xpath('.//*[@id="productTitle"]/text()')
separador = ""
nome = separador.join(nome_produto)


preco_produto = corpo.xpath('.//*[@id="soldByThirdParty"]/span/text()')
preco_produto2 = corpo.xpath('.//*[@id="price_inside_buybox"]/text()')
preco = separador.join(preco_produto)
preco2 = separador.join(preco_produto2)

fullprice = corpo.xpath('.//*[@id="buyBoxInner"]/ul/li[1]/span/span[2]/text()')
semdesc = separador.join(fullprice)

# estudar como salvar o link da imagem do produto, abaixo temos o provável xpath da imagem
# linkimg = corpo.xpath('.//*[@id="imgBlkFront"]/text()')  

print()
print('Nome: ', nome.strip())

# Utilizado concatenação nas duas variaveis de preço, pois uma delas é nula. Será criada uma variavel
# que receberá o preço do produto e rejeitará as outras variáveis nulas (Provavelmente com '||' (OR))
print('Preco atual: ' + preco.strip() + preco2.strip())

if (semdesc > preco or semdesc > preco2):
    print('Preço sem desconto: ', semdesc)
else:
    print('Preço sem desconto: ' + preco.strip() + preco2.strip())

print()