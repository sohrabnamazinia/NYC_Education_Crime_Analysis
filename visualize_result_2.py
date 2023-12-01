import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_visualization_2(ela_path, arrest_path):
    # Load CSV files into pandas DataFrames
    ela_df = pd.read_csv(ela_path)
    arrest_df = pd.read_csv(arrest_path)

    # Merge the two datasets based on 'borough' and 'Year'
    merged_df = pd.merge(ela_df, arrest_df, on=['borough', 'Year'])

    merged_df.to_csv("final_output.csv", index=False)

    # Get unique years for separate mini scatter plots
    unique_years = merged_df['Year'].unique()

    # Set up subplots
    num_plots = len(unique_years)
    num_cols = 2  # Assuming you want 2 subplots per row, you can adjust as needed
    num_rows = (num_plots + 1) // num_cols

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))

    # Flatten the 2D array of axes for easier iteration
    axes = axes.flatten()

    for i, year in enumerate(unique_years):
        # Filter data for the current year
        year_data = merged_df[merged_df['Year'] == year]

        # Scatter plot for the current year
        sns.scatterplot(x='Arrest_Count', y='Level 3+4 %', hue='borough', data=year_data, ax=axes[i])
        axes[i].set_title(f'Scatter Plot for {year}')
        axes[i].set_xlabel('Arrest Count')
        axes[i].set_ylabel('Level 3+4 %')

    # Adjust layout to prevent overlapping
    plt.tight_layout()
    plt.show()

# Example usage
# ela_path = "ela_result.csv"
# arrest_path = "arrest_result.csv"
# plot_visualization_2(ela_path, arrest_path)
