# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def time(a,b,h):
    time=(1/2)*b*h 
    print("the area of a triangle is ",time)
   
time(1/2,12,24)
chocolate1 = "milk"
chocolate2 = "dark"
chocolate3 = "white"

print(chocolate1)
print("chocolate1")

milk =3
dark =6
white =9

milk = milk+3
print(milk+20)

dark = dark+6
print(dark+6)

white = white+9
print(white+9)

import math
dir(math)

math.factorial(7)

math.sqrt(350)
math.exp(2)
math.pow(2.718281828459045,2)
math.pow(35,9)
(35**

 studentlistdf=[["Steve",32,"M"],["Lia",28,"F"]]
import pandas

studentlistdf = pandas.DataFrame(studentlistdf,columns=["name","age","gender"])
studentlistdf

import plotly
from plotly.offline import plot
import plotly.graph_objs as go 

agename = go.Bar(x=studentlistdf["name"] ,y=studentlistdf["age"])
plot([agename])

import plotly 
from plotly.offline import plot
import plotly.graph_objs as go 

wodf = pandas.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")
wodf

womenoccupation = go.Bar(x= wodf['occupation", y=wodf["women"],
                        marker = {"color' : ["women"],
                                  'colorscale" ; "rainbow"})
    
    plot([womenoccupation])
titles = go.layout(titlec = "percentage of women employed by occupation",
                   xaxis= go.layout.XAxis(title = go.layout.yaxis.title(text = occupation",)
                                          (text = "percentage")