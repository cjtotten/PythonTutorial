#Python dictionaries
thisdict =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])

thisdict =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.get("brand"))

thisdict['year'] = 1965
print(thisdict)

# print all keys in a dictionary
for x in thisdict:
  print(x)
  
# print all values in a dictionary
for x in thisdict:
    print(thisdict[x])

# add an item to the dictionary
thisdict["color"] = "red"
print(thisdict)

thisdict.popitem()
print(thisdict)
