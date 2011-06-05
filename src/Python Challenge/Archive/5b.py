import pickle
f = open('banner.p', 'rb')
unpickled = pickle.load(f)

pieces2 = []
for pieces in unpickled:
    #pieces.append(piece)
    #print(pieces)
    #print ("\n")
    pieces2.append(pieces)
    for p in pieces2:
        print(p)
        #x,y = p
        #print(x)
        #print(y)
    #for y in pieces:
    #    print(x)

#for piece in pieces:

 #   for y in piece:
  #      print (x)

