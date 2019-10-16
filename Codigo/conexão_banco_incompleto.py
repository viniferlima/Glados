import requests
import lxml.html
from datetime import date
import re
import schedule
import time
from amazon.api import AmazonAPI
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# Links para teste:
# url2 = 'https://www.amazon.com.br/gp/product/8562848107/ref=ox_sc_act_title_1?smid=A1ZZFT5FULY4LN&psc=1'
# url = 'https://www.amazon.com.br/Action-Figure-Sonic-Hedgehog-Boom/dp/B01AKT1Y50/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sonic&qid=1569325718&s=gateway&sr=8-1'
# url3 = 'https://www.amazon.com.br/Akira-5-Katsuhiro-Otomo/dp/8545712367/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=akira&qid=1569456784&sr=8-5'
    
url = input("Digite o link do produto: ")
res = requests.get(url, headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'})

site = (re.findall("amazon", url) or re.findall("submarino", url) or re.findall("saraiva", url))
dominio = site[0]
dominio = dominio.capitalize()

def maincode():


    while(res.status_code == 503):
        html = requests.get(url)

    #if res.status_code == 200:
    #    print("Conexao bem sucedida")

    doc = lxml.html.fromstring(res.content)

    corpo = doc.xpath('//*[@id="dp"]')[0]


    nome_produto = corpo.xpath('.//*[@id="productTitle"]/text()')
    separador = ""
    nome = separador.join(nome_produto)

    categoria = corpo.xpath('.//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[1]/span/a/text()')
    cat = separador.join(categoria)

    preco_produto = corpo.xpath('.//*[@id="soldByThirdParty"]/span/text()')
    preco_produto2 = corpo.xpath('.//*[@id="price_inside_buybox"]/text()')
    preco = separador.join(preco_produto)
    preco2 = separador.join(preco_produto2)

    fullprice = corpo.xpath('.//*[@id="buyBoxInner"]/ul/li[1]/span/span[2]/text()')
    semdesc = separador.join(fullprice)

    av = corpo.xpath('.//*[@id="availability"]/span/text()')
    disp = separador.join(av)

    # estudar como salvar o link da imagem do produto, abaixo temos o provável xpath da imagem
    # linkimg = corpo.xpath('.//*[@id="imgBlkFront"]/text()')  

    price = preco.strip() or preco2.strip()
    data_atual = date.today()
    

    if (semdesc > preco or semdesc > preco2):
        fup = semdesc.strip()
    else:
        fup = preco.strip() or preco2.strip()

    price = price.replace("R$", "").replace(",", ".")
    price = float(price)
    fup = fup.replace("R$", "").replace(",",".")
    fup = float(fup)
    porc_desc = 100 - int((price/fup)*100)

    insert("", nome.strip, cat.strip, fup, price, porc_desc, data_atual, dominio, disp.strip, "")

def insert(id, nome, categoria, preco, preco_desconto, porcentagem_desconto, data_consulta, site, disponivel, imagem):
    #conexão com o banco
    try:
        connection = mysql.connector.connect(host='localhost', database='glados', user='root', password='')

        if connection.is_connected():
            mySql_insert_Query = """INSERT INTO `produtos` (`id`, `nome`, `categoria`, `preco`, `preco_desconto`, `porcentagem_desconto`, `data_consulta`, `site`, `disponivel`, `imagem`) VALUES (NULL,'%s','%s','%s','%s','%s','%s','%s','%s' , NULL)"""#ultimo campo para imagem
            cursor = connection.cursor()
            result = cursor.execute(mySql_insert_Query)
            connection.commit()
        
        else:
            print("Erro ao conectar")

    except mysql.connector.Error as error:
        print("Failed to insert record into table {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

maincode()

#####################################################################
######################### Criação de rotina #########################
#print("Pesquisando preço...")     
#maincode() 

#def job(): 
    #print("Pesquisando novo preço...")     
    #maincode() 
   
# schedule.every(10).seconds.do(job) # Repete açao a cada 10 segundos 
# schedule.every(10).hours.do(job)   # Repete açao a cada 10 horas
  
#while True: 
    #schedule.run_pending() 
    #time.sleep(1) 
#####################################################################