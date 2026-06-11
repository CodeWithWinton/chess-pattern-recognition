# 📁 Data Directory

## Source
Dataset is loaded directly from **HuggingFace** — not stored locally in this repo.

🔗 **HuggingFace:** [angeluriot/chess_games](https://huggingface.co/datasets/angeluriot/chess_games)  
🔗 **GitHub:** [angeluriot/Chess_games](https://github.com/angeluriot/Chess_games)

## How to Load

```python
from datasets import load_dataset

dataset = load_dataset("angeluriot/chess_games")
```

## Dataset Stats

| Metric | Value |
|---|---|
| Total Games | 14M |
| Total Moves | 1.2B |
| Mean ELO | 2,388 |
| Format | Parquet |
| Size | 7.31 GB |

## Schema

```json
{
    "date": "YYYY.MM.DD or null",
    "white_elo": "int or null",
    "black_elo": "int or null",
    "end_type": "resignation | checkmate | draw_agreement | stalemate | ...",
    "winner": "white | black | null",
    "moves_san": ["e4", "e5", "Nf3", ...],
    "moves_uci": ["e2e4", "e7e5", ...],
    "moves_custom": ["w.♙e2♙e4..", ...],
    "source": "string"
}
```

## Folders

- **`raw/`** — Cache for HuggingFace downloads (auto-generated, gitignored)
- **`processed/`** — Cleaned & feature-engineered data (gitignored)
