import pdftables_api
import pandas as pd
# import os
c = pdftables_api.Client('p6rxm6rk91il')

def convert(INPUT_FILENAME='name.pdf'):
	OUTPUT_FILENAME='result.csv'
	c.csv(INPUT_FILENAME,OUTPUT_FILENAME) 
	data= pd.read_csv(OUTPUT_FILENAME)
	# removeFile(INPUT_FILENAME)
	# removeFile(OUTPUT_FILENAME)	
	return data 
	
# def removeFile(FILENAME):
# 	if os.path.isfile(FILENAME):
# 		os.remove(FILENAME)