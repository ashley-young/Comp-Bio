
# coding: utf-8

# In[ ]:


import csv
ifile  = open('train.csv', "r")
read = csv.reader(ifile)
for row in read:
    print (row) 

