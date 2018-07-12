import pdftables_api
import pandas as pd
c = pdftables_api.Client('e9zlcysareqc')
c.csv('input.pdf', 'output.csv') 

data= pd.read_csv('output.csv')
data['Enorlment NO.']=list(data['Enorlment NO.'])
data['Marks']=list(data['Marks'])

print(data)