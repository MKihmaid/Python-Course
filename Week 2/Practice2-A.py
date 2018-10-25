
# coding: utf-8

# In[ ]:


n = int(input("your number (n) : "))
number=int(n**(0.50))
for i in range(3,number,2):
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        print(f"{n} is a composite number")
        break
    if  n % i == 0:
        print(f"{n} is a composite number")

else:
    print(f"{n} is a prime number")

