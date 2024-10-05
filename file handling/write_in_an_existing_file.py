f = open(r"c:\Users\pc1\Desktop\New Text Document.txt","a")
f.write("now the file has more content")
f.close()

f= open (r"c:\Users\pc1\Desktop\New Text Document.txt","r")
print(f.read())