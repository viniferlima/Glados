import requests
import lxml.html
import re

# Programa simples, feito apenas para estudar as sintaxes e o tratamento do site
# Principal problema nessa versão: se o link (submarino/saraiva) possuir
# o nome "amazon", o retornado será que o site é da amazon
# O problema pode ser corrigido comparando somente o inicio da string txt
# Será utilizado no webbot para detectar o site e assim coletar os dados do 
# produto. Deve ser otimizado e reduzido.

#links
txt = "https://www.submarino.com.br/produto/202857141?pfm_carac=amazon&pfm_index=9&pfm_page=search&pfm_pos=grid&pfm_type=search_page%20&sellerId"
#txt = "https://www.submarino.com.br/produto/132627403?chave=prf_hm_odh_0_1_black-night-24set-132627403"
#txt = "https://www.amazon.com.br/gp/product/8562848107/ref=ox_sc_act_title_1?smid=A1ZZFT5FULY4LN&psc=1"
x = re.search("amazon", txt)
y = re.search("submarino", txt)
z = re.search("saraiva", txt)

if (x):
    print("Site: Amazon!")
elif(y):
    print("Site: Submarino!")
elif(z):
    print("Site: Saraiva!")
else:
    print("Site não encontrado! Tente com: Amazon, Submarino e Saraiva")
