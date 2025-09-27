import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "src" / "models"

# Model paths
DEMAND_MODEL_PATH = MODELS_DIR / "demand_model.pkl"
FEATURE_COLS_PATH = MODELS_DIR / "feature_columns.pkl"

# Data paths
RAW_DATA_PATH = DATA_DIR / "raw" / "hotel_bookings.csv"
PROCESSED_DATA_PATH = DATA_DIR / "processed" / "hotel_bookings_processed.csv"

# App configuration
APP_CONFIG = {
    "title": "Dynamic Pricing Engine",
    "description": "AI-powered hotel pricing optimization",
    "max_sample_size": 1000,
    "default_constraints": {
        "min_price": 30,
        "max_price": 800,
        "cost_per_night": 40
    }
}

# Styling
CUSTOM_CSS = """
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .insight-box {
        border-left: 5px solid #1f77b4;
        padding-left: 1rem;
        margin: 1rem 0;
        background-color: #f8f9fa;
        border-radius: 0 0.5rem 0.5rem 0;
    }
</style>
"""
