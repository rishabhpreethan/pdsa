def dre(l):
    try:
        if l[0]%l[1]==0 and l[1]!=0:
            if l[0]/(l[1]**2 - l[2])==0:
                return True
        return False
    except ZeroDivisionError:
        print("zero")
    except:
        print("other error")
    else:
        print("No exception")
        
l=[4,2,8]
print("1",dre(l))
l=[4,2,4]
print("1",dre(l))
l=[8,4,16]
print("1",dre(l))
l=[48,6,36]
print("1",dre(l))
l=[44,6,36]
print("1",dre(l))