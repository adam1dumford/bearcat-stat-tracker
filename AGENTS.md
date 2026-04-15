# AI Assistance Disclosure

For this project, I used an AI assistant as a pair-programming tool to build the Bearcat Stat Tracker. As the lead developer, I guided the architecture and verified all logic.

### How AI was utilized:

1. **API Integration:** I used AI to help structure the initial `requests` call to the College Football Data (CFBD) API and set up secure `.env` credential loading.
2. **Troubleshooting & Debugging:** - When the API returned "Unknown" for team names, I recognized the error, generated a diagnostic script to view the raw JSON, and used the AI to help remap the logic to the correct camelCase keys (`homeTeam`, `awayTeam`).
   - I used the AI to help resolve Python `IndentationError` blocks during the Command Line Interface (CLI) implementation.
3. **Refactoring & Testing:** I prompted the AI to refactor the display logic into a standalone `format_matchup` function so that it could be tested offline. We then co-wrote a 5-test `pytest` suite.
4. **CI/CD Pipeline:** I utilized AI to generate the YAML syntax for the GitHub Actions workflow, ensuring the tests run automatically on push.
5. **Feature Iteration:** I requested the addition of live score reporting after the core app was built. We used AI to safely inject this logic (`homePoints` / `awayPoints`) and completely rewrote the `pytest` suite to validate the new string formatting and edge cases.