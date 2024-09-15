setx={"A","B","C"}
sety={"A","C","F"}
print("The original sets are: ")
print(setx)
print(sety)
setz=setx.intersection(sety)
print("Their intersection is: ")
print(setz)

setx={"red","blue","green"}
sety={"green","yellow"}
print("The original sets are: ")
print(setx)
print(sety)
setz=setx.union(sety)
print("Their union is: ")
print(setz)

setx={"1","2","3"}
sety={"3","4","0"}
print("The original sets are: ")
print(setx)
print(sety)
setz=setx.difference(sety)
print("Their difference is: ")
print(setz)

