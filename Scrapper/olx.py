import dbconnection as db 
from requests_html import HTMLSession
from bs4 import BeautifulSoup
s = HTMLSession()

#########urls do iphones##########################################
iphone6='https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-Iphone-6/?search%5Bfilter_float_price%3Ato%5D=50&search%5Bdescription%5D=1'

##########DB OPENING########################################################################################################################
conn = db.conn
cursor = conn.cursor()
