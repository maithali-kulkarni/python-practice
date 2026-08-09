dict1 = {'a':1, "b":3}
dict2 = {"c":5,"d":6}

for key,value in dict1.items():
    if not(key in dict2.keys()):
        dict2[key] = value

print(dict2)