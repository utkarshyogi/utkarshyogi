def duplicate_elements(li):
    dict_of_elements = {}
    
    for i in range(len(li)):
        if dict_of_elements.get(li[i]) is None:
            dict_of_elements.update({li[i]:0})
        else:
            dict_of_elements[li[i]] += 1
    return dict_of_elements

list = [1,2,3,4,5,5,5,6,6,6,6,7,8,9]        
# print(duplicate_elements(list))
result = duplicate_elements(list)
for k,v in result.items():
    if v > 0:
        print (k)


