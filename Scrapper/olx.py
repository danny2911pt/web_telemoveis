import olxscrapper

########urls#########################################
Iphone4url = 'https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-iphone-4/?search%5Bfilter_float_price%3Ato%5D=30&search%5Bdescription%5D=1'
Iphone4surl = 'https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-iphone-4s/?search%5Bfilter_float_price%3Ato%5D=30&search%5Bdescription%5D=1'
Iphone5url = 'https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-iphone-5/?search%5Bfilter_float_price%3Ato%5D=30&search%5Bdescription%5D=1'
Iphone5surl = 'https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-iphone-5s/?search%5Bfilter_float_price%3Ato%5D=40&search%5Bdescription%5D=1'
Iphone6url = 'https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-iphone-6/?search%5Bfilter_float_price%3Ato%5D=50&search%5Bdescription%5D=1'
Iphone6Plusurl = 'https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-iphone-6-plus/?search%5Bfilter_float_price%3Ato%5D=70&search%5Bdescription%5D=1'
Iphone6Surl = 'https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-iphone-6s/?search%5Bfilter_float_price%3Ato%5D=50&search%5Bdescription%5D=1'
Iphone6SPlusurl = 'https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-iphone-6s-plus/?search%5Bfilter_float_price%3Ato%5D=70&search%5Bdescription%5D=1'
Iphone7url = 'https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-Iphone-7/?search%5Bfilter_float_price%3Ato%5D=70&search%5Bdescription%5D=1'
Iphone7Plusurl = 'https://www.olx.pt/telemoveis-e-tablets/telemoveis/q-iphone-7-plus/?search%5Bfilter_float_price%3Ato%5D=90&search%5Bdescription%5D=1'
Iphone8url = 'q-iphone-8/?'
Iphone8Plusurl = 'q-iphone-8-plus/?'
IphoneXurl = 'q-iphone-x/?'
IphoneXMaxurl = 'q-iphone-x-max/?'
IphoneXsurl = 'q-iphone-xs/?'
IphoneXsMaxurl = 'q-iphone-xs-max/?'
Iphone11url = 'q-iphone-11/?'
Iphone11Prourl ='q-iphone-11-pro/?'


#########modelos####################################################
Iphone4 = '4'
Iphone4s = '4s'
Iphone5 = '5'
Iphone5s = '5s'
Iphone6 = '6'
Iphone6Plus = '6 Plus'
Iphone6S = '6s'
Iphone6SPlus = '6s Plus'
Iphone7 = '7'
Iphone7Plus = '7 Plus'
Iphone8 = 'Iphone 8'
Iphone8Plus = '8 Plus'
IphoneX = 'X'
IphoneXMax = 'X Max'
IphoneXs = 'XS'
IphoneXsMax = 'XS Max'
Iphone11 = '11'
Iphone11Pro ='11 Pro'

def iphone6():
    conta = 0
    iphone = Iphone6
    url = olxscrapper.trueurl(Iphone6url)
    conta +=int(olxscrapper.nPages(url))
    olxscrapper.searchBaseModel(url,iphone,conta)

def iphone6Plus():
    conta = 0
    iphone = Iphone6Plus
    url = olxscrapper.trueurl(Iphone6Plusurl)
    conta +=int(olxscrapper.nPages(url))
    olxscrapper.searchBaseModel(url,iphone,conta)


def iphone6s():
    conta = 0
    iphone = Iphone6
    url = olxscrapper.trueurl(Iphone6Surl)
    conta +=int(olxscrapper.nPages(url))
    olxscrapper.searchBaseModel(url,iphone,conta)

def iphone6sPlus():
    conta = 0
    iphone = Iphone6Plus
    url = olxscrapper.trueurl(Iphone6SPlusurl)
    conta +=int(olxscrapper.nPages(url))
    olxscrapper.searchBaseModel(url,iphone,conta)

def iphone7():
    conta = 0
    iphone = Iphone7
    url = olxscrapper.trueurl(Iphone7url)
    conta +=int(olxscrapper.nPages(url))
    olxscrapper.searchBaseModel(url,iphone,conta)

def iphone7Plus():
    conta = 0
    iphone = Iphone7Plus
    url = olxscrapper.trueurl(Iphone7Plusurl)
    conta +=int(olxscrapper.nPages(url))
    olxscrapper.searchBaseModel(url,iphone,conta)

