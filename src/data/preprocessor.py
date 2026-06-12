import pandas as pd
import chess
from datasets import load_dataset
from tqdm import tqdm

import os
os.environ.get("HF_TOKEN")

class ChessPreprocessor:
    def __init__(self, num_games=10000, min_moves=10):
        self.num_games = num_games
        self.min_moves = min_moves

    def load_data(self):
        dataset = load_dataset("angeluriot/chess_games", split="train", streaming=True)

        rows = list(dataset.take(10000))
        df = pd.DataFrame(rows)

        print(f"Loaded {len(df)} games")
        df.head()

        return df       

    def clean_data(self, df):
        df.isnull().sum().sum()
        df.isnull().sum()

        df['winner'] = df['winner'].fillna('draw')

        df['elo_missing'] = df['white_elo'].isnull()
        df['white_elo'] = df['white_elo'].fillna(df['white_elo'].median())
        df['black_elo'] = df['black_elo'].fillna(df['black_elo'].median())

        return df

    def filter_short_games(self, df):
        """Remove games with fewer than min_moves moves."""
        # TODO: Check len(moves_san) for each row
        pass

    def validate_moves(self, df):
        """Try replaying each game with python-chess. Drop corrupted ones."""
        # TODO: Loop through games, push moves on a chess.Board()
        # If any move throws an error, mark that game as invalid
        pass

    def run(self):
        """Full pipeline: load → clean → filter → validate → save."""
        df = self.load_data()
        df = self.clean_data(df)
        df = self.filter_short_games(df)
        df = self.validate_moves(df)
        df.to_parquet('data/processed/cleaned_games.parquet', index=False)
        print(f"Saved {len(df)} clean games.")
        return df
    