a={"name":"arunima","age":20,"email":"a@mail"}
print(a)
b=a["name"]
print(b)
c=a.get("name")
print(c)

a["name"]="vismaya"
print(a)
a["email"]="v@gmail"
print(a)
a["phone no"]=739920
print(a)

z=a.copy()
print(z)

a.pop("email")
print(a)

a.clear()
print(a)
