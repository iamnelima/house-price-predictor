# House Price Prediction System

A machine learning system for predicting apartment rental prices in Kenya based on location, bedrooms, and bathrooms.

## Dataset
- **Source**: Kaggle - Apartment Prices in Kenya
- **Size**: 2,520 apartments across Kenya (mainly Nairobi and Mombasa)
- **Features**: Location, bedrooms, bathrooms, price

## Project Structure
```
house-price-predictor/
├── data/
│   ├── raw/              # Original dataset
│   └── processed/        # Cleaned data
├── notebooks/
│   ├── 01_data_exploration.ipynb    # Data analysis
│   └── 02_model_training.ipynb      # Model development
├── src/
│   ├── predictor.py      # Prediction engine
│   └── ...
├── models/               # Saved models
├── predict_price.py      # CLI interface
└── requirements.txt
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/iamnelima/house-price-predictor.git
cd house-price-predictor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the predictor:
```bash
python predict_price.py
```

## How It Works

The system predicts apartment prices by finding similar apartments in the dataset:
1. First tries exact matches (same beds, baths, location)
2. Falls back to similar apartments (same beds, baths, any location)
3. Uses bedroom averages as final fallback

## Example Usage
```
Number of bedrooms: 3
Number of bathrooms: 4
Location: Kileleshwa, Nairobi

Result: 70,000 KES/month (based on 130 similar apartments)
```

## Contributors
- [Your Name]
- [Collaborator names]

## License
MIT