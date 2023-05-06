from api.schedule import *

def test_get_schedule_length():
    schedule_df = get_schedule(20192020, "r")
    assert len(schedule_df.index) > 2

def test_invalid_schedule_game_type():
    error_code = get_schedule(20192020, "PreSeason")
    assert error_code == 0

def test_invalid_schedule_season():
    error_code = get_schedule(2020, "pr")
    assert error_code == 0