import json
import requests
import pandas as pd

'''
Returns the schedule as a Pandas Dataframe.

Requires a season in the StartYearEndYear (20182019) format.

Acceptable game types:
    * PR - Preseason
    * R - Regular Season
    * P - Playoffs
'''
def get_schedule(season, game_type):
    if game_type.upper() not in ['PR', 'R', 'P']:
        print('Invalid gametype')
        return 0
    
    if len(str(season)) != 8:
        print("Invalid season")
        return 0

    request_string = "https://statsapi.web.nhl.com/api/v1/schedule?season={}&gameType={}".format(str(season), game_type)
    schedule_detailed = json.loads(requests.get(request_string).text)
    records = []

    for date in schedule_detailed['dates']:
        for game in date['games']:
            schedule_game_data = {}
            schedule_game_data['game_id'] = game['gamePk']
            schedule_game_data['away_team_id'] = game['teams']['away']['team']['id']
            schedule_game_data['home_team_id'] = game['teams']['home']['team']['id']
            schedule_game_data['away_team_name'] = game['teams']['away']['team']['name']
            schedule_game_data['home_team_name'] = game['teams']['home']['team']['name']

            if game['status']['abstractGameState'] == "Final":
                schedule_game_data['away_score'] = game['teams']['away']['score']
                schedule_game_data['home_score'] = game['teams']['home']['score']
            else:
                schedule_game_data['home_score'] = None
                schedule_game_data['away_score'] = None
            records.append(schedule_game_data)
    records_df = pd.DataFrame(records)
    return(records_df)