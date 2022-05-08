# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 11:36:56 2022

@author: Ziyah
"""
from tkinter import*
import random

root=Tk()
root.title("capitals and countries")
root.geometry("500x500")
root.configure(background="gold")

country_word=Entry(root)
country_word.place(relx=0.5, rely=0.2, anchor=CENTER)

capital_word=Entry(root)
capital_word.place(relx=0.5, rely=0.3, anchor=CENTER)

country_name=Label(root)
capital_name=Label(root)
random_capital=Label(root)
random_country=Label(root)

country_list=[]
capital_list=[]
def addname():
    country=country_word.get()
    capital=capital_word.get()
    country_list.append(country)
    capital_list.append(capital)
    country_name["text"]="Country Name = " + str(country_list)
    capital_name["text"]="Capital Name = " + str(capital_list)
    
def random_name():
    capital_length=len(capital_list)
    country_length=len(country_list)
    random_no1=random.randint(0,capital_length-1)
    random_no2=random.randint(0,country_length-1)
    generate_random_capital=capital_list[random_no1]
    generate_random_country=country_list[random_no2]
    random_capital["text"]="Random Capital = "+ generate_random_capital
    random_country["text"]="Random Country = "+ generate_random_country
    
btn=Button(root, text="Display Country And Capital", command=addname, bg="#ffb254")
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
country_name.place(relx=0.5,rely=0.5,anchor=CENTER)
capital_name.place(relx=0.5,rely=0.6,anchor=CENTER)

btn1=Button(root, text="Display Random Country And Capital", command=random_name, bg="#ffb254")
btn1.place(relx=0.5,rely=0.7,anchor=CENTER)
random_country.place(relx=0.5,rely=0.8,anchor=CENTER)
random_capital.place(relx=0.5,rely=0.9,anchor=CENTER) 

root.mainloop()














