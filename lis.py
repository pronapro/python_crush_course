name_li = ["one","two","three","four"]
#len
len(name_li)
#changing to list you use list()
name ="hello world"
list(name)
#adding items
name_li.append("twenty")
print(name_li)
#index of an items
ind =name_li.index("three")
print(ind)
""" other functions include Pop,remove,extend,sort,reverse"""

#list comprehension
for i in range(1,10):
    print(i**2)
#can be written as
print("for list comprehension")
[print(i**2) for i in range(1,10)]
#lists can be nexted to great matrix
mat = [[1,2,3],[4,5,6],[7,9,10]]
