'''
Module Name : Inverted Index
Functionality:  Read the list of files from the web crawler
               Removes the stopwords from the input file
               Creates a inverted index
               Allow the user to search and return the search result
I/P : List of files created by web crawling
 
'''
from nltk.corpus import stopwords
 
def invertedindex():
   '''
   Takes the list of file, loop through all the files, parse the files and removes the stop keywords
   Call add to Index module
   '''
   index = {}
   file_crawled = open("listoffilenames.txt", "r")
   for line in file_crawled.readlines():
       # print(line)
       line = line.replace('\n', '')
       link = line
       f_file = open(line, "r")
       content = f_file.read().lower()
       content=content.replace('\n','_')
       # print(content)
       words = content.split('_')
       # print(words)
       stopwords.words('english')
       for word in words:
 
           add_to_index(index, word, link)
 
   return index
 
def add_to_index(index, keyword, link):
   '''
   Add the index to the corresponding file it is found in
   '''
   if keyword in index:
       if link not in index[keyword]:
           index[keyword].append(link)
   else:
       index[keyword] = [link]
 
def lookup(index, keyword):
   '''
   lookup the index list, return the keyword if already exist
   '''
   if keyword in index:
       return index[keyword]
   else:
       return None
 
def searchfile(text):
   '''
   Prompt the user to input
   Search for the inverted index and return the corresponding key value
   '''
   if text in index:
       finalresults= (index[text])
       print("The searched keywords is found at :", end=" ")
       if len(finalresults)!=0:
           for finalresult in finalresults:
               print(finalresult[6:-4] + " mail box ")
 
   else:
       print("The searched keyword is not found")
 
index= invertedindex()
print("-----------------------Inverted Index-----------------------")
print(index)
 
text = input("Enter the text you want to search :")
searchfile(text.lower())
 
# end of file
