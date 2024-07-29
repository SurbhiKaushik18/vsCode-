myDict = {
    "Surbhi":"You have to do a hard work.",
    "Silki":"My lovely Sister."
}
print(myDict.keys())
print(type(myDict.keys()))
print(myDict.values())
print(myDict.items())
print(myDict)
updateDict = {
   "Vishal":"My Brother",
   "Surbhi":"Good girl"
}
myDict.update(updateDict)
print(myDict)
print(myDict.get("Surbhi2")) #It returns none value as Surbhi2 is not present.
#print(myDict("Surbhi2"))
