def odd_one(lst):
    first_datatype = type(lst[0])
    for element in lst[1:]:
        if type(element) != first_datatype:
            return str(type(element))[8:-2]
    return None 
        
    
print(odd_one([2,13,16,4.5]))