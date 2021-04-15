#!/usr/bin/env python
# coding: utf-8

# In[2]:


if __name__ == "__main__":
    from bs4 import BeautifulSoup
    import csv

soup = BeautifulSoup (open("2020_NFL.htm"), features="lxml")
print(soup.prettify())


# In[3]:


list(soup.children)


# In[4]:


[type(item) for item in list(soup.children)]


# In[5]:


trs = soup.find_all('tr')
for tr in trs:
    print(tr)


# In[6]:


top_players = soup.find_all('tr')[1:21]
for player in top_players:
    names = player.contents[0]
    
    print(names)
    


# In[7]:


position = soup.find_all('span', class_='CellPlayerName-position')[1:21]
print(position)


# In[8]:


team = soup.find_all('span', class_='CellPlayerName-team')[1:21]
print(team)


# In[9]:


score = soup.find_all('td', class_='TableBase-bodyTd TableBase-bodyTd--number')
print(score)


# In[10]:


file = csv.writer(open("NFL_2020.csv", "w"))
file.writerow(["Names", "TD"]) 

top_players = soup.find_all('tr')[1:21]
for player in top_players:
    names = player.contents[0]
    
    print(names)
    file.writerow(names)


# In[11]:



    


# In[ ]:




