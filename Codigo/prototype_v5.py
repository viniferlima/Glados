import requests # pip3 install requests
import lxml # pip3 install lxml
from lxml import html
from datetime import datetime # pip3 install datetime
import re # 
import schedule # pip3 install schedule
import time #  
import xlsxwriter # pip3 install xlsxwriter
import pymysql # pip3 install pymysql 
import interpy # pip3 install interpy




def track(url):
    res = requests.get(url, headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}) # Trocar user-agent pelo da sua máquina
    #html = requests.get(url)
    while(res.status_code == 503):
        print('Sem conexão! :c')
    #    html = requests.get(url)   
    #    time.sleep(1)
    else:    
        doc = html.fromstring(res.content)

        #corpo = doc.xpath('//*[@id="dp"]')[0]

        separador = ""

        # Site pesquisado
        site = (re.findall("amazon", url) or re.findall("submarino", url) or re.findall("saraiva", url))
        dominio = site[0].capitalize()
        #dominio = dominio.capitalize()

        # Nome do produto
        nome_produto = doc.xpath('.//*[@id="productTitle"]/text()')
        nome = separador.join(nome_produto).strip()

        # Categoria do produto
        categoria = doc.xpath('.//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[1]/span/a/text()')
        cat = separador.join(categoria).strip()

        # Preço cheio do produto
        fullprice = doc.xpath('.//*[@id="buyBoxInner"]/ul/li[1]/span/span[2]/text()')
        semdesc = separador.join(fullprice)

        # Preço do produto
        preco_produto = doc.xpath('.//*[@id="soldByThirdParty"]/span/text()')
        preco_produto2 = doc.xpath('.//*[@id="price_inside_buybox"]/text()')
        preco = separador.join(preco_produto)
        preco2 = separador.join(preco_produto2)
        price = preco.strip() or preco2.strip()
        if (semdesc > preco or semdesc > preco2):
            fup = semdesc.strip()
        else:
            fup = preco.strip() or preco2.strip()

        price = price.replace("R$", "").replace(",", ".")
        price = float(price)
        fup = fup.replace("R$", "").replace(",",".")
        fup = float(fup)

        # Desconto em %
        desconto = "%.2f" % round(((1 - (price/fup))*100),2)
        #desconto = str(desconto)
        #desconto = desconto + "%"

        # Disponibilidade do produto
        av = doc.xpath('.//*[@id="availability"]/span/text()')
        disp = separador.join(av).strip()

        # Data da consulta
        data_atual = datetime.today()
        data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
	
	    #print()
        #print('ID: ', z)
        print('Nome: ', nome)
        print('Categoria: ', cat)
        print("Preco atual: ", price)
        print('Preço sem desconto: ', fup)
        print("Porcentagem de desconto: ", desconto)
        print("Consultado em: ", data_em_texto)
        print("Site: ", dominio)
        print("Disponibilidade: ", disp)
        print()

        connection = pymysql.connect(host="localhost", user="root", passwd="", database="glados")
        cursor = connection.cursor()

        insert1 = "INSERT INTO produtos(nome, categoria, preco, preco_desconto, porcentagem_desconto, site, disponivel) VALUES ('{}', '{}', {}, {}, {}, '{}', '{}');".format(nome, cat, fup, price, desconto, dominio, disp)
        print(insert1)
        print()
        cursor.execute(insert1)
        connection.commit()
        connection.close()




#n = 1
urls = []
#url = input("Digite o link do produto: ")

url = "https://www.amazon.com.br/Batman-Longo-Bruxas-Edi%C3%A7%C3%A3o-Definitiva/dp/8573514353/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=batman&qid=1570144258&sr=8-1"
urls.append(url)
#track(url, 1)

#url = "https://www.amazon.com.br/Batman-Noir-Cavaleiro-das-Trevas/dp/8583684154/ref=sr_1_4?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=batman&qid=1570144258&sr=8-4"
#urls.append(url)
#track(url, 2)

url = 'https://www.amazon.com.br/Di%C3%A1rio-Anne-Frank-Quadrinhos/dp/8501109673/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=quadrinhos&qid=1570489605&sr=8-1'
urls.append(url)
#track(url, 3)

url = 'https://www.amazon.com.br/Quadrinhos-arte-sequencial-Will-Eisner/dp/8578273079/ref=sr_1_3?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=quadrinhos&qid=1570489605&sr=8-3'
urls.append(url)
#track(url, 4)

url = 'https://www.amazon.com.br/%C3%9Altimo-Voo-das-Borboletas/dp/8593695361/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=pipoca+e+nanquim&qid=1570489630&sr=8-1'
urls.append(url)
#track(url, 5)

url = 'https://www.amazon.com.br/Um-Pedaço-Madeira-Aço-Exclusivo/dp/8593695108/ref=sr_1_2?__mk_pt_BR=ÅMÅŽÕÑ&keywords=pipoca+e+nanquim&qid=1570489630&sr=8-2'
urls.append(url)
#track(url, 6)

url = 'https://www.amazon.com.br/Lone-Sloane-Único-Exclusivo-Amazon/dp/8593695205/ref=sr_1_3?__mk_pt_BR=ÅMÅŽÕÑ&keywords=pipoca+e+nanquim&qid=1570489630&sr=8-3'
urls.append(url)
#track(url, 7)

url = 'https://www.amazon.com.br/Desonra-Kubidai-Hikiukenin-Exclusivo-Amazon/dp/8593695329/ref=sr_1_4?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=pipoca+e+nanquim&qid=1570489630&sr=8-4'
urls.append(url)
#track(url, 8)

url = 'https://www.amazon.com.br/Grande-Odalisca-2-Olympia/dp/8593695388/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=pipoca+e+nanquim&qid=1570489630&sr=8-5'
urls.append(url)
#track(url, 9)

url = 'https://www.amazon.com.br/Grande-Odalisca-Exclusivo-Amazon/dp/859369537X/ref=pd_bxgy_14_img_2/130-5784877-1003836?_encoding=UTF8&pd_rd_i=859369537X&pd_rd_r=3150e915-5aa1-45b1-afb3-27cc7be642e5&pd_rd_w=BjpUR&pd_rd_wg=uVD2q&pf_rd_p=30d9caac-9c74-4af5-a588-0cf9ff65dd47&pf_rd_r=CNZ8WKJVE9BPFG28Z0MP&psc=1&refRID=CNZ8WKJVE9BPFG28Z0MP'
urls.append(url)
#track(url, 10)

url = 'https://www.amazon.com.br/Eternauta-1969-H%C3%A9ctor-Germ%C3%A1n-Oesterheld/dp/8562848107/ref=pd_bxgy_14_img_3/130-5784877-1003836?_encoding=UTF8&pd_rd_i=8562848107&pd_rd_r=e7aad612-205a-4c32-ba92-95306566e986&pd_rd_w=wohfR&pd_rd_wg=tn0SU&pf_rd_p=30d9caac-9c74-4af5-a588-0cf9ff65dd47&pf_rd_r=VRA2EQ6WP1CNY40KV5PW&psc=1&refRID=VRA2EQ6WP1CNY40KV5PW'
urls.append(url)
#track(url, 11)

#n = 1
#workbook.close()
def search():
    #global n
    for url in urls: 
        track(url)
    #    n += 1
    else:
        print("Finalizado.")
        #workbook.close()

search()
#workbook.close()


#####################################################################
######################### Criação de rotina #########################
#print("Pesquisando preço...")     
#track() 

#def job(): 
#    print("Pesquisando novo preço...")
#    search()

#schedule.every(3).seconds.do(job) # Repete açao a cada 10 segundos 
#schedule.every(10).hours.do(job)   # Repete açao a cada 10 horas
#w = 1     
#while (w <= 10):
#    schedule.run_pending() 
#    time.sleep(1) 
#    w += 1
#else:
#    workbook.close()
#####################################################################
