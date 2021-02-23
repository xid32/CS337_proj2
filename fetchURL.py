import urllib.request

try:
   with urllib.request.urlopen('https://www.allrecipes.com/recipe/82768/lauras-quick-slow-cooker-turkey-chili/') as f:
      # print(f.read().decode('utf-8'))
      saveFile = open("url.txt", "w")
      content = f.read().decode("utf-8") 
      saveFile.write(content)
      saveFile.close()


except urllib.error.URLError as e:
   print(e.reason)


