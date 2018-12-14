#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Pickling in Python


# In[ ]:


import pickle


# In[2]:


example_dict = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}


# In[3]:


selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)


# In[4]:


selfref_list


# In[5]:


pickle_out = open("dict.pickle","wb") #writing in binary mode

# Pickle dictionary using protocol 0.
pickle.dump(example_dict, pickle_out)  #use pickle.dump() to put the dict into opened file


# In[6]:


# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, pickle_out, -1)

pickle_out.close()


# In[7]:


#unpickling in Python
#To read from a pickled file


# In[8]:


import pprint, pickle


# In[18]:


pickle_in = open('dict.pickle', 'rb')

data1 = pickle.load(pickle_in)
pprint.pprint(data1)


# In[19]:


data2 = pickle.load(pickle_in)
pprint.pprint(data2)

pickle_in.close()


# In[ ]:




