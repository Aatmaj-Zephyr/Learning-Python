>>> hardware={    "Brand": "Dell",    "Model": 2430,    "Year":  "2020"}
>>> print(hardware) #prints the value of the dictionary
{'Brand': 'Dell', 'Model': 2430, 'Year': '2020'}
>>> print(hardware["Model"])
2430
>>> print(hardware.get("Model"))
2430
>>> hardware["Year"]=2021 #Changing the value of the dictionary
>>> print(hardware)
{'Brand': 'Dell', 'Model': 2430, 'Year': 2021}
>>> print(hardware.pop("Model"))
2430
>>> print(hardware)
{'Brand': 'Dell', 'Year': 2021}
>>> hardware["Model"]="Lenovo"
>>> hardware["Year"]=2019
>>> print(hardware.popitem()) #popitem returns the last value entered
('Model', 'Lenovo')
>>> print(hardware)
{'Brand': 'Dell', 'Year': 2019}
>>> for y in hardware:
...     print(y)#Corresponds to each key
...
Brand
Year
>>> for x in hardware:
...      print(hardware[x])#referes to the value
...
Dell
2019
>>> for z in hardware.values():
...      print(z)
...
Dell
2019
>>> hardware.clear() #Cleares the dictionary (not delete)
>>> print(hardware)
{}
>>> print(hardware["Price"])#trying to remove element which is not present
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Price'
