weather=(1,0,0,1,0,1,1)
sunny=0
rainy=0
for i in range(len(weather)-1):
    if weather[i]==0:
        sunny+=1
    else:
        rainy+=1
if (sunny>rainy) :
    print("Good weather")
else :
    print("Bad weather")
    
