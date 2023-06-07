from array import *
array1=array('i',[10,20,30,40,50])
for x in array1:
    print (x)
    print(array1[0])
    print(array1[-1])
    
    # inserting a value in an array
    
array1.insert(1,60)
for i in array1:
    print(i)
    
# deletion method  
array1.remove(10)  
for i in array1:
    print(i) 
    
# search method
array1.index(40)
for i in array1:
    print(i) 
    
myArray=['cat','dog','cow','goat','rabbit','sheep']
# myArray.index('cat')
print(myArray.index('rabbit'))
# for x in myArray:
#     print(x)  

# update operation
# it means updating an existing element in an array
myArray[5]=('elephant') 
print(myArray) 

# array in python
import array as arr
array_1=arr.array['i',2,3,4,5]
print(array_1)
print(type(array_1))
