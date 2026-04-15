import os
import argparse
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CFBD_API_KEY")

def get_bearcat_game(year, week):
    url = "https://api.collegefootballdata.com/games"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "accept": "application/json"
    }
    params = {
        "year": year,
        "week": week,
        "team": "Cincinnati"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        games = response.json()
        if len(games) > 0:
            game = games[0] 
            
            home = game.get('homeTeam', 'Unknown')
            away = game.get('awayTeam', 'Unknown')
            is_neutral = game.get('neutralSite', False)
            
            if home == "Cincinnati":
                opponent = away
                location = "vs"
            else:
                opponent = home
                location = "@"
                
            if is_neutral:
                location = "vs (Neutral Site)"
                
            print(f"Year {year}, Week {week} Matchup: Bearcats {location} {opponent}")
        else:
            print(f"No game found for the Bearcats in Year {year}, Week {week}. (Maybe a bye week?)")
    else:
        print(f"Error fetching data: Status Code {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Track Cincinnati Bearcats Football Stats")
    parser.add_argument("--year", type=int, required=True, help="The season year (e.g., 2024)")
    parser.add_argument("--week", type=int, required=True, help="The week of the season (e.g., 1)")
    
    args = parser.parse_args()
    
    get_bearcat_game(args.year, args.week)