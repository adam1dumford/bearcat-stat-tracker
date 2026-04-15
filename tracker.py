import os
import requests
from dotenv import load_dotenv

# Load the API key from the hidden .env file
load_dotenv()
API_KEY = os.getenv("CFBD_API_KEY")

def get_bearcat_games(year):
    url = "https://api.collegefootballdata.com/games"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "accept": "application/json"
    }
    params = {
        "year": year,
        "team": "Cincinnati"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: Status Code {response.status_code}")
        return None

if __name__ == "__main__":
    games_data = get_bearcat_games(2025)
    
    if games_data and len(games_data) > 0:
        first_game = games_data[0]
        
        # We now use the exact keys from your terminal output
        home = first_game.get('homeTeam', 'Unknown')
        away = first_game.get('awayTeam', 'Unknown')
        is_neutral = first_game.get('neutralSite', False)

        # Figure out who the opponent is and where the game is played
        if home == "Cincinnati":
            opponent = away
            location = "vs"
        else:
            opponent = home
            location = "@"
            
        # Override location if it's a neutral site
        if is_neutral:
            location = "vs (Neutral Site)"

        print(f"Matchup: Bearcats {location} {opponent}")