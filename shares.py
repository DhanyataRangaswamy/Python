shares1=int(input("Enter the number of existing shares: "))
val1=int(input("Enter the value of one share: "))
vs1=shares1*val1
shares2=int(input("Enter the number of shares you bought: "))
val2=int(input("Enter the value of new shares bought: "))
vs2=shares2*val2
avg=int((vs1+vs2)/(shares1+shares2))
print("The average value of your shares is",avg)