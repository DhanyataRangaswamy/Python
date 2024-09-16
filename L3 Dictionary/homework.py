test_dict={'hi':1,'how':2,'are':2,'you':2,'doing':1}
print("The original dictionary" + str(test_dict))
k=int(input("Frequency of: "))
res=0
for key in test_dict:
    if test_dict[key]==k:
     res=res+1
print("Frequency of", k, "is "+str(res))