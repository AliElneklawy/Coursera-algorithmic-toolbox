#==================================================================
#                        dictionaries 
#==================================================================
# dictionaries are created with curly braces {}
# They contain key:value pairs
# The keys are separated by commas
# The values are separated by colons
# example:
# {"Name" : Ali, "Age": 22, "Country": "Egypt"}
# The keys can be any type of data
# The values can be any type of data
# Keys are unique and cannot be duplicated
# If a key is duplicated, the last value will be used
#==================================================================

user = {"Name": "ali",
        "age": 22,
        "countrry": "Egypt",
        1: "one", 
        2: "two",
        (1, 2, 3): "tuple",
        "skills": ["Python", "C"],
        "Name": "ahmed"   # This will override the last value of "name"
}
print(user)

#  to get the value of a key: 
print(user["Name"])  # "ahmed" because it overrides the first value of "name"
print(user.get("Name"))

# You can get all the keys or all the values of the dictionary as follows:
print(user.keys())
print(user.values())

#   =    Nested dictionaries     =    #

langs = {
    "one": {
        "arabic": "native",
        "progress": 90
    },
    "two": {
        "english": "B2",
        "progress": 80
    },
    "three": {
        "german": "A1",
        "progress": 20
    }
}
print(langs)
print(langs["one"])
print(langs["one"]["progress"])
print(langs.keys())
print(langs.values())


#==================================================================
#                        dictionary methods
#==================================================================
# 1- clear(): Clears the dictionary
# 2- update(): updates the dictionary with the given value. Takes only one arguement
# 3- copy(): takes a shallow copy of a dictionary
# 4- setdefault(): if the given key is already in the list, nothing happens. If not, the given key along with its value will be added to the dictionary 
# 5- popitem(): returns the last added element
# 6- fromkeys(): creates a dictionary from a given variable
# 7- get(): returns the value of the given key
#==================================================================

mydict = {
    "name": "ali", 
    "age": 22,
    "hobbys": ["football", "programming"],
    "languages": {
        "one": {
            "german": "c1"
        }, 
        "two": {
            "english": "c1"
        }
    }
}
print(mydict)

# 1- clear(): Clears the dictionary
#mydict.clear()
#print(mydict)  will print an empty dictionary {}


# 2- update(): updates the dictionary with the given value. Takes only one arguement
mydict.update({"country": "egypt"})  #will be added to the end of the dictionary
print(mydict)


# 3- copy(): takes a shallow copy of a dictionary
mydict2 = mydict.copy()
print(mydict2)


# 4- setdefault(): if the given key is already in the list, nothing happens. If not, the given key along with its value will be added to the dictionary
mydict2.setdefault("name", "ahmed")  # the key "name" is already in the list so nothing happens
print(mydict2)
mydict2.setdefault("food", "fish")   # the key "food" is not in the list, so it will be added at the end
print(mydict2)


# 5- popitem(): returns the last added element
print(mydict.popitem())  # will add the key "country" not "food" 


# 6- fromkeys(): creates a dictionary from a given variable
a = ("key1", "key2", "key3")
[d, b, c] = 3, 4, 5
print(dict.fromkeys(a, c))
print(dict.fromkeys(a, [d,b, c]))


# 7- get(): returns the value of the given key
print(mydict.get("languages"))

