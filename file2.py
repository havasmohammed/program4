my_string="My name is Havas My name is Havas"
l=my_string.split()
count={}
for i in l:
 if i in count.keys():
    count[i] +=1
 else:
    count[i] =1
      
print (count)
