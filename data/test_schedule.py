from api.schedule import *

def test_get_schedule_length():
    schedule_df = get_schedule()
    assert len(schedule_df.index) > 0

