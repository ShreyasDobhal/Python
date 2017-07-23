a,b,c=(10,5,25)

if a>b:
    if a>c:
        print("a = "+str(a)+" is largest")
    else:
        print("c = "+str(c)+" is largest")
else:
    if b>c:
        print("b = " + str(b) + " is largest")
    else:
        print("c = " + str(c) + " is largest")

if b<a>c:
    print("a = " + str(a) + " is largest")
elif a<b>c:
    print("b = " + str(b) + " is largest")
else:
    print("c = " + str(c) + " is largest")