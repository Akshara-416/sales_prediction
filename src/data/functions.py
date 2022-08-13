import numpy as np
import pandas as pd

#Function to get initial data statistics
def input_read(file):
    
    #read input file
    file_type = file.split(".")[-1]
    if file_type =='csv':
        df = pd.read_csv(file)
    elif file_type =='xlsx':
        df = pd.read_excel(file)
    
    file = file.split("/")[-1]
    #Number of records
    file_name = file.split(".")[0]
    record_count = df.shape
    print("Shape of {} : {}\n". format(file_name,record_count))
    
    #Column names
    column_list = df.columns
    print("List of columns in {} : {}".format(file_name,column_list))
    
    #Datatypes
    print("\nDatatype of columns in {} :\n{}".format(file_name,df.dtypes))
    
    #data_stats(df)
    
    return df

def data_stats(data):
    
    #print(data)
    
    #Data describe
    print("\nData stats: \n{}".format(data.describe()))
    
    #Null count
    print("\nNull count :\n{}".format(data.isnull().sum()))
    
    return