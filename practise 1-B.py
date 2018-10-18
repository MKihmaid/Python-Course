
# coding: utf-8

# In[ ]:


l= str(input("what is your name"))
print(f"Welcome , {l}") 

y=input("enter the first num : ")
z=input("enter the second numb : ")
 
t=float(y)+float(z) 
o=float(y) - float(z) 
p= float(y)*float(z)
q=float(y)/float(z)
u=float(y)%float(z)
r=float(y)**float(z)
print("the sum is ", t )
print ("the minus is" , o )
print("the multi is " , p )
print("the divison is " , q )
print("the reminder is " , u )  
print("the exponent of first to second is " , r)


# In[27]:


x= float(input("enter your numb : ")) 
c=float

#in the case of changing the float to int a big difference will occur specially for f(x) between -100 to -25 due to the power force 
#so i tried this whren it is a -29 the answer was 702781 bu when it is -28.9999 then the answer is 707271.244 a very big difference

if x < -100:  
    c=x*-1       
elif x >= -100 and x <= -25:
    c=x**4 
elif x >= -25 and x<= 0:
    c=3*x**2 - 1
elif x >0 and x <=100:
    c= 1.571 * x + pow(3,x)
else:
    c=x 
print (c) 
 
    

