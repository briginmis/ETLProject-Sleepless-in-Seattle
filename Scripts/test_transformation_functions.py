import pandas as pd
import datetime as dt
from dans_functions import * 

def test_explode_into_rows_in_new_table():

    # ASSEMBLE 
    input_df = pd.DataFrame({
        "listing_id": [241032,953595],
        "amenities": ['{TV,"Cable TV"}','{"Wireless Internet",TV}']
    })

    expected_df = pd.DataFrame({
        "listing_id": [241032,241032,953595,953595], 
        "amenities": ["TV","Cable TV","Wireless Internet","TV"] 
    })

    # ACT 
    output_df = explode_into_rows_in_new_table(input_df=input_df, id_column = "listing_id", explode_column = "amenities")

    # ASSERT 

    pd.testing.assert_frame_equal(left=output_df, right=expected_df,check_exact=True)
 