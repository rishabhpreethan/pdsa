def DishPrepareOrder(order_list):
    d={}
    for i in order_list:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    s = sorted(d.keys(), key=lambda x: (-d[x], x))
    return s
nums = eval(input())
print(DishPrepareOrder(nums))