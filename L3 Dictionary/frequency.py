test_dict={'My':1,'name':2,'is':2,'Dhanyata':2}
print("The original dictionary" + str(test_dict))
k=2
res=0
for key in test_dict:
    if test_dict[key]==k:
     res=res+1
print("Frequency of k is"+str(res))