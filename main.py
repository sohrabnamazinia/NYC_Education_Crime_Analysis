from create_ela_dataset import create_ela_dataset
from create_arrest_dataset import create_arrest_dataset
from visualize_result_1 import plot_visualization_1
from visualize_result_2 import plot_visualization_2
from visualize_result_3 import plot_visualization_3

# set input for the number of considered arrest records
n = 10000

ela_file = create_ela_dataset()
arrest_file = create_arrest_dataset(n=n)
plot_visualization_1(ela_path=ela_file, arrest_path=arrest_file)
plot_visualization_2(ela_path=ela_file, arrest_path=arrest_file)
plot_visualization_3(ela_path=ela_file, arrest_path=arrest_file)