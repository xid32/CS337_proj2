import urllib.request

def fetchURL(url):
   try:
      with urllib.request.urlopen(url) as f:
         # print(f.read().decode('utf-8'))
         saveFile = open("url.txt", "w")
         content = f.read().decode("utf-8") 
         saveFile.write(content)
         saveFile.close()


   except urllib.error.URLError as e:
      print(e.reason)


