# ♟️ Chess Pattern Recognition & AI Training Bot

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?logo=pytorch&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

## Overview

A machine learning project that analyzes **14M+ high-level chess games** to:

- **Predict next moves** based on game history and board state
- **Recognize patterns** in opening, middlegame, and endgame play
- **Identify best games** from the dataset for both Black and White
- **Teach optimal move combinations** through pattern analysis
- **Human vs AI training bot** for interactive practice

## Dataset

Using the [Chess Games Dataset](https://github.com/angeluriot/Chess_games) by Angel Uriot:

| Metric | Value |
|---|---|
| Total Games | 14M |
| Total Moves | 1.2B |
| Mean ELO | 2,388 |
| Format | Parquet |
| Size | 7.31 GB |
| Time Range | 1600–2024 |

## Project Structure

```
chess-pattern-recognition/
├── data/
│   ├── raw/                    # Original dataset files
│   └── processed/              # Cleaned & feature-engineered data
├── notebooks/
│   ├── 01_eda.ipynb            # Exploratory Data Analysis
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_evaluation.ipynb
│   └── 05_best_games_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loader.py           # Dataset loading & HuggingFace integration
│   │   ├── preprocessor.py     # Data cleaning & transformation
│   │   └── feature_engineer.py # Board state & move features
│   ├── models/
│   │   ├── __init__.py
│   │   ├── move_predictor.py   # Next-move prediction model
│   │   ├── pattern_recognizer.py # Pattern recognition model
│   │   ├── game_evaluator.py   # Game quality scoring
│   │   └── opening_classifier.py # Opening classification
│   ├── engine/
│   │   ├── __init__.py
│   │   ├── chess_bot.py        # AI training bot engine
│   │   ├── board_encoder.py    # Board state encoding
│   │   └── move_generator.py   # Legal move generation & ranking
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── best_games.py       # Best game identification
│   │   ├── pattern_mining.py   # Frequent pattern extraction
│   │   └── move_combos.py      # Best move combination teaching
│   ├── train.py                # Model training pipeline
│   └── evaluate.py             # Model evaluation pipeline
├── models/
│   └── saved/                  # Trained model checkpoints
├── results/
│   ├── figures/                # Visualizations & plots
│   ├── metrics/                # Model performance metrics
│   └── reports/                # Analysis reports
├── app/
│   ├── __init__.py
│   ├── chess_ui.py             # Human vs AI interface
│   └── templates/              # UI templates
├── configs/
│   └── config.yaml             # Hyperparameters & settings
├── tests/
│   ├── __init__.py
│   └── test_preprocessing.py
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md
```

## 🔬 ML Pipeline

### Phase 1: Data Engineering
- Load 14M games from HuggingFace (Parquet)
- Parse SAN/UCI/custom move notations
- Encode board states as tensors
- Feature engineering (piece positions, material balance, pawn structure, king safety)

### Phase 2: Pattern Recognition
- CNN/Transformer for board pattern recognition
- Opening classification (ECO codes)
- Middlegame tactical pattern detection
- Endgame pattern clustering

### Phase 3: Move Prediction
- Sequence model (Transformer/LSTM) for next-move prediction
- Attention-based move ranking
- Position evaluation scoring

### Phase 4: Game Quality Analysis
- Game brilliancy scoring algorithm
- Best games identification for White/Black
- Critical moment detection
- Move accuracy analysis

### Phase 5: AI Training Bot
- Interactive Human vs AI gameplay
- Adaptive difficulty based on user ELO
- Post-game analysis & teaching feedback
- Best move suggestions with explanations

## 🛠️ Tech Stack

- **Python 3.10+**
- **PyTorch** – Deep learning framework
- **python-chess** – Chess logic & board representation
- **HuggingFace Datasets** – Data loading
- **pandas / polars** – Data processing
- **scikit-learn** – Classical ML & evaluation
- **matplotlib / seaborn / plotly** – Visualization
- **Streamlit** – Interactive UI for AI bot

## Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/chess-pattern-recognition.git
cd chess-pattern-recognition

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download dataset
python src/data/loader.py

# Run EDA notebook
jupyter notebook notebooks/01_eda.ipynb
```

## Key Features

| Feature | Description | Model |
|---|---|---|
| Next Move Prediction | Predict most likely next move | Transformer |
| Pattern Recognition | Identify tactical/positional patterns | CNN + Attention |
| Best Game Finder | Score and rank games by quality | Gradient Boosting |
| Opening Classifier | Classify openings from move sequences | LSTM |
| AI Training Bot | Play against adaptive AI | Ensemble |

## License

MIT License

## Credits

- Dataset: [Angel Uriot - Chess Games](https://github.com/angeluriot/Chess_games)
- Chess Logic: [python-chess](https://python-chess.readthedocs.io/)
