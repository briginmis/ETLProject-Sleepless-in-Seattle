import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import cleaning_functions as cf

# read in csv
df=pd.read_csv("../Resources/listings.csv")

# keep only those columns
df = df[['host_id','host_verifications']]

df3 = cf.explode_into_rows_in_new_table(input_df = df, id_column = "host_id", explode_column = "host_verifications")

# save as csv
df3.to_csv("../Resources/Host_Verifications_Clean.csv")

