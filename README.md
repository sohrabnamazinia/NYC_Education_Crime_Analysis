# NYC_Education_Crime_Analysis


## Table of Contents
- [Introduction](#introduction)
- [Datasets_Description](#datasets)
- [Data_Preparation](#data_preparation)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Example](#example)


## Introduction
This project aims to visualize two distinct large datasets regarding education level and crime in New York City. The goal is to find out if there is any correlation between education level and crime rate in different boroughs and different years in NYC. If such a correlation exists, it might be concluded that education has been edffective in reducing crime rates, and we have to make best use of it for regions that lack sufficient hgih-quality educational system. If there is no specific between crime rate and education indifferent regions, one can conclude that education has not been effective enough to make the community aware of the consequences of crimes. Therefore, probably new methods are requrired to be adapted in the educational system of the New York City.

## Datasets Description
Two datasets have been used in this project:

### The NYPD Arrests Data (Historic):
You can download this dataset via the following link:
https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u
This dataset is a extremely large set of arrest cases recorded in New York City. Each record, has several attributes, but the following ones are important in this experiment:
Latitude, Longitude, ARREST_DATE
Latitude, Longitude: Two floating point numbers that represent the coordinate in which the arrest action took place.
ARREST_DATE: the exact date of the arrest case reported in the following format: MM/DD/YYYY

### The ELA Test Results by Grade - School level - by Race-Ethnicity
You can download this dataset via the following link:
https://data.cityofnewyork.us/Education/2006-2011-English-Language-Arts-ELA-Test-Results-b/g8e6-y4ax
This dataset is a large set of New York City Results on the New York State English Language Arts (ELA) Tests, for grades 3 - 8. Each record, has several attributes, but the following ones are important in this experiment:
DBN, Year, Level 3+4 %
DBN: Every school in New York City has a distinct DBN (District Borough Number), and it refers to that
Year: The year which the ELA test took place
3+4 %: Students taking ELA test may score in level 1, 2, 3, or 4. If they score in level 3, it means they meet the learning standards. In case of scoring in level 4, it has the meaning of meeting learning standards in distinction. For a spcific DBN, Level 3+4 basically means the total number of cases that scored in either level 3 or 4. Finally, Level 3+4 % means the proportion of test takes in a specific DBN that score in level 3 or 4. It basically means what percentage of students in a DBN (school) meet the learning standards.


## Data Preparation


## Project Structure
This project has been implemented in a modular structure, and the RL agents have been defined once to be used for the both use cases. The python files serve different goals in the project, and the generated CSV files are the results of the implemented tests. Here is a high-level overview of the different parts/files of the project:

- The agents folder consists of the QLearning and Deep Agents. 

- The env folder has two important files: 
"gridworld.py" and "query_refine.py"
These two files are basically the environments of our two use cases. We have used/inherited Environment of "Gym" library to define all the details of our use cases over that. 
The other files in the env folder serve different functionalities. For example, connecting to the database to get amazon reviews, connecting to OpenAI LLM to interact  with gpt-3.5 for the query-refine use case, generating random policies, embedding text to vector and compute cosine similarity between vectors. 

- Python files starting with the word "train_" are basically the implementation of the train process of different agents for the two use cases. 

- Files having a "npy" extension are just the Q-Tables of the training instances stored after the training was done. 

- "pkl" extension files are also trained deep agents that have been stored. 

- Python files starting with "inference_" are used to implement the inference phase of an agent. They are helpful since we can use them to make sure an agent has been trained properly.

- Python files starting with "heuristic" are the implementation of the "greedy-k" algorithm. One of the proposed methods in our research work. 

- Python files starting with "DAG" represent the DAG data structure that we use as a core concept in our proposed algorithm. For each instance of training a DAG is also created that consists of all the transitions occured during the training. The corresponding DAGs of different training instances are unioned together to get a final DAG on which our pruning algorithm is based on.

- Pyhton files starting with "pruning" contain our core pruning algorithm called "ExNonZeroDiscount". 

- Python files starting with "test_" are all the the experiments that we have performed on the two use cases for different scenarios. These are the files that we can run.

- "utilities.py" is a unique file containing a set of functions to plot different experiment results based on their csv files. 


## Getting Started
To run this project, you need to have Python3 installed (Preferrebly Python3.9 or higher versions). Also, you need to have some libraries installed using "pip install" command. 

The files containing the "test" word in the beginning are the experiments of the project. You can run any of them to see their corresponding results. After you run a test file, some information might be printed about the execution process in the terminal. When the test is done, a csv file including the test results is created in the root directory of the project. Also, a window pops up which plots the resulting graphs of the experiment if applicable. 

Also, since the Query Refinement use case uses amazon reviews, we have stored a subset of reviews of the whole amazon dataset reviews in a csv file, and we read from that csv file in the code. However, if one wants to get the whole dataset and work on that, must have PostgreSQL installed, load "amazon reviews" dataset in their PostreSQL server, and also delete the "review.csv" file. Because if this file exists, the code will not read from the database, but if it doesn't, our code will get the reviews from the amazon database. You can also specify more details about that (number of desired reviews, etc) in the code.

Finally, as another optional step, if you want to have some of the generated figures stored on an online environment, you can create an account on WandB website, and use "wandb login" command in your terminal to login to your account. Then, you can uncomment the lines of the code that are related to WandB so that the figures get stored on your WandB account. 

### Prerequisites
- Python 3.x (Preferrebly 3.9 or higher)
- (Optional) PostgreSQL 
- (Optional) Load Amazon reviews dataset in PostgreSQL. Here is the link to the amazon reviews dataset:
    - https://www.dropbox.com/s/j04z1gx4tt51q20/intex_amazon.backup?dl=0
    - The daabase must be called "amazon_reviews"
- The following python libraries using "pip install":
    - networkx
    - matplotlib
    - numpy
    - torch
    - stable-baselines3
    - pandas
    - transformers
    - scikit-learn
    - gym
    - wandb 
    - psycopg2
    - psutil


### Usage

1. Clone the repository:
<pre>
<code>
    git clone https://github.com/PolicyReusablityInRL/Policy-Reusablity.git
</code>
</pre>
2. Install the following libraries using pip:
<pre>
<code>
    pip install matplotlib
    pip install numpy
    pip install torch
    pip install pandas
    pip install transformers
    pip install stable-baselines3
    pip install scikit-learn
    pip install gym
    pip install wandb
    pip install psycopg2
    pip install networkx
    pip install psutil
</code>
</pre>
3. **(Optional)** Setup the database if you want to work on more reviews as explained in the previous section.

4. **(Optional)**: if you want to have some figures/plots stored on an online envrionment, you can create a [WandB account](https://wandb.ai/site), login to your account using terminal and uncomment any wandb commands in the code that you want to execute and store their corresponding figures. Here is the command you need to run in your terminal after you create an account on WandB website:
<pre>
<code>
    wandb login
</code>
</pre>

5. Run any test file that you want to see its results. A test file's name starts with "test_". Before you run a test file, you can search "#input" in the file, and then you will see the already default parameters set to some values. You can change these input parameters. These are the setting parameters of the tests (For example number of different test cases, etc). 

### Example

After the setup process is all done, we can run a sample test file like "test_recall_deep.py". 

First we can modify the input parameters if we want (not necessary):
![Test_Recall_Deep_Input](./sample_images/Test_Recall_Deep_Input.png)

After running the file, here is the generated output Figure and CSV file:

![Test_Recall_Deep_CSV](./results/Visualization_1.png)
![Test_Recall_Deep_Figure](./results/Visualization_2.png)
