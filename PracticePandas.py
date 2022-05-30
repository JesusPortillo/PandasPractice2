#Nombre: Jesus David Portillo Villa
#ID: 324718
#Email: jesus.portillo@upb.edu.co

from email.policy import default
import pandas as pd
import numpy as np

data = pd.read_excel("data.xlsx")

#exercise 1

imc = (data["weight"]/(data["height"])**2).round(0)
data["imc"] = imc

#exercise 2

compound_interest = ((data["money for investing"]*(1+(data["annual interest rate"]/100))**data["time for investing"])-data["money for investing"]).round()
data["compound interest"] = compound_interest

#exercise 3

condition_list = [
    (data["time to buy the bread after baking"] <= 6),
    (data["time to buy the bread after baking"] <= 12 ),
    (data["time to buy the bread after baking"] <= 18 ),
    (data["time to buy the bread after baking"] <= 24 )
]
choice_list = [10,20,30,40]
data["discount percentage"] = np.select(condition_list,choice_list,default="not specified")

#exercise 4

condition_list_for_extension = [
    (data["gender"] == "M"),
    (data["gender"] == "F" )
]
choice_list_for_extension = [data["phone number"] + "-11",data["phone number"] + "-10"]
data["number with extension"] = np.select(condition_list_for_extension,choice_list_for_extension,default="not specified")


print(data)
