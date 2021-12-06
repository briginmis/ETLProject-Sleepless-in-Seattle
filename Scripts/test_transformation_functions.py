import pandas as pd
import datetime as dt
from dans_functions import * 

def test_explode_into_rows_in_new_table():

    # ASSEMBLE 
    input_df = pd.DataFrame({
        "host_id": [956883,5177328],
        "host_verifications": [["'email'","'phone'"],["'reviews'","'email'"]]
    })

    expected_df = pd.DataFrame({
        "host_id": [956883,956883,5177328,5177328], 
        "host_verifications": ["email","phone","reviews","email"] 
    })

    # ACT 
    output_df = explode_into_rows_in_new_table(input_df=input_df, id_column = "host_id", explode_column = "host_verifications")

    # ASSERT 

    pd.testing.assert_frame_equal(left=output_df, right=expected_df,check_exact=True)
 