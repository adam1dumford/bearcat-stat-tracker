# Bearcat Stat Tracker

A Command Line Interface (CLI) Python application that fetches and formats Cincinnati Bearcats football schedules using the College Football Data (CFBD) API.

## Features
* **Custom CLI:** Fetch matchup data for any specific year and week.
* **Score Tracking:** Displays final scores for completed games and intelligently tags future/unplayed matchups.
* **Smart Parsing:** Automatically formats output for home, away, and neutral-site games.
* **Edge Case Handling:** Detects and gracefully handles bye weeks.
* **Tested:** Includes a comprehensive `pytest` suite for core formatting logic.
* **Automated:** Features a GitHub Actions CI/CD pipeline.

## Prerequisites
* Python 3.12+
* A free API key from [College Football Data](https://collegefootballdata.com/)

## Setup and Installation

1. Clone the repository and navigate into it:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/bearcat-stat-tracker.git](https://github.com/YOUR_USERNAME/bearcat-stat-tracker.git)
   cd bearcat-stat-tracker

2. Create and activate a virtual environment:
    python -m venv venv
    source venv/Scripts/activate

3. Install the required dependencies:
    pip install -r requirements.txt

4. Create a hidden .env file in the root directory and add your API key:
    CFBD_API_KEY=your_actual_key_here

## Usage

Run the script via the command line by passing the --year and --week arguments:
    python tracker.py --year 2024 --week 10

## Testing

To run the automated test suite locally, ensure your virtual environment is active and run:
    pytest