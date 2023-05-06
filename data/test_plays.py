from api.plays import *
import pandas as pd

def test_plays_df_length():
    plays_df = get_game_plays(2022010001)
    assert len(plays_df.index) > 2

def test_df_invalid_id():
    error_code = get_game_plays(453546)
    assert error_code == 2