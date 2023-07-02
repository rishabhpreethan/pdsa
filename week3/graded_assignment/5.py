def partition(a,l,h):
    i=l+1
    j=h
    pivot=a[l]
    while i<=j:
        while a[i]<pivot and i<h:
            i+=1
        while a[j]>pivot:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
        else:
            i+=1
    a[l]=a[j]
    a[j]=pivot
    print(a)
    return j

print(partition([13, 18, 8, 10, 21, 7, 2, 32, 6, 19], 0, 9))