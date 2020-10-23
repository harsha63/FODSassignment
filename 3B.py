#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np 
import matplotlib.pyplot as plt 
from pylab import figure, text, scatter, show
from scipy.special import gamma as G


# In[13]:


import scipy as sp
import random 
import scipy.integrate


# In[8]:


a=4; b=6; mu=np.linspace(0,1,100);
beta=(scipy.special.gamma (a+b)/(scipy.special.gamma (a)*scipy.special.gamma (b)))*((mu)**(a-1))*(((1-mu)**(b-1)))


# In[18]:


plt.plot(mu,beta)
text(0.1, 0.9,'prior', ha='center', va='center')


# In[30]:


## M = Number of Heads in Randomly Generated Sample. 
u = 0
N = 160
M = np.random.randint(1,161)
while(M >= 0.4*160 and M <= 0.6*160):
    M = np.random.randint(1,161)
L = N - M
arr = np.array([0]*(N-M) + [1]*(M))	
np.random.shuffle(arr)
U_ML = M/160.00

P = []
U = []
for i in range (101):
    if u > 1:
        u = 1
    Norm = G(a + b + N)/(G(a + M)*G(b + L))
    u1 = pow(u, (a - 1 + M))
    u2 = pow(1 - u, (b - 1  + L))
    P_Val = Norm * u1 * u2
    P.append(P_Val)
    U.append(u)
    u += 0.010000
        #print(Norm)
print('%0.2f' %U_ML)

fig = plt.figure()
plt.plot(U, P)
text(0.1, 0.9,'posterior', ha='center', va='center')
plt.ion()
plt.xlabel('μ')
plt.ylabel('P')
plt.show()
plt.pause(0.1)
plt.close()
fig.savefig('Final Graph.png')


# In[36]:


zero=random.randint(0,40)
one=160-zero
n=[0]*zero+[1]*one
random.shuffle(n)
N=n


# In[37]:


u=np.linspace(0,1,100)
b=lambda u: (u**N[i])*((1-u)**(1-N[i]))


# In[39]:


plt.plot(u,b(u))
text(0.1, 0.9,'likelihood', ha='center', va='center')

