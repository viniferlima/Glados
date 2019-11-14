import requests
import lxml
from lxml import html
from datetime import datetime
import re
from flask import Flask
from flask import jsonify
app = Flask(__name__)



@app.route('/')
def BotFlask():
    
    dados = []
    urls = []
    i = 0

    busca = "Eden"
    link = ('https://www.amazon.com.br/s?k=ProdutoPesquisado&i=stripbooks&__mk_pt_BR=ÅMÅŽÕÑ&ref=nb_sb_noss_2')
    url = link.replace("ProdutoPesquisado",busca.strip())

    res = requests.get(url, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'})
    
    doc = lxml.html.fromstring(res.content)
    corpo = doc.xpath('//*[@class="sg-row"]')[0]

    separador = "\n"
    link_produto = corpo.xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[*]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/@href')
    link_site = separador.join(link_produto)
    z = link_site.split("\n")
    qtde = len(z)

    while(i < qtde):
        res = requests.get(url, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'})
        path = str('https://www.amazon.com.br' + z[i])
        urls.append(path)
        i = 1 + i

    for url in urls:

        res = requests.get(url, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'})
        
        while(res.status_code == 503):
            print('Sem conexão! :c')
            
        else:    
            res = requests.get(url, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'})
            doc = html.fromstring(res.content)
            separador = ""

            # Site pesquisado
            site = (re.findall("amazon", url) or re.findall("submarino", url) or re.findall("saraiva", url))
            dominio = site[0].capitalize()
            print(dominio)

            # Nome do produto
            nome_produto = doc.xpath('.//*[@id="productTitle"]/text()')
            nome = separador.join(nome_produto).strip()
            print(nome)

            # Categoria do produto
            categoria = doc.xpath('.//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[1]/span/a/text()')
            cat = separador.join(categoria).strip()
            print(cat)

            # Preço cheio do produto
            fullprice = doc.xpath('.//*[@id="buyBoxInner"]/ul/li[1]/span/span[2]/text()')
            semdesc = separador.join(fullprice)
            print(semdesc)

            # Preço do produto
            preco_produto = doc.xpath('.//*[@id="soldByThirdParty"]/span/text()')
            preco_produto2 = doc.xpath('.//*[@id="price_inside_buybox"]/text()')
            preco_produto3 = doc.xpath('.//*[@id="unqualifiedBuyBox"]/div/div[1]/span/text()')
            preco_produto4 = doc.xpath('.//*[@id="priceblock_ourprice"]/text()')                

            preco = separador.join(preco_produto)
            preco2 = separador.join(preco_produto2)
            preco3 = separador.join(preco_produto3)
            preco4 = separador.join(preco_produto4)

            print(preco)
            print(preco2)
            print(preco3)
            print(preco4)
            
            price = preco.strip() or preco2.strip() or preco3.strip() or preco4.strip()
            if (semdesc > preco or semdesc > preco2 or semdesc > preco3 or semdesc > preco4):
                fup = semdesc.strip()
            else:
                fup = preco.strip() or preco2.strip() or preco3.strip() or preco4.strip()

            
            price = price.replace("R$", "").replace(",", ".")
            #price = float(price)
            fup = fup.replace("R$", "").replace(",",".")
            #fup = float(fup)

            print(fup)

            # Desconto em %
            #desconto = "%.2f" % round(((1 - (price/fup))*100),2)
            #desconto = str(desconto)
            #desconto = desconto + "%"

            # Disponibilidade do produto
            av = doc.xpath('.//*[@id="availability"]/span/text()')
            disp = separador.join(av).strip()

            # Data da consulta
            data_atual = datetime.today()
            data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

            dado = {
                "nome": nome,
                "preco": price
            }

            dados.append(dado)


    print("Finalizado.")
    return jsonify(dados)
