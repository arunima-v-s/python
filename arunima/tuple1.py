# to create a tuple
a=(1,2,3,4,5)
print(a)

# to find length of tuple-by using len fnctn
print(len(a))

# to edit tuple-coverting the tuple to a list by using list fnctn- converting it back to tuple by tuple fnctn
b=list(a)
b.append(6)
print(b)
a=tuple(b)
print(a)