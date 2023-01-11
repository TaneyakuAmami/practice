import urllib.request

url = 'https://www.google.com/?hl=ja'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
 print(response.geturl())
 print(response.getcode())
 print(response.info()['Content-Type'])
 print(response)

 file = open('output\httpresponse.txt', 'w')
 file.write(response.geturl())
 file.write('\n')
 file.write(str(response.getcode()))
 file.write('\n')
 file.write(response.info()['Content-Type'])
 file.write('\n')
 file.write(str(response))

 file.close()
