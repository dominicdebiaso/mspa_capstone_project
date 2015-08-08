#import urllib2
from bs4 import BeautifulSoup
import requests

def GetGoogleSearchResult(keyword):
#     proxy = urllib2.ProxyHandler({'http':'41.188.49.163:3128'})
#     opener = urllib2.build_opener(proxy)
# 
#     opener = urllib2.build_opener()
#     opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# 
#     urllib2.install_opener(opener)
    
    resText = []    
        
    for start in range(0,1):
        try:
            keyword = keyword.encode('utf-8')
        except:
            keyword = str(keyword)

        url = "http://www.google.com/search?q={0}&start=".format(keyword.replace(' ','+')) + str(start*5)
#        page = opener.open(url)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3',
        }

        
        page = requests.get(url, headers=headers)
#        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.text)
        
        #page = urllib2.urlopen(url)
        #soup = BeautifulSoup(page.read())
        
        
        if 'systems have detected' in page.text:
            print 'Error: Please be behind a proxy server'
            return 0
    
        for txt in soup.findAll('span', class_ = 'st'):
            resText.append(txt.text.encode('utf-8'))
            
    wordList = {}

    wordList [ 'beer'] =0
    wordList['wine'] =0
    wordList['alcohol'] =0
        
    i = 0
    while i < len(resText):
        for word in wordList.keys():
                
            if word in resText[i].lower():
                wordList[word] = wordList[word] + 1
                
        i = i+1
            
    return wordList

#print GetGoogleSearchResult('beer')