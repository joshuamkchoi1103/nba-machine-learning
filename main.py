from scripts.scrape_player_stats import scrape_advanced_season
from scripts.preprocess_mvp import build_dataset
from scripts.train_mvp_model import train_model

if __name__ == "__main__":
    print("Fetching data...")
    for year in range(2012, 2025):
        scrape_advanced_season(year)

    print("Preprocessing MVP data...")
    build_dataset()

    print("Training MVP model...")
    train_model()
