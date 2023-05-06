import json
import requests

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

    api_string = "https://statsapi.web.nhl.com/api/v1/schedule?season={}&gameType={}".format(str(season), game_type)
    return False