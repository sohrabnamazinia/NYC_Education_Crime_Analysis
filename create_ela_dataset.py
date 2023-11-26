import pandas as pd

def create_ela_dataset():
    dataset_ela_school_level_path = "2006_-_2011_English_Language_Arts__ELA__Test_Results_by_Grade_-_School_level_-_by_Race-Ethnicity_20231125.csv"

    # Column names and output path
    borough_column = 'borough'
    year_column = 'Year'
    level_percentage_column = 'Level 3+4 %'
    output_file_path = "ela_result.csv"

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(dataset_ela_school_level_path)

    # Extract borough from the first column (DBN)
    df[borough_column] = df['DBN'].str[2]  # Assuming the borough letter is always in the third position

    # Select relevant columns
    df = df[[borough_column, year_column, level_percentage_column]]

    # Check if 'level 3+4%' column is already numeric
    if pd.api.types.is_numeric_dtype(df[level_percentage_column]):
        print(f"{level_percentage_column} column is already numeric.")
    else:
        # Convert 'level 3+4%' column to numeric (assuming it's a percentage string)
        df[level_percentage_column] = pd.to_numeric(df[level_percentage_column].str.rstrip('%'), errors='coerce')

    # Group by 'borough' and 'year' and calculate the rounded average for 'level 3+4%'
    result_df = df.groupby([borough_column, year_column])[level_percentage_column].mean().round(2).reset_index()

    # Save the result to ela_result.csv
    result_df.to_csv(output_file_path, index=False)
    print("ela_result.csv created successfully.")
    return output_file_path