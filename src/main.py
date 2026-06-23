import numpy as np
import pandas as pd

def run_cli_loop():
    # Native Python interactive user controller interface loop [cite: 51]
    while True:
        print("\n================================================")
        print("=== Welcome to StemMatch-Analytics CLI Engine ===")
        print("================================================")
        print("1. View Raw Dataset Profile")
        print("2. Run High-Performance Cohort Analytics")
        print("3. Exit Application")
        
        # Intercepting user prompt input selection arguments [cite: 51]
        choice = input("\nEnter your selection option (1-3): ").strip()
        
        if choice == "1":
            print("\n--- Ingesting Raw Dataset Matrix Table ---")
            try:
                df = pd.read_csv("data/raw_data.csv")
                print(df)
            except FileNotFoundError: # Defensive check wrapper [cite: 53]
                print("\n[ERROR] Core spreadsheet data matrix not found. [cite: 54]")
            except Exception as e:
                print("\n[ERROR] System Crash Defense: Data file is corrupted or structurally invalid.")
                print(f"Diagnostic Logs: {e}")                
        elif choice == "2":
            print("\n--- Executing Cellular Cohort Screening Filters ---")
            try:
                df = pd.read_csv("data/raw_data.csv")
                cancer_cell_mask = df["Cell_Type"] == "Cancer_Cell"
                print(df[cancer_cell_mask])
            except FileNotFoundError: # Defensive check wrapper [cite: 53]
                print("\n[ERROR] Core spreadsheet data matrix not found. [cite: 54]")
            except Exception as e:
                print("\n[ERROR] System Crash Defense: Data file is corrupted or structurally invalid.")
                print(f"Diagnostic Logs: {e}")    
        elif choice == "3":
            print("\nExiting StemMatch-Analytics. Systems turning off gracefully. Goodbye!")
            break
            
        else:
            print("\nInvalid argument selection option. Please pick 1, 2, or 3.")

# Entry gate execution controller
if __name__ == "__main__":
    run_cli_loop()


