import urllib.request
import base64

start = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=92512"
base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

#response = urllib.request.urlopen(start)
#html = response.read()

id = "str(int(92118/2))"
for i in range(400):
    url = base + id
    response = urllib.request.urlopen(base+id)
    html = response.read()
    length = (len(html) - 5)
    #print (length)
    id = str(int(html[length:]))
    #if len(id) == 5:
        #id = id
    if len(id) == 4:
        id = "0"+id
    if len(id) == 3:
        id = "00" + id
    if len(id) == 2:
        id = "000" + id
    if len(id) == 1:
        id = "0000" + id
    if len(id) >5:
        print("Godamnit Mike you fucking suck")
        
    #print (html)
    #print (id)
    print (url)

#id = int(html[l-5:])

#print(id)
  

#print(html)


