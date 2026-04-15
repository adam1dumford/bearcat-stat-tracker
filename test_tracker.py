from tracker import format_matchup

def test_format_matchup_home_game():
    fake_game = {"homeTeam": "Cincinnati", "awayTeam": "Houston", "neutralSite": False}
    result = format_matchup(2024, 5, fake_game)
    assert result == "Year 2024, Week 5 Matchup: Bearcats vs Houston"

def test_format_matchup_away_game():
    fake_game = {"homeTeam": "Iowa State", "awayTeam": "Cincinnati", "neutralSite": False}
    result = format_matchup(2024, 6, fake_game)
    assert result == "Year 2024, Week 6 Matchup: Bearcats @ Iowa State"

def test_format_matchup_neutral_site():
    fake_game = {"homeTeam": "Cincinnati", "awayTeam": "Nebraska", "neutralSite": True}
    result = format_matchup(2025, 1, fake_game)
    assert result == "Year 2025, Week 1 Matchup: Bearcats vs (Neutral Site) Nebraska"

def test_format_matchup_missing_home_team():
    # Edge case: API glitch drops the home team name
    fake_game = {"awayTeam": "Cincinnati", "neutralSite": False}
    result = format_matchup(2024, 2, fake_game)
    assert result == "Year 2024, Week 2 Matchup: Bearcats @ Unknown"

def test_format_matchup_missing_away_team():
    # Edge case: API glitch drops the away team name
    fake_game = {"homeTeam": "Cincinnati", "neutralSite": False}
    result = format_matchup(2024, 3, fake_game)
    assert result == "Year 2024, Week 3 Matchup: Bearcats vs Unknown"