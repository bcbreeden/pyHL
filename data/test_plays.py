from api.plays import *
import pandas as pd

def test_df_lenth():
    df = get_game_plays(2022010001)
    assert len(df.index) > 0