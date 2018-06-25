import random  
c=4
a=input('enter s to roll a dice')
while(c<=100):
    if(a=='s'):
      r=random.randint(1,6)
      print(r)
      c=c+r
 
