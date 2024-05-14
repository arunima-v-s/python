# to print a string
a="good morning"
print(a)
# to find the lenth of string using len function
print(len(a))
#to find specific charecters of string
print(a[6:1])


# to remove unwanted spaces before and after a string by using strip functn
b="     hi    "
print(b)
print(b.strip())

# to find lower of a string by using lower functn
c="WHITE"
print(c)
print(c.lower())

# to find upper of a string by using upper functn
d="black"
print(d)
print(d.upper())

# to use replace function-to replace a character
print(d.replace("k","s"))

# to capitalize first letter of string by using capitalize functn
print(d.capitalize())

# addition of two strings
x="orange"
y="apple"
print(x+y)

# true or false
z="good morning"
print(z.startswith("hei"))
print(z.endswith("morning"))

# to count the repeated string-by using count fnctn
g="hii","hello","hii"
print(g.count("hii"))

# to swap uppercase and lower case- by using swapcase fnctn
c="hai Hello"
result=c.swapcase()
print(result)


#to create a SET 
a={1,2,3}
print(a)
b={"a","b","c"}
print(b)

# to find length of set
print(len(a))

# it coudn't find data using index value--it hasn't proper position
#print(b[0])

# to find is in or is not---true/false
print("b" in b)
print("f" in b)


b.add("d")
print(b)
b.update(["f","g","hiii"])
print(b)
b.remove("b")
print(b)
b.discard("h")
print(b)

a={"apple","orange","pineapple","grapes"}
b={"white","black"}
c=a.union(b)
print(c)

a={"apple","orange","pineapple","grapes"}
b={"white","orange","black"}
c=a.intersection(b)
print(c)

a={"apple","orange","pineapple","grapes"}
b={"white","apple","black"}
c=a.difference(b)
print(c)
c=b.difference(a)
print(c)

a.clear()
print(a)

del a
