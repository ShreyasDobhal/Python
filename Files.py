text="Hello World\nPython File Handling"
saveFile = open("test.txt",'w')
saveFile.write(text)
saveFile.close()

text="\nNew data"
appendFile = open("test.txt",'a')
appendFile.write(text)
appendFile.close()

readFile = open("test.txt",'r')
text=readFile.read()
readFile.close()
print(text)
textdata=open("test.txt",'r').readlines()
print(textdata)
for str in textdata:
    print(str)
