import numpy as geek 

new1=geek.array([1,2,3])
new2=geek.array([4,5,6])
  
arr1 = geek.array([[2, 4], [6, 8]]) 
arr2 = geek.array([[3, 5], [7, 9]]) 
  
gfg = geek.concatenate((arr1, arr2), axis = 1) 

newc=geek.concatenate((new1,new2))
print(newc)
  
print (gfg) 