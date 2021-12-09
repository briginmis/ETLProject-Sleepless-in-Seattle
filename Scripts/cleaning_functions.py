#Import dependencies

import pandas as pd

#Create function to convert list in one cell, to many rows

def explode_into_rows_in_new_table (input_df:pd.DataFrame,id_column, explode_column):
    # remove any unwanted brackets and quotation marks from the amenities column
    input_df[explode_column]=input_df[explode_column].str.replace('{','')
    input_df[explode_column]=input_df[explode_column].str.replace('}','')
    input_df[explode_column]= input_df[explode_column].str.replace('"','')
    input_df[explode_column]= input_df[explode_column].str.replace('[','')
    input_df[explode_column]= input_df[explode_column].str.replace(']','')
    input_df[explode_column]= input_df[explode_column].str.replace("'","")


    # Create lists to store id and list of amenities
    id_list=[]
    explode_list=[]
    #iterate through each row and convert the string lists to actual lists using split function
    for index,row in input_df.iterrows():
        id_list.append(row[id_column])
        explode_list.append(row[explode_column].split(","))
    
    # Create a data frame from the id and amenities for each instance
    df2=pd.DataFrame({id_column:id_list,explode_column:explode_list})

    # Explode (split the lists into new rows)
    df2=df2.explode(explode_column)
    df2=df2.reset_index(drop=True)
    return df2

#Create function to clean prices, by removing dollar signs and commas
def clean_dollar(input_df, col_list):
    df=input_df.copy(deep=True)
    for col in col_list:
        df[col] = df[col].str.replace('$','')
        df[col] = df[col].str.replace(',','')
    return df

#Create function to convert percentages into floats by removing '%' sign
def clean_percent(input_df, col_list):
    df=input_df.copy(deep=True)
    for col in col_list:
        df[col] = df[col].str.replace('%','')
    return df

#Create function to replace 't' with 'True', and 'f' with False
def clean_boo(input_df, col_list):
    df=input_df.copy(deep=True)
    for col in col_list:
        df[col] = df[col].str.replace('t','True')
        df[col] = df[col].str.replace('f','False')
    return df