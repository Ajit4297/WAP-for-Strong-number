#!/usr/bin/env python
# coding: utf-8

# In[27]:


def fact(n):
   f=1
   for i in range(1,n+1):
       f=f*i

   return f
n=int(input())
temp=n
s=0
while n!=0:
   d=n%10
   s=s+fact(d)
   n=n//10
if temp==s:
   print('true')
else:
   print('false')


# In[ ]:




