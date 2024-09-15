import array as arr
a=arr.array('i',[1,2,3,4,5,2,2])
print("The original array is: "+str(a))
print("The number of occurences of the number 2 is: "+str(a.count(2)))

a.reverse()
print("The reverse order of items is: ")
print(str(a))

     
