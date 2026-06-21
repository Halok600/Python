#Dictonary : Key-Value pairs, Unordered, Mutable

mydict = {"name":"Max","age":28,"City":"New York"}
print(mydict)

mydict2 = dict(name = "Mary", age = 28, city = "Boston")
print(mydict2)

value = mydict["name"]

mydict["email"] = "max@123.com"
mydict["email"] = "coolmax@123.com"
print(value)
print(mydict)


del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict2:
    print(mydict2["name"])


try:
    print(mydict["name"])
except:
    print("error")


for key in mydict2: # or mydict2.keys()
    print(key)

for value in mydict2.values():
    print(value)

for key, value in mydict2.items():
    print(key,value)

# editing

mydict_cpy = mydict
print(mydict_cpy)
mydict_cpy["age"] = 26 #modifies the og one too
print(mydict_cpy) 
print(mydict)

mydict_cpy2 = mydict.copy() # or mydict_cpy = dict(mydict)

print(mydict_cpy2)
mydict_cpy2["name"] = "Max"

print(mydict_cpy2)
print(mydict)


#Merge method


dict1 = {"name": "Max","age":28,"email":"max@xyz.com"}
dict2 = {"name":"Maey","age":27,"city":"Boston"}

dict1.update(dict2)
print(dict1)

#KEY TYPES

dict_og = {3: 9, 6: 36, 9: 81}
print(dict_og)
value = dict_og[3]
print(value)

mytuple = (8, 7) #tuple can be used as key but not list as tuple is immutable
dictnew = {mytuple:15}
print(dictnew)