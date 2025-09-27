import os
import sys
from pathlib import Path
import importlib.util

def check_file_exists(filepath, description):
    """Check if a file exists and report status"""
    if Path(filepath).exists():
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} MISSING: {filepath}")
        return False

def check_import(module_name, description):
    """Check if a module can be imported"""
    try:
        importlib.import_module(module_name)
        print(f"✅ {description} imported successfully")
        return True
    except ImportError as e:
        print(f"❌ {description} import failed: {e}")
        return False

def check_data_files():
    """Check all required data files"""
    print("\n📊 CHECKING DATA FILES")
    print("-" * 30)
    
    checks = [
        ("../data/raw/hotel_bookings.csv", "Raw dataset"),
        ("../data/processed/hotel_bookings_processed.csv", "Processed dataset"),
        ("../src/models/demand_model.pkl", "Trained model"),
        ("../src/models/feature_columns.pkl", "Feature columns"),
    ]
    
    all_good = True
    for filepath, description in checks:
        if not check_file_exists(filepath, description):
            all_good = False
    
    return all_good

def check_dependencies():
    """Check all required Python packages"""
    print("\n📦 CHECKING DEPENDENCIES")
    print("-" * 30)
    
    dependencies = [
        ("streamlit", "Streamlit"),
        ("pandas", "Pandas"),
        ("numpy", "NumPy"),
        ("plotly", "Plotly"),
        ("sklearn", "Scikit-learn"),
        ("joblib", "Joblib")
    ]
    
    all_good = True
    for module, description in dependencies:
        if not check_import(module, description):
            all_good = False
    
    return all_good

def check_project_structure():
    """Check project structure"""
    print("\n📁 CHECKING PROJECT STRUCTURE")
    print("-" * 30)
    
    required_dirs = [
        "../data/raw/",
        "../data/processed/", 
        "../src/models/",
        "../notebooks/",
        "./",  # app directory
    ]
    
    all_good = True
    for directory in required_dirs:
        if Path(directory).exists():
            print(f"✅ Directory exists: {directory}")
        else:
            print(f"❌ Directory missing: {directory}")
            all_good = False
    
    return all_good

def test_pricing_engine():
    """Test if pricing engine can be imported and initialized"""
    print("\n🚀 TESTING PRICING ENGINE")
    print("-" * 30)
    
    try:
        # Add src to path
        sys.path.append('../src')
        from pricing_engine import DynamicPricingEngine
        
        # Try to initialize
        engine = DynamicPricingEngine(
            '../src/models/demand_model.pkl',
            '../src/models/feature_columns.pkl'
        )
        
        print("✅ Pricing engine initialized successfully")
        
        # Test with sample data
        import pandas as pd
        sample_features = pd.DataFrame({
            'lead_time': [45],
            'total_nights': [3],
            'total_guests': [2],
            'is_weekend': [0],
            'is_peak_season': [0],
            'day_of_week': [2],
            'arrival_date_month_num': [6],
            'is_repeated_guest': [0],
            'previous_cancellations': [0],
            'booking_changes': [0],
            'required_car_parking_spaces': [0],
            'total_of_special_requests': [1],
            'hotel_encoded': [1],
            'meal_encoded': [1],
            'market_segment_encoded': [1],
            'distribution_channel_encoded': [1],
            'reserved_room_type_encoded': [0],
            'deposit_type_encoded': [0],
            'customer_type_encoded': [0]
        })
        
        recommendation = engine.generate_pricing_recommendation(sample_features)
        
        if 'recommended_price' in recommendation:
            print(f"✅ Test recommendation: ${recommendation['recommended_price']:.2f}")
            return True
        else:
            print("❌ Recommendation failed")
            return False
            
    except Exception as e:
        print(f"❌ Pricing engine test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 DYNAMIC PRICING APP - PRE-LAUNCH TESTING")
    print("=" * 50)
    
    tests = [
        ("Project Structure", check_project_structure),
        ("Dependencies", check_dependencies), 
        ("Data Files", check_data_files),
        ("Pricing Engine", test_pricing_engine)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🔍 Testing: {test_name}")
        results.append(test_func())
    
    print("\n" + "=" * 50)
    print("📋 TESTING SUMMARY")
    print("-" * 20)
    
    for i, (test_name, _) in enumerate(tests):
        status = "PASS" if results[i] else "FAIL"
        emoji = "✅" if results[i] else "❌"
        print(f"{emoji} {test_name}: {status}")
    
    all_passed = all(results)
    
    if all_passed:
        print("\n🎉 ALL TESTS PASSED! Your app is ready to launch!")
        print("🚀 Run: streamlit run streamlit_app.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues before launching.")
        print("💡 Check the error messages above for guidance.")
    
    return all_passed

if __name__ == "__main__":
    main()
