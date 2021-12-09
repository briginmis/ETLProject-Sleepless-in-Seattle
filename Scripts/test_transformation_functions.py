#Unit testing transformation functions

import pandas as pd
import datetime as dt
from cleaning_functions import *
import warnings
warnings.filterwarnings("ignore")

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
 

def test_clean_dollar():

    # ASSEMBLE
    input_df = pd.DataFrame({
        "price":["", "$1,000.00", "$85.00"]
    })

    expected_df = pd.DataFrame({
        "price":["", "1000.00", "85.00"]
    })

    # ACT
    output_df = clean_dollar(input_df, ["price"])

    # ASSERT

    pd.testing.assert_frame_equal(left = output_df, right=expected_df, check_exact = True)

def test_clean_percent():

    # ASSEMBLE
    input_df = pd.DataFrame({
        "host_response_rate":["96%", "N/A", "98%"]
    })

    expected_df = pd.DataFrame({
        "host_response_rate":["96", "N/A", "98"]
    })

    # ACT
    output_df = clean_percent(input_df, ["host_response_rate"])

    # ASSERT

    pd.testing.assert_frame_equal(left = output_df, right=expected_df, check_exact = True)

def test_clean_boo():

    # ASSEMBLE
    input_df = pd.DataFrame({
        "host_is_superhost":["f", "t", "f"]
    })

    expected_df = pd.DataFrame({
        "host_is_superhost":["False", "True", "False"]
    })

    # ACT
    output_df = clean_boo(input_df, ["host_is_superhost"])

    print(output_df)

    # ASSERT

    pd.testing.assert_frame_equal(left = output_df, right=expected_df, check_exact = True)