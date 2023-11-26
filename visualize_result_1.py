import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_visualization_1(ela_path, arrest_path):
    # Define attribute names
    borough = "borough"
    year = "Year"
    meeting_learning_standards = "Level 3+4 %"
    arrest_count = "Arrest_Count"

    ela_df = pd.read_csv(ela_path)
    arrest_df = pd.read_csv(arrest_path)

    # Merge the two datasets on 'borough' and 'year'
    merged_df = pd.merge(ela_df, arrest_df, on=[borough, year])

    # Plotting the scatter plot with seaborn for hue and size support
    plt.figure(figsize=(12, 8))
    sns.scatterplot(
        data=merged_df,
        x=arrest_count,
        y=meeting_learning_standards,
        hue=borough,
        palette='Set1',
        size=year,  # Map the size to the 'year' attribute
        sizes=(50, 200),  # Define the size range for better visibility
        alpha=0.7
    )

    # Adding labels and title
    plt.xlabel('Arrest Count')
    plt.ylabel('% Meeting Learning Standards')
    plt.title('Arrest Count vs. Meet Learning Standards Percentage by Borough and Year')

    # Display the legend with adjusted position
    plt.legend(bbox_to_anchor=(1, 0.5), loc='center left')

    # Display the plot
    plt.grid(True)
    plt.show()


# ela_path = "ela_result.csv"
# arrest_path = "arrest_result.csv"
# plot_visualization_1(ela_path, arrest_path)