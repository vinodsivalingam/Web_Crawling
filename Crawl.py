import requests
from bs4 import BeautifulSoup
import json
 
def trade_spider():
   '''
   loops through the Enron website, crawls over the sub folders
 
   '''
   url='http://www.enron-mail.com/email/'
   source_code=requests.get(url, allow_redirects=False)
   plain_text = source_code.text.encode('ascii', 'replace')
   soup = BeautifulSoup(plain_text, 'html.parser')
   listoffile = ""
 
   finaldictionary={}
   for link in soup.findAll('a'):
           href = link.get('href')
           title = link.string
 
#Limited crwaling : Restricted by matching the first charcter of the names
           # letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
           letters = "abcABC"
           if href[0] in letters:
               personname=href
               # print( "Person Name:" +href)
               sublink= "http://www.enron-mail.com/email/"+href
               # print(sublink)
 
               # crawls over the cubfolder
               url='http://www.enron-mail.com/email/'+href
               source_code = requests.get(url, allow_redirects=False)
               plain_text = source_code.text.encode('ascii', 'replace')
               soup = BeautifulSoup(plain_text, 'html.parser')
               intermediatedictionary=''
               for link in soup.findAll('a'):
                   href = link.get('href')
                   title = link.string
                   if href[0] in letters:
 
                       # print("Title :" + title )
                       url = sublink + href
                       source_code = requests.get(url, allow_redirects=False)
                       plain_text = source_code.text.encode('ascii', 'replace')
                       soup = BeautifulSoup(plain_text, 'html.parser')
 
                       finaltext=''
                       for link in soup.findAll('a'):
                           href = link.get('href')
                           title = link.string
                           if href[0] in letters :
                               # print(title)
 
                               finaltext= finaltext + title + "\n"
 
                               print(finaltext)
                               # finaltext.append(title)
                       intermediatedictionary += finaltext
               finaldictionary[personname] = intermediatedictionary
 
# Creates the list of files for all the crawled use
               filename = "Files/" + personname[:-1] + '.txt'
               listoffile = listoffile + filename + "\n"
               print(filename)
               f= open(filename, 'a')
               f.write(intermediatedictionary)
               f.close()
 
# collecting all the files created in to a single file
   f=open('listoffilenames.txt','w')
   f.write(listoffile)
   print("List of Files created :"+'\n' + listoffile)
trade_spider()
 
# end of file
