import pandas as pd

def explode_into_rows_in_new_table (input_df:pd.DataFrame,id_column, explode_column):
    # remove the { and } and " from the amenities column
    input_df[explode_column]=input_df[explode_column].str.replace('{','')
    input_df[explode_column]=input_df[explode_column].str.replace('}','')
    input_df[explode_column]= input_df[explode_column].str.replace('"','')
    input_df[explode_column]= input_df[explode_column].str.replace('[','')
    input_df[explode_column]= input_df[explode_column].str.replace(']','')

    # split the lists inside the amenities column for each row ????
    id_list=[]
    explode_list=[]
    for index,row in input_df.iterrows():
        id_list.append(row[id_column])
        explode_list.append(row[explode_column].split(","))
    
    # Create a data frame from the id and amenities for each instance
    df2=pd.DataFrame({id_column:id_list,explode_column:explode_list})

    # Explode (split the lists into new rows)
    df2=df2.explode(explode_column)
    return df2