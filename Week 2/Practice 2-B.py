
# coding: utf-8

# In[ ]:


x=int
z=int
y=str(input("the currencies to onvert between is in JD to $ or $ to JD or JD to TL or $ to JD or $ to TL or TL to JD or TL to $ "))
print(y)
x=int(input("the amount of money to convert :  "))

if y=="JD to $":
    z= x / 0.708
    print(z, "$")
elif y=="JD to TL":
    z= x * 7.8
    print(z, "TL")
elif y=="$ to TL":
    z= x * 5.8
    print(z, "TL")
elif y=="$ to JD":
    z= x * 0.708
    print(z, "JD")
elif y=="TL to JD":
    z= x / 7.8
    print(z, "JD")
else:
        y=="TL to $"
        z= x / 5.8 
        print(z, "$")

