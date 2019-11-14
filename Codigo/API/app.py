import requests # pip3 install requests
import lxml # pip3 install lxml
from lxml import html
from datetime import datetime # pip3 install datetime
import re # 
import schedule # pip3 install schedule
import time #  
import xlsxwriter # pip3 install xlsxwriter
import pymysql # pip3 install pymysql 
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/')
def BotFlask():

    #busca = input("Digite o nome do produto: ")
    busca = ('batman')
    link = ('https://www.amazon.com.br/s?k=ProdutoPesquisado&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss')
    url = link.replace("ProdutoPesquisado",busca.strip())
    res = requests.get(url, headers={'user-agent': 'glados'})
    errors = []

    def track(url):
        x = url.split(".")
        # Trocar user-agent pelo da sua máquina (Google -> my user agent)
        res = requests.get(url, headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'})
        while(res.status_code == 503):
            print('Sem conexão! :c')
        else:    
            try:
                doc = html.fromstring(res.content)

                separador = ""

                # Site pesquisado
                if(x[1] == "amazon"):
                    dominio = "Amazon"
                if(x[1] == "submarino"):
                    dominio = "Submarino"
                if(x[1] == "saraiva"):
                    dominio = "Saraiva"

                # Nome do produto
                nome_produto = doc.xpath('.//*[@id="productTitle"]/text()')
                nome = separador.join(nome_produto).strip()

                # Categoria do produto
                categoria = doc.xpath('.//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[1]/span/a/text()')
                cat = separador.join(categoria).strip()

                # Preço cheio do produto
                fullprice = doc.xpath('.//*[@id="buyBoxInner"]/ul/li[1]/span/span[2]/text()')
                fullprice2 = doc.xpath('.//*[@id="price"]/table/tbody/tr[1]/td[2]/span[1]/text()')

                fullp = separador.join(fullprice)
                fullp2 = separador.join(fullprice2)

                semdesc = fullp or fullp2
                #semdesc = separador.join(fullprice_final)

                # Preço atual do produto
                preco_produto = doc.xpath('.//*[@id="soldByThirdParty"]/span/text()')
                preco_produto2 = doc.xpath('.//*[@id="price_inside_buybox"]/text()')
                preco_produto3 = doc.xpath('.//*[@id="unqualifiedBuyBox"]/div/div[1]/span/text()')
                preco_produto4 = doc.xpath('.//*[@id="priceblock_ourprice"]/text()')

                preco = separador.join(preco_produto)
                preco2 = separador.join(preco_produto2)
                preco3 = separador.join(preco_produto3)
                preco4 = separador.join(preco_produto4)

                price = preco.strip() or preco2.strip() or preco3.strip() or preco4.strip()
                if (semdesc > preco or semdesc > preco2 or semdesc > preco3 or semdesc > preco4):
                    fup = semdesc.strip()
                else:
                    fup = preco.strip() or preco2.strip() or preco3.strip() or preco4.strip()

                price = price.replace("R$", "").replace(",", ".")
                price = float(price)
                fup = fup.replace("R$", "").replace(",",".")
                fup = float(fup)

                # Desconto em %
                desconto = "%.2f" % round(((1 - (price/fup))*100),2)

                # Disponibilidade do produto
                av = doc.xpath('.//*[@id="availability"]/span/text()')
                disp = separador.join(av).strip()

                # Data da consulta
                data_atual = datetime.today()
                data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

                img = doc.xpath('.//*[@id="imgBlkFront"]/@data-a-dynamic-image')

                print()
                print('Nome: ', nome)
                print('Categoria: ', cat)
                print("Preco atual: ", price)
                print('Preço sem desconto: ', fup)
                print("Porcentagem de desconto: ", desconto, "%")
                print("Consultado em: ", data_em_texto)
                print("Site: ", dominio)
                print("Disponibilidade: ", disp)
                print(img)

                connection = pymysql.connect(host="localhost", user="root", passwd="", database="glados")
                cursor = connection.cursor()
                insert1 = "INSERT INTO produtos_test(nome, categoria, preco_cheio, preco_desconto, porcentagem_desconto, site, disponibilidade) VALUES ('{}', '{}', {}, {}, {}, '{}', '{}');".format(nome, cat, fup, price, desconto, dominio, disp)
                #print("Código SQL para consulta: ")
                #print(insert1)
                #print()
                cursor.execute(insert1)
                connection.commit()
                connection.close()
            except:
                errors.append(url)


    doc = lxml.html.fromstring(res.content)
    corpo = doc.xpath('//*[@class="sg-row"]')[0]
    separador = "\n"
    link_produto = corpo.xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[*]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/@href')
    link_site = separador.join(link_produto)
    z = link_site.split("\n")
    qtde = len(z)
    i = 0

    urls = []

    while(i < qtde):
        path = str('https://www.amazon.com.br' + z[i])
        urls.append(path)
        i = 1 + i

    def search():
        for url in urls: 
            track(url)
        #else:
        #    print("Finalizado.")

    search()

    def select_all(conn):
    
    #Query all rows in the tasks table
    #:param conn: the Connection object
    #:return:
        cur = conn.cursor()
        cur.execute("SELECT id, nome, categoria, preco_cheio, preco_desconto, porcentagem_desconto, site, disponibilidade, data_consulta FROM produtos_test")

        rows = cur.fetchall()

        lista = []
        for row in rows:
            ad = {}
            ad.update({'id': row[0]})
            ad.update({'nome':row[1]})
            ad.update({'categoria':row[2]})
            ad.update({'preco_cheio':row[3]})
            ad.update({'preco_desconto':row[4]})
            ad.update({'porcentagem_desconto':row[5]})
            ad.update({'site':row[6]})
            ad.update({'disponibilidade':row[7]})
            ad.update({'data_consulta':row[8]})
            lista.append(ad)
        

        #print(json.dumps(lista))
        conn.commit()
        conn.close()
        return(lista)

    conn = pymysql.connect(host="localhost", user="root", passwd="", database="glados")             
    
    plist = select_all(conn)
    
    return jsonify(plist)
    


app.run()
