#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyinputplus as pyip

while True:
    price = {'wheat':10,'white':12,'sourdough':13,
            'chicken':50,'turkey':45,'ham':35,'tofu':35,
            'cheddar':20,'Swiss':20,'mozzarella':20}
    items = []
    bread_type = pyip.inputMenu(['wheat','white','sourdough'],numbered=True)
    items.append(bread_type)
    protein_type = pyip.inputMenu(['chicken','turkey','ham','tofu'],numbered=True)
    items.append(protein_type)
    prompt = "Do you Want Cheese? "
    cheese = pyip.inputYesNo(prompt)
    
    if cheese == 'yes':
        cheese_type = pyip.inputMenu(['cheddar','Swiss','mozzarella'],numbered=True)
        items.append(cheese_type)
    prompt = "Enter no of items: "
    item_num = pyip.inputInt(prompt)
    value = []
    for i in items:
        v1 = price[i]
        value.append(v1)
    result = sum(value)
    print('The total Cost of your order is %s $.'%(result*item_num))
    break


# In[ ]:




