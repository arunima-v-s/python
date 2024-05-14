# to create a list
a=["a","b","c","d","e"]
print(len(a))
print(a[0])
print(a[-1])
# to change data in specific index value
a[0]="A"
print(a)

#to add datas in a list by using append functn
a.append("hi")
print(a)

# to add datas in a specific position of list by using insert fnctn
a.insert(1,"a")
print(a)

# to add charecters of string in a list by using extend fnctn
a.extend("hello")
print(a)

# to remove data from list by using remove functn
a.remove("e")
print(a)
b=[1,2,3,4]
#/a.append(b)
print(a)

# to find specific datas by its position
print(a[2:4])
print(a[ :4])
print(a[3: ])
print(a[ : ])
print(a[2:4]+a[4:6])

# list is a mutable function- it can add, remove, and extend datas