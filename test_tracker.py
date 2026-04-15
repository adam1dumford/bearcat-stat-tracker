from tracker import format_matchup

def test_format_matchup_home_game():
    fake_game = {
        "homeTeam": "Cincinnati", 
        "awayTeam": "Houston", 
        "neutralSite": False,
        "homePoints": 24,
        "awayPoints": 14
    }
    result = format_matchup(2024, 5, fake_game)
    assert result == "Year 2024, Week 5 Matchup: Bearcats vs Houston | Final: 24-14"

def test_format_matchup_away_game():
    fake_game = {
        "homeTeam": "Iowa State", 
        "awayTeam": "Cincinnati", 
        "neutralSite": False,
        "homePoints": 20,
        "awayPoints": 27
    }
    result = format_matchup(2024, 6, fake_game)
    assert result == "Year 2024, Week 6 Matchup: Bearcats @ Iowa State | Final: 27-20"

def test_format_matchup_neutral_site():
    fake_game = {
        "homeTeam": "Cincinnati", 
        "awayTeam": "Nebraska", 
        "neutralSite": True,
        "homePoints": None,
        "awayPoints": None
    }
    result = format_matchup(2025, 1, fake_game)
    assert result == "Year 2025, Week 1 Matchup: Bearcats vs (Neutral Site) Nebraska | (Game not yet played)"

def test_format_matchup_missing_home_team():
    fake_game = {
        "awayTeam": "Cincinnati", 
        "neutralSite": False
    }
    result = format_matchup(2024, 2, fake_game)
    assert result == "Year 2024, Week 2 Matchup: Bearcats @ Unknown | (Game not yet played)"

def test_format_matchup_missing_away_team():
    fake_game = {
        "homeTeam": "Cincinnati", 
        "neutralSite": False
    }
    result = format_matchup(2024, 3, fake_game)
    assert result == "Year 2024, Week 3 Matchup: Bearcats vs Unknown | (Game not yet played)"