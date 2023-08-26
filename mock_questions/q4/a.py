def peak_unimodal(a):
    l=0
    r=len(a)-1
    
    while l < r:
        mid = l + (r - l) // 2
        if a[mid] < a[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l