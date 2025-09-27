import streamlit as st
import subprocess
import sys
from pathlib import Path

def main():
    """Launch the Streamlit app"""
    
    # Get the current directory
    app_dir = Path(__file__).parent
    app_file = app_dir / "streamlit_app.py"
    
    print("🚀 Launching Dynamic Pricing Engine Demo...")
    print(f"📍 App location: {app_file}")
    print("🌐 The app will open in your default browser")
    print("⏹️  Press Ctrl+C to stop the app")
    
    # Launch Streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(app_file),
            "--server.headless", "false",
            "--server.port", "8501",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 App stopped!")
    except Exception as e:
        print(f"❌ Error launching app: {e}")

if __name__ == "__main__":
    main()
