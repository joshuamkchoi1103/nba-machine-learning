import pandas as pd
import os

MVP_DICT = {
    2012: "LeBron James", 2013: "LeBron James", 2014: "Kevin Durant",
    2015: "Stephen Curry", 2016: "Stephen Curry", 2017: "Russell Westbrook",
    2018: "James Harden", 2019: "Giannis Antetokounmpo", 2020: "Giannis Antetokounmpo",
    2021: "Nikola Jokic", 2022: "Nikola Jokic", 2023: "Joel Embiid", 2024: "Nikola Jokic"
}

def clean_name(name):
    return name.replace("*", "").strip()

def build_dataset():
    all_data = []

    for year in range(2012, 2025):
        df = pd.read_csv(f"data/player_stats/{year}.csv")
        df['Player'] = df['Player'].apply(clean_name)
        df = df[df['MP'] >= 1500]  # Played enough minutes
        df['Season'] = year
        df['Label'] = (df['Player'] == MVP_DICT[year]).astype(int)

        all_data.append(df[['Player', 'Season', 'PER', 'WS', 'BPM', 'VORP', 'Label']])

    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_csv("data/mvp_dataset.csv", index=False)
    print("Saved data/mvp_dataset.csv")

if __name__ == "__main__":
    build_dataset()
