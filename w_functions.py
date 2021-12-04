import pandas as pd

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