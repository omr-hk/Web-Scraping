import requests
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing import cpu_count, Pool, Manager
import time
class Scraper_final:
    def __init__(self, startingPage, endingPage):
        self.base_url = "https://attestazione.net"
        self.df = pd.DataFrame()
        self.dict_list = []
        self.startingPage = startingPage
        self.endingPage = endingPage
        self.shared_list = Manager().list()
    def getCSV(self):
        start_t = time.time()
        s = requests.Session()
        for i in range(self.startingPage,self.endingPage+1):
            url = "https://attestazione.net/SoaEngine?Page={}".format(i)
            r = s.get(url)
            soup = BeautifulSoup(r.content,'html5lib')
            links = soup.find_all('a',{'class' : 'text-info'})
            for link in links:
                cr = s.get(self.base_url+link['href'])
                csoup = BeautifulSoup(cr.content,'html5lib')
                dt=csoup.find_all('dt')
                dd=csoup.find_all('dd')
                dictionary={}
                for(k,v) in zip(dt,dd):
                    dictionary[k.text.strip()] = v.text.strip()
                self.dict_list.append(dictionary)
        end_t = time.time()
        self.df = pd.DataFrame.from_dict(self.dict_list)
        self.df.to_csv('output.csv')
        print('Execution time = %.6f seconds' % (end_t-start_t))
    
    def mpFetch(self, i):
        url = "https://attestazione.net/SoaEngine?Page={}".format(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html5lib')
        links = soup.find_all('a',{'class' : 'text-info'})
        for link in links:
            cr = requests.get(self.base_url+link['href'])
            csoup = BeautifulSoup(cr.content,'html5lib')
            dt = csoup.find_all('dt')
            dd = csoup.find_all('dd')
            dictionary={}
            for(k,v) in zip(dt,dd):
                dictionary[k.text.strip()] = v.text.strip()
            self.shared_list.append(dictionary)

    def mpCSV(self):
        self.df = pd.DataFrame.from_dict(list(self.shared_list))
        self.df.to_csv('output.csv')

if __name__ == '__main__':
    startingPage = int(input("Enter starting page number: "))
    endingPage = int(input("Enter ending page number: "))
    fin = Scraper_final(startingPage=startingPage, endingPage=endingPage)
    choice = input("Enter 1 if device is multiprocessing compatible (This will lead to faster web-scraping and performance): ")
    if choice == "1":
        print("multiprocessing enabled")
        start_t = time.time()
        links = []
        with Pool(cpu_count()) as p:
            p.map(fin.mpFetch,range(fin.startingPage,fin.endingPage+1))
        fin.mpCSV()
        end_t = time.time()
        print('Execution time = %.6f seconds' % (end_t-start_t))
    else:
        fin.getCSV()