import dbconnection as db 
import requests 
import pandas as pd
from requests_html import HTMLSession
from bs4 import BeautifulSoup
s = HTMLSession()
conta = 0

def trueurl(url):
    return url

def nPages(url):
    global conta
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')
    conta = str(soup.find(attrs={"data-cy" : "page-link-last"}).text.strip())
    return conta


def searchBaseModel(url,modelo,ranger):
    iphonelinks=[]
    iphonelist=[]
    for x in range (1,ranger+1):
        r = requests.get(url +'&page'+str(x))
        soup = BeautifulSoup(r.content,'lxml')
        iphones = soup.find_all('h3',class_='lheight22 margintop5')

        for item in iphones:
            for link in item.find_all('a',href=True):
                if(link=='https://www.google.com/aclk?sa=l&ai=DChcSEwiFvuS86evsAhXElNUKHfjOAqEYABABGgJ3cw&num=1&sig=AOD64_0g198xSGCPCyHteY2acuVNcNfHgA&adurl=&q=&nb=18&rurl=https%3A%2F%2Fwww.olx.pt%2F&nm=32'
                or link=='/aclk?sa=l&ai=DChcSEwiai6KO7OvsAhUEstUKHRNECL8YABAAGgJ3cw&num=1&sig=AOD64_0JWdg4eP95dPRwpzunhXzZ-P8lWw&adurl=&q='):
                        print('')
                else : 
                    iphonelinks.append(link['href']) 
    
    for link in iphonelinks:
        r = requests.get(link)
        soup = BeautifulSoup(r.content,'lxml')
        

        if (str('Iphone '+modelo) in soup.find('h1').text.strip() and 'Capas' not in soup.find('h1').text.strip()
        and 'capas' not in soup.find('h1').text.strip() and 'Ecrã' not in soup.find('h1').text.strip()
        and 'Display' not in soup.find('h1').text.strip() and 'Auriculares' not in soup.find('h1').text.strip()
        and 'auriculares' not in soup.find('h1').text.strip() and 'bateria' not in soup.find('h1').text.strip() and 
        'Bateria' not in soup.find('h1').text.strip() and str(modelo+'s') not in soup.find('h1').text.strip() 
        and str(modelo+'S') not in soup.find('h1').text.strip() and str(modelo+' s') not in soup.find('h1').text.strip() 
        and str(modelo+' S') not in soup.find('h1').text.strip() and 'Capa' not in soup.find('h1').text.strip()
        and 'capa' not in soup.find('h1').text.strip()):
            #Separacao dos Negociaveis dos Nao Negociaveis pois as paginas sao montadas de maneiras diferentes
            if(soup.find('small', class_='pricelabel__label')!=None):
                nome = soup.find('h1').text.strip()  
                preco = soup.find('strong', class_='pricelabel__value arranged').text.strip()
                descricao = soup.find('div', class_='clr lheight20 large').text.strip()
                iphoner = {
                    'Link':link,
                    'Nome': nome,
                    'Modelo':modelo,
                    'Negociavel?':'Negociavel',
                    'Preco':preco,
                    'Descricao':descricao
                    } 
                iphonelist.append(iphoner)
                print('Saving:', iphoner['Nome'])
                
            else:
                nome = soup.find('h1').text.strip()
                preco = soup.find('strong', class_='pricelabel__value not-arranged').text.strip()
                descricao = soup.find('div', class_='clr lheight20 large').text.strip()
                iphoner = {
                        'Link':link,
                        'Nome': nome,
                        'Modelo':modelo,
                        'Negociavel?':'Negociavel',
                        'Preco':preco,
                        'Descricao':descricao
                        } 
                iphonelist.append(iphoner)
                print('Saving:', iphoner['Nome'])
                
def searchSModel(url,modelo,ranger):
    iphonelinks=[]
    iphonelist=[]
    for x in range (1,ranger+1):
        r = requests.get(url +'&page'+str(x))
        soup = BeautifulSoup(r.content,'lxml')
        iphones = soup.find_all('h3',class_='lheight22 margintop5')

        for item in iphones:
            for link in item.find_all('a',href=True):
                if(link=='https://www.google.com/aclk?sa=l&ai=DChcSEwiFvuS86evsAhXElNUKHfjOAqEYABABGgJ3cw&num=1&sig=AOD64_0g198xSGCPCyHteY2acuVNcNfHgA&adurl=&q=&nb=18&rurl=https%3A%2F%2Fwww.olx.pt%2F&nm=32'
                or link=='/aclk?sa=l&ai=DChcSEwiai6KO7OvsAhUEstUKHRNECL8YABAAGgJ3cw&num=1&sig=AOD64_0JWdg4eP95dPRwpzunhXzZ-P8lWw&adurl=&q='):
                        print('')
                else : 
                    iphonelinks.append(link['href']) 
    
    for link in iphonelinks:
        r = requests.get(link)
        soup = BeautifulSoup(r.content,'lxml')
        modelo1=str(modelo+'s')
        modelo2=str(modelo+'S')
        modelo3=str(modelo+' s')
        modelo4=str(modelo+' S')
        print (str('Iphone '+modelo1))
        if (str('Iphone '+modelo1) in soup.find('h1').text.strip() or str('Iphone '+modelo2) in soup.find('h1').text.strip()
        or str('Iphone '+modelo3) in soup.find('h1').text.strip() or str('Iphone '+modelo4) in soup.find('h1').text.strip()
        and 'Capa' not in soup.find('h1').text.strip()
        and 'capa' not in soup.find('h1').text.strip() and 'Ecrã' not in soup.find('h1').text.strip()
        and 'Display' not in soup.find('h1').text.strip() and 'Auriculares' not in soup.find('h1').text.strip()
        and 'auriculares' not in soup.find('h1').text.strip() and 'bateria' not in soup.find('h1').text.strip() and 
        'Bateria' not in soup.find('h1').text.strip() and 'Capas' not in soup.find('h1').text.strip()
        and 'capas' not in soup.find('h1').text.strip()):
            #Separacao dos Negociaveis dos Nao Negociaveis pois as paginas sao montadas de maneiras diferentes
            if(soup.find('small', class_='pricelabel__label')!=None):
                nome = soup.find('h1').text.strip()  
                preco = soup.find('strong', class_='pricelabel__value arranged').text.strip()
                descricao = soup.find('div', class_='clr lheight20 large').text.strip()
                iphoner = {
                    'Link':link,
                    'Nome': nome,
                    'Modelo':modelo,
                    'Negociavel?':'Negociavel',
                    'Preco':preco,
                    'Descricao':descricao
                    } 
                iphonelist.append(iphoner)
                print('Saving:', iphoner['Nome'])
                
            else:
                nome = soup.find('h1').text.strip()
                preco = soup.find('strong', class_='pricelabel__value not-arranged').text.strip()
                descricao = soup.find('div', class_='clr lheight20 large').text.strip()
                iphoner = {
                        'Link':link,
                        'Nome': nome,
                        'Modelo':modelo,
                        'Negociavel?':'Negociavel',
                        'Preco':preco,
                        'Descricao':descricao
                        } 
                iphonelist.append(iphoner)
                print('Saving:', iphoner['Nome'])





