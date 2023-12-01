import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_visualization_3(ela_path, arrest_path):
    # Define attribute names
    borough = "borough"
    year = "Year"

    ela_df = pd.read_csv(ela_path)
    arrest_df = pd.read_csv(arrest_path)

    # Merge the two datasets on 'borough' and 'year'
    df = pd.merge(ela_df, arrest_df, on=[borough, year])

    df.to_csv("final_output.csv", index=False)
    

        # Pivot the DataFrame to create matrices for the heatmaps
    heatmap_data_percent = df.pivot(index='borough', columns='Year', values='Level 3+4 %')
    heatmap_data_count = df.pivot(index='borough', columns='Year', values='Arrest_Count')

    # Create subplots for a side-by-side comparison
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))

    # Create the heatmap for Level 3+4 %
    sns.heatmap(heatmap_data_percent, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=.5, ax=ax[0])
    ax[0].set_title('Level 3+4 % by Borough and Year')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Borough')

    # Create the heatmap for Arrest_Count with a diverging color map
    sns.heatmap(heatmap_data_count, annot=True, cmap='RdYlGn_r', fmt="d", linewidths=.5, ax=ax[1])
    ax[1].set_title('Arrest Count by Borough and Year')
    ax[1].set_xlabel('Year')
    ax[1].set_ylabel('Borough')

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()
