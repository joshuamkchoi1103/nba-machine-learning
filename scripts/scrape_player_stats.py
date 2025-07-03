import pandas as pd
import os

def scrape_advanced_season(season_end_year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season_end_year}_advanced.html"
    df = pd.read_html(url, header=0)[0]
    df = df[df['Player'] != 'Player']  # Remove duplicated header rows
    df = df.dropna(subset=["PER"])     # Only keep rows with valid data
    df = df[~df['Tm'].isin(['TOT'])]   # Ignore players with combined stats across teams
    os.makedirs('data/player_stats', exist_ok=True)
    df.to_csv(f"data/player_stats/{season_end_year}.csv", index=False)
    print(f"Saved advanced season stats for {season_end_year}")

if __name__ == "__main__":
    for year in range(2012, 2025):
        scrape_advanced_season(year)
