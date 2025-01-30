collection = {1, 2, 3,3, 4, 5,"hello ","world"}
print(collection)
print(type(collection))
print(len(collection))

collection  = {} # empty dictionary
print(type(collection))

collection= set() # empty set
print(type(collection))


#add
collection.add(1)
collection.add(2)
collection.add(2)

print(collection)

#remove

collection.remove(1)
print(collection)


#union

collection1 = {1,2,3,4,5}
collection2 = {4,5,6,7,8}
print(collection1.union(collection2))
print(collection1 )
print(collection2)
print(collection1.intersection(collection2))
  
  
  
#practice 1


collection={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figures"],
}  
print(collection)

#practice 2

marks={}

x=int(input("enter physics marks::"))
marks.update({"physics":x})

x=int(input("enter chemistry marks::"))
marks.update({"chemistry":x})

x=int(input("enter maths marks::"))
marks.update({"maths":x})

print(marks)


#practice 3


values={9,9.0,0.9,8}
print(values)