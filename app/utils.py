import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def create_feature_vector(hotel_type, lead_time, total_nights, total_guests, 
                         arrival_month, is_weekend, market_segment, 
                         customer_type, room_type):
    """Create feature vector from user inputs"""
    
    month_mapping = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    
    features = pd.DataFrame({
        'lead_time': [lead_time],
        'total_nights': [total_nights],
        'total_guests': [total_guests],
        'is_weekend': [1 if is_weekend else 0],
        'is_peak_season': [1 if month_mapping[arrival_month] in [6, 7, 8, 12] else 0],
        'day_of_week': [5 if is_weekend else 2],
        'arrival_date_month_num': [month_mapping[arrival_month]],
        'is_repeated_guest': [0],
        'previous_cancellations': [0],
        'booking_changes': [0],
        'required_car_parking_spaces': [0],
        'total_of_special_requests': [1],
        'hotel_encoded': [1 if hotel_type == "Resort Hotel" else 0],
        'meal_encoded': [1],
        'market_segment_encoded': [1],
        'distribution_channel_encoded': [1],
        'reserved_room_type_encoded': [ord(room_type) - ord('A')],
        'deposit_type_encoded': [0],
        'customer_type_encoded': [0]
    })
    
    return features

def create_price_sensitivity_chart(price_range, revenues, demands, optimal_price):
    """Create price sensitivity analysis chart"""
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=['Revenue vs Price', 'Demand vs Price'],
        specs=[[{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    fig.add_trace(
        go.Scatter(x=price_range, y=revenues, mode='lines+markers',
                  name='Revenue', line=dict(color='blue')),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(x=price_range, y=demands, mode='lines+markers',
                  name='Demand', line=dict(color='red')),
        row=1, col=2
    )
    
    # Highlight optimal price
    fig.add_vline(x=optimal_price, line_dash="dash", line_color="green", 
                 annotation_text="Optimal Price")
    
    fig.update_layout(height=400, showlegend=False)
    return fig

def format_currency(value):
    """Format value as currency"""
    return f"${value:,.2f}"

def format_percentage(value):
    """Format value as percentage"""
    return f"{value:.1f}%"

@st.cache_data
def load_sample_data(file_path):
    """Load and cache sample data"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(f"Data file not found: {file_path}")
        return None

def create_strategy_comparison_chart(strategy_results):
    """Create strategy comparison visualization"""
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=['Average Price', 'Total Revenue', 'Total Profit', 'Profit Margin'],
        specs=[[{"type": "bar"}, {"type": "bar"}],
               [{"type": "bar"}, {"type": "bar"}]]
    )
    
    strategies = list(strategy_results.keys())
    strategy_names = [s.replace('_', ' ').title() for s in strategies]
    
    # Average Price
    avg_prices = [strategy_results[s]['avg_price'] for s in strategies]
    fig.add_trace(go.Bar(x=strategy_names, y=avg_prices, 
                        marker_color='lightblue'), row=1, col=1)
    
    # Total Revenue
    total_revenues = [strategy_results[s]['total_revenue'] for s in strategies]
    fig.add_trace(go.Bar(x=strategy_names, y=total_revenues, 
                        marker_color='green'), row=1, col=2)
    
    # Total Profit
    total_profits = [strategy_results[s]['total_profit'] for s in strategies]
    fig.add_trace(go.Bar(x=strategy_names, y=total_profits, 
                        marker_color='gold'), row=2, col=1)
    
    # Profit Margin
    profit_margins = [strategy_results[s]['avg_margin'] for s in strategies]
    fig.add_trace(go.Bar(x=strategy_names, y=profit_margins, 
                        marker_color='red'), row=2, col=2)
    
    fig.update_layout(height=600, showlegend=False)
    fig.update_xaxes(tickangle=45)
    
    return fig
