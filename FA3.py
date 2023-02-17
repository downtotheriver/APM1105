#!/usr/bin/env python
# coding: utf-8

# In[4]:


num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 24, 26, 28, 30, 32]
for even in num:
    if even % 2==0:
        print(even)


# In[5]:


numbers = list(range(62))
even_numbers = numbers[10::2]
print(even_numbers)


# In[ ]:


def show_feu_professor_1():
    print("Name: Frederick Gella")
    print("Salary: 80 000.00 PHP")
    print("Name: Jeffrey Alvarina")
    print("Salary: 60 000.00 PHP")
    print("Name: JOANNA EUGENIO")
    print("Salary: 75 000.00 PHP")
    print("Name: MARIA LOURDES MARIANO")
    print("Salary: 70 000.00 PHP")
    print("Name: RICHMOND RIYADHEN LIM")
    print("Salary: 80 000.00 PHP")
    

def show_feu_professor(name, salary):
    print("Name:", name)
    print("Salary:", salary)
i=0
professor=[]
money=[]

show_feu_professor_1()
print()
print()
while i < 5:
    name=str(input("What is your name: "))
    salary=(input("What is your salary: "))
    if salary=='':
        salary=70000
    if float(salary) <= 70000:
        salary=70000
    professor.append(name)
    money.append(salary)
    i+=1
    
show_feu_professor(professor, money)


# In[ ]:




