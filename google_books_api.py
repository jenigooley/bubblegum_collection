import requests
import pprint

#title = raw_input('isbn: ')
key = 'AIzaSyAV40ssf0WZMSo26nFLSPER1YGoygdC9U0'
payload = {'q':'isbn: 9781445506074', 'maxResults':'1', 'printType':'books', 'orderBy':'relevance', 'projection':'lite', 'key':key}
r = requests.get('https://www.googleapis.com/books/v1/volumes', params = payload)
#print(r.json())
#print(r.text)
r = r.json()
results = {}

results = r['items'][0]['volumeInfo']
keys = ['title', 'authors', 'publisher', 
	'publishedDate','description','imageLinks']
r_res = [results[x]for x in keys]
for i in r_res:
    print (i)
