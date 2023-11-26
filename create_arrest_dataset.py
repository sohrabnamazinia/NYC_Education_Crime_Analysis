from find_borough import find_borough
import pandas as pd
import os

def create_arrest_dataset(n=10000, last_year=2011):
    dataset_arrest_nyc_path = "NYPD_Arrests_Data__Historic__20231125.csv"
    arrest_date = "ARREST_DATE"
    year = "Year"
    borough = "borough"
    arrest_count = "Arrest_Count"
    output_file_path = f"arrest_result_{n}.csv"

    if os.path.exists(output_file_path):
        return output_file_path

    df = pd.read_csv(dataset_arrest_nyc_path)
    df_sampled = df.sample(n=n, random_state=42)
    df_sampled[arrest_date] = pd.to_datetime(df_sampled[arrest_date], format='%m/%d/%Y')
    df_sampled[year] = df_sampled[arrest_date].dt.year
    df_sampled[borough] = df_sampled.apply(lambda row: find_borough(row['Latitude'], row['Longitude']), axis=1)

    # Filter the DataFrame for years smaller or equal to last_year and exclude "Unknown" borough
    df_sampled = df_sampled[(df_sampled[year] <= last_year) & (df_sampled[borough] != "Unknown")]

    result_df = df_sampled.groupby([year, borough]).size().reset_index(name=arrest_count)

    # Save the result to arrest_result.csv
    result_df.to_csv(output_file_path, index=False)
    print("arrest_result.csv file generated successfully.")
    return output_file_path
