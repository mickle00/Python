import zipfile

map2 = {}
zf = zipfile.ZipFile('/home/mikey/Dropbox/Python/Mike/channel.zip', 'r')
for info in zf.infolist():
    fn = info.filename
    cm = info.comment
    map2[fn] = cm

#for key in map2:
    #print(key)
    #print(key)
    #print(map2[key])
#print(map2)
    
start = ('/home/mikey/Dropbox/Python/Mike/channel/')

one = open(start + '90052' +'.txt', 'r')
first = '90052'
next = '90052'
comments =""

for i in range(908):
    o = open(start + next +'.txt', 'r')
    
    for line in o:
        second = line.split('is ')
        next = second[1]
        file2 = str(next)+'.txt'
        out = map2[file2].decode('utf-8')
        comments = comments + out

print(comments)

#print(next)
#print(comments)
#print(len(comments))


#list = zf.namelist()
#print(list)

#p = zipfile.comments
#print(p)

#z = zipfile.ZipFileZipFile('/home/mikey/Dropbox/Python/Alex/challenge6/channel.zip', 'r')

#output = zipfile.open(file)
#output2 = output.comments
#print(output2)
