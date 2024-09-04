def match_list(words):
    ctr=0 
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
         ctr+=1
         lst.append(word)
    print("The new list with same start and end letters are: ",lst )
    return ctr

count=match_list(['aba','aba','acg','aya','1001','1221'])
print("The number of elements in new list is: ",count)