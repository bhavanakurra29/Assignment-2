#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


# Write a python program to remove empty list from a list


# In[5]:


lst=[1,2,[],3,[],4,5,6]
res=list(filter(None, lst))
print("the list after removal of empty list is",res)


# # Question 2

# In[6]:


# Write a python program to remove all duplicates from a given sentence


# In[11]:


s="Python is great and Java is also great"
l=a.split()
k=[]
for i in l:
    if (s.count(i)>1 and (i not in k) or s.count(i)==1):
        k.append(i)
print(' '.join(k))


# # Question 3

# In[12]:


# Write a pyhton program to find all occurences of a character in the given string


# In[ ]:


a="bhavana"
counter=

