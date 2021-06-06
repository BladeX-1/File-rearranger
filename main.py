#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from os import path
from os import system as cmd


# In[2]:


all_files_and_dir=os.listdir()


# In[3]:


all_files_and_dir_upper=[]
for i,j in enumerate(all_files_and_dir):
    all_files_and_dir_upper.append( j.upper() )


# In[4]:


folderName2exetenctions={'Music':'mp3',
                         'Documents':'pdf doc docx ppt xls txt'.split(' '),
                         'Videos':'mp4 wmv avi mov mkv 3gp'.split(' '),
                         'Compressed':'zip rar jar tar 7z gz gzip pak z'.split(' '),
                         'Executables':'exe msi'.split(' ')
                        }
exetenctionsUpper2folderName={}
for foldername in folderName2exetenctions:
    for exetenction in folderName2exetenctions[foldername]:
        exetenctionsUpper2folderName[exetenction.upper()]=foldername


# In[5]:


print(exetenctionsUpper2folderName)


# In[6]:


for k in folderName2exetenctions.keys():
    if(k.upper() not in all_files_and_dir_upper):
        cmd('md '+k)


# In[7]:


for name in all_files_and_dir:
    if(path.isfile(name)):
        namel=list(name)
        namel.reverse()
        namel.append('.')
        namel=namel[0:namel.index('.')]
        namel.reverse()
        exetenction=str(''.join(namel))
        print(exetenction)
        if(exetenction.upper() in exetenctionsUpper2folderName.keys()):
            print('here')
            foldername=exetenctionsUpper2folderName[exetenction.upper()]
            if( not path.exists('move "{}" "{}"'.format(name,foldername+'\\'+name)) ):
                cmd('move "{}" "{}"'.format(name,foldername+'\\'+name))


# In[ ]:





# In[ ]:





# In[ ]:




