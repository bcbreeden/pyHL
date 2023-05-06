from api.plays import *
import pandas as pd

def test_df_length():
    df = get_game_plays(2022010001)
    assert len(df.index) > 0

def test_df_invalid_id():
    error_code = get_game_plays(453546)
    assert error_code == 2