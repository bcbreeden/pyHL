import json
import requests
import pandas as pd

'''
Pulls all of the plays for a given game id. Plays will be returned as a Pandas Dataframe.
'''
def get_game_plays(game_id):
    request_string = 'https://statsapi.web.nhl.com/api/v1/game/{}/feed/live'.format(game_id)
    game_detailed = json.loads(requests.get(request_string).text)

    play_data = {}
    records = []

    play_data['home_team_id'] = game_detailed['gameData']['teams']['home']['id']
    play_data['away_team_id'] = game_detailed['gameData']['teams']['away']['id']
    play_data['home_team'] = game_detailed['gameData']['teams']['home']['name']
    play_data['away_team'] = game_detailed['gameData']['teams']['away']['name']
    plays = game_detailed['liveData']['plays']['allPlays']
    for play in plays:
        play_data['play_id'] = int(str(game_id) + str(play['about']['eventId']))
        play_data['game_id'] = game_id
        play_data['event'] = play['result']['event']
        play_data['event_id'] = play['about']['eventId']
        play_data['event_type_id'] = play['result']['eventTypeId']
        play_data['description'] = play['result']['description']
        play_data['time_stamp'] = play['about']['dateTime']
        play_data['period'] = play['about']['period']
        play_data['period_time'] = play['about']['periodTime']
        play_data['period_time_remaining'] = play['about']['periodTimeRemaining']
        play_data['goals_home'] = play['about']['goals']['home']
        play_data['goals_away'] = play['about']['goals']['away']
        try:
            play_data['team_id'] = play['team']['id']
            play_data['team_name'] = play['team']['name']
            play_data['team_abrv'] = play['team']['triCode']
        except(KeyError):
            print('No team assignment for play.')
            play_data['team_id'] = None
            play_data['team_name'] = None
            play_data['team_abrv'] = None
        records.append(play_data)
        print('Play {} has been added to the records list.'.format(play_data['play_id']))
    records_df = pd.DataFrame(records)
    return(records_df)

print(get_game_plays(2022010001).head())