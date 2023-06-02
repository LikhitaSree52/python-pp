fruits = {"apple", "banana", "cherry"}
#add
fruits.add("orange")
print(fruits) 

#copy 
x = fruits.copy()
print(x)

#difference
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

#difference_update
x.difference_update(y)
print(x)

#discard 
fruits.discard("banana")
print(fruits)

#disjoint
z = x.isdisjoint(y)
print(z)

#intersection
z = x.intersection(y)
print(z)

#remove
fruits.remove("banana")
print(fruits)

#union
z = x.union(y)
print(z)

#pop
fruits.pop()
print(fruits)

#clear method
fruits.clear()
print(fruits)


