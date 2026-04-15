import os
import argparse
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CFBD_API_KEY")

def format_matchup(year, week, game):
    """Takes a game dictionary and formats it into a readable string with scores."""
    home = game.get('homeTeam', 'Unknown')
    away = game.get('awayTeam', 'Unknown')
    home_score = game.get('homePoints')
    away_score = game.get('awayPoints')
    is_neutral = game.get('neutralSite', False)
    
    # Logic for determining the opponent and location
    if home == "Cincinnati":
        opponent = away
        location = "vs"
        cin_score = home_score
        opp_score = away_score
    else:
        opponent = home
        location = "@"
        cin_score = away_score
        opp_score = home_score
        
    if is_neutral:
        location = "vs (Neutral Site)"
        
    # Build the base string
    base_msg = f"Year {year}, Week {week} Matchup: Bearcats {location} {opponent}"
    
    # Only add scores if the game has actually been played (points aren't None)
    if cin_score is not None and opp_score is not None:
        return f"{base_msg} | Final: {cin_score}-{opp_score}"
    else:
        return f"{base_msg} | (Game not yet played)"

def get_bearcat_game(year, week):
    """Fetches the data from the API and prints the formatted matchup."""
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
            # Use our new function to format the string
            matchup_string = format_matchup(year, week, game)
            print(matchup_string)
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