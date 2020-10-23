#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma as G


# In[17]:


k = 1
a = 4
b = 6
u = 0
N = 160


# In[18]:


M = np.random.randint(1, 161)
while M >= 0.4 * 160 and M <= 0.6 * 160:
    M = np.random.randint(1, 161)
L = N - M
arr = np.array([0] * (N - M) + [1] * M)
np.random.shuffle(arr)


# In[19]:


images = []
P = []
Q = []
m = 0
l = 0
MaxP = 0


# In[20]:


U_ML = M / 160.00
print ('%0.2f' % U_ML)


# In[ ]:


for j in range(len(arr)):
    P = []
    Q = []
    u = 0

    for i in range(101):
        if  u > 1:
            u = 1
        Norm = G(a+b+l+m)/(G(a+m)*G(b+l))
        u1 = pow(u, a-1 + m)
        u2 = pow(1 - u, b- 1 + l)
        P_Val = Norm * u1 * u2  #beta function
        if MaxP < P_Val:
            MaxP = P_Val
        P.append(P_Val)
        Q.append(u)
        u += 0.010000
        if arr[j] == 1:
            m += 1
        else:
            l += 1
fig = plt.figure()
plt.plot(U, P, 'g')
plt.ion()
plt.axis([0, 1, 0, 25])
plt.xlabel('μ ' + '(No. of points sampled = ' + str(j + 1) + ')')
plt.ylabel('Prior probability distribution (β)')
plt.text(0.4, 27, 'μ ML = ' + str(U_ML))
fig.savefig('/Users/harsha/Desktop/Imagedata3/plot' + str(j+1) + '.png')
   

