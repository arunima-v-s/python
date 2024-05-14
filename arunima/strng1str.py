a="malayalam"
print(a)
print(a.upper())
b="MALAYALAM"
print(b.lower())
print(b.replace("L","z"))
print(a.capitalize())


a="how are you"
print(a.startswith("how"))
print(a.endswith("are"))
print(a.endswith("you"))

a="How are you? Are you okey"
print(a.count("how"))
print(a.count("you"))

print(a.swapcase())

a={"malayalam","tamil","english","hindi"}
print(len(a))
# true/false
print("blue" in a)
print("english" in a)

#to add data into set-by using add fnctn
a.add("blue")
print(a)

# to update set by using update fnctn-one or more data
a.update("white")
print(a)
a.update(["black","yellow"])
print(a)

# to remove data from set ,by using discard fnctin to remove the item that has not in the set-there occur a error
a.remove("hindi")
print(a)
a.discard("tamil")
print(a)
# there is no error when removing item that is not in the set
a.discard("kerala")
print(a)


# to find union,intersection,difference of two sets
a={"one","two","three","four","five"}
b={"one","two","three"}
c=a.union(b)
print(c)
c=a.intersection(b)
print(c)
c=a.difference(b)
print(a)
c=b.difference(a)
print(a)

#to clear and delete set
a.clear()
print(a)

del b
