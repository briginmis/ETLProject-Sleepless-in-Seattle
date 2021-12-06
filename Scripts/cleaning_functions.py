import pandas as pd

def explode_into_rows_in_new_table (input_df:pd.DataFrame,id_column, explode_column):
    # remove the { and } and " from the amenities column
    input_df[explode_column]=input_df[explode_column].str.replace('{','')
    input_df[explode_column]=input_df[explode_column].str.replace('}','')
    input_df[explode_column]= input_df[explode_column].str.replace('"','')
    input_df[explode_column]= input_df[explode_column].str.replace('[','')
    input_df[explode_column]= input_df[explode_column].str.replace(']','')
    input_df[explode_column]= input_df[explode_column].str.replace("'","")


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
    df2=df2.reset_index(drop=True)
    return df2


def clean_all(df):
    for x in range(len(df.columns)):
        try:
            if str.find(df.iloc[:, x].name,'url')>0: # if column header contains 'url' then skip column
                z=1
            else:
                y = 0
                while df.iloc[y, x]!=df.iloc[y, x]: # Check for NaN value and skip to next row to test
                    y = y+1
                if str.find(df.iloc[y, x],'$')>=0: # if column content contains '$' then remove the '$' and ','
                    df.iloc[:, x] = df.iloc[:, x].str.replace('$','')
                    df.iloc[:, x] = df.iloc[:, x].str.replace(',','')
                elif str.find(df.iloc[y, x],'%')>0: # If column content contains '%' then remove '%'
                    df.iloc[:, x] = df.iloc[:, x].str.replace('%','')
                elif (len(df.iloc[y, x])==1) and (str.find(df.iloc[y, x],'t')>=0 or str.find(df.iloc[0, x],'f')>=0): # If column content is 't' or 'f' and length is 1 then change column to True or False
                    df.iloc[:, x] = df.iloc[:, x].str.replace('t','True')
                    df.iloc[:, x] = df.iloc[:, x].str.replace('f','False')
        except:
            z=1