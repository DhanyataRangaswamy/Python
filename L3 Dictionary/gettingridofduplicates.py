student_data={'ID1':
              {'Name':'Sasha','class':'V','Subjects':['english','maths','science']},
              'ID2':
              {'Name':'Tom','class':'V','Subjects':['english','maths','science']},
              'ID3':
              {'Name':'Sasha','class':'V','Subjects':['english','maths','science']},
              'ID4':
              {'Name':'Nick','class':'V','Subjects':['english','maths','science']}}
result={}
for key,value in student_data.items():
  if value not in result.values():
   result[key]=value
print (result)
  
  

            

