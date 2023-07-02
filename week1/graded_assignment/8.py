def sim(l):
    try:
        while len(l)>0:
            if l.pop(0) != l.pop(-1):
                return False
        return True
    
    except IndexError:
        print("index")
    except:
        print("other error")
    else:
        print("No exception")
        

# l=[1,2,3,4,3,2,1]
l=[2, 2, 2, 2, 2, 2]
sim(l)