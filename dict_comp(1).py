dict1 = {'Washington':3000,'St.Louis':7000,'Azzuri':10000}

dict2= {k:v for k,v in dict1.items() if v >4000}

print(dict2)
