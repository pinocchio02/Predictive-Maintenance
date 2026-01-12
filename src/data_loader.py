import pandas as pd
import os

def load_data(filepath):
    """
    Loads the NASA data and calculates RUL.
    """
    # Define columns
    index_names = ['unit_nr', 'time_cycles']
    setting_names = ['setting_1', 'setting_2', 'setting_3']
    sensor_names = ['s_{}'.format(i) for i in range(1, 22)] 
    col_names = index_names + setting_names + sensor_names

    # Load data using the passed filepath variable
    df = pd.read_csv(filepath, sep='\s+', header=None, names=col_names)

    # Calculate RUL
    max_cycle = df.groupby('unit_nr')['time_cycles'].max()
    result_frame = df.merge(max_cycle.to_frame(name='max_cycle'), left_on='unit_nr', right_index=True)
    result_frame['RUL'] = result_frame['max_cycle'] - result_frame['time_cycles']
    result_frame.drop('max_cycle', axis=1, inplace=True)
    
    return result_frame

if __name__ == "__main__":
    # Get the directory where THIS script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)

    # We check two likely places for the file:
    # 1. Root/CMaps/train_FD001.txt (Your likely structure)
    # 2. Root/data/CMaps/train_FD001.txt (Standard structure)
    
    path_option_1 = os.path.join(project_root, 'CMaps', 'train_FD001.txt')
    path_option_2 = os.path.join(project_root, 'data', 'CMaps', 'train_FD001.txt')
    
    # Pick the path that actually exists
    if os.path.exists(path_option_1):
        test_path = path_option_1
    elif os.path.exists(path_option_2):
        test_path = path_option_2
    else:
        # If neither works, default to option 1 so we can see the error path
        test_path = path_option_1 

    print(f"Checking for file at: {test_path}")

    if os.path.exists(test_path):
        df = load_data(test_path)
        print("✅ Success! Data loaded.")
        print(f"Dataset Shape: {df.shape}")
        print("First 5 rows of RUL:")
        print(df[['unit_nr', 'time_cycles', 'RUL']].head())
    else:
        print(f"❌ Error: File NOT found.")
        print(f"I looked in: {path_option_1}")
        print(f"And in: {path_option_2}")
        print(f"Root folder contents: {os.listdir(project_root)}")