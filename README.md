# NYC_Education_Crime_Analysis


## Table of Contents
- [Introduction](#introduction)
- [Datasets Description](#datasets-description)
- [Data Preparation & Join](#data-preparation-and-join)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Results](#results)


## Introduction
This project aims to visualize two distinct large datasets regarding education level and crime in New York City. The goal is to find out if there is any correlation between education level and crime rate in different boroughs and different years in NYC. If such a correlation exists, it might be concluded that education has been effective in reducing crime rates, and I have to make the best use of it for regions that lack sufficient hgih-quality educational systems. If there is no specific between the crime rate and education in different regions, one can conclude that education has not been effective enough to make the community aware of the consequences of crimes. Therefore, probably new methods are required to be adapted to the educational system of New York City.

## Datasets Description
Two datasets have been used in this project:

### The NYPD Arrests Data (Historic):
You can download this dataset via the following link:  
https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u  
This dataset is an extremely large set of arrest cases recorded in New York City. Each record has several attributes, but the following ones are important in this experiment:  
**Latitude, Longitude, ARREST_DATE**      
**Latitude, Longitude**: Two floating point numbers that represent the coordinate in which the arrest action took place.
**ARREST_DATE**: the exact date of the arrest case reported in the following format: MM/DD/YYYY

### The ELA Test Results by Grade - School Level - by Race-Ethnicity
You can download this dataset via the following link:  
https://data.cityofnewyork.us/Education/2006-2011-English-Language-Arts-ELA-Test-Results-b/g8e6-y4ax  
This dataset is a large set of New York City Results on the New York State English Language Arts (ELA) Tests, for grades 3 - 8. Each record has several attributes, but the following ones are important in this experiment:  
**DBN, Year, Level 3+4 %**    
**DBN**: Every school in New York City has a distinct DBN (District Borough Number), and it refers to that.
**Year**: The year in which the ELA test took place.
**Level 3+4 %**: Students taking ELA tests may score in levels 1, 2, 3, or 4. If they score in level 3, it means they meet the learning standards. In the case of scoring in level 4, it has the meaning of meeting learning standards in distinction. For a specific DBN, Level 3+4 basically means the total number of cases that scored in either Level 3 or 4. Finally, Level 3+4 % means the proportion of tests taken in a specific DBN that scores in level 3 or 4. It basically means what percentage of students in a DBN (school) meet the learning standards.


## Data Preparation and Join
I want to join the two datasets based on distinct values for the pair of Year and Borough so that finally I will have the following attributes:  
**Borough, Year, Arrest Count, % Meeting Learning Standards**  
However, obtaining appropriate values for these attributes requires several data preprocessing steps because the two dataset attributes in their raw format cannot be merged properly and meaningfully. Here the most important data preprocessing steps in this experiment have been mentioned: For the Arrest dataset, there is a column "ARREST_DATE" and it has the format "MM/DD/YYYY". Therefore, I can easily convert it to a new attribute called Year by considering only the "YYYY". For the Arrest dataset, there is a pair of Latitude and Longitude for each record. I have provided a method "Find_Borough" that gets a pair of (Latitude, Longitude) and computes what borough this coordinate belongs to. This has been implemented by considering approximate polygon boundaries for each borough. For the ELA dataset, each record has a DBN that refers to a unique school. I need the corresponding borough for that school, and that can be obtained by extracting the third character of a DBN. Here is how each borough in NYC has been abbreviated:  
    * K: Brooklyn (Kings County)
    * M: Manhattan
    * Q: Queens
    * R: The Bronx (originally "B" for the Bronx, but "R" was chosen to avoid confusion with Brooklyn)
    * X: Staten Island (Richmond County) To obtain the appropriate value for the Arrest Count attribute, I have done a "GROUP BY" operation on the arrest dataset to get the total number of arrest cases in each specific pair (year, borough). 


## Project Structure
In this section I have described each file/folder in the project:

- find_borough.py: given a pair of coordinates, it returns a character representing the corresponding borough for that coordinate.

- create_arrest_dataset.py: does all the preprocessing steps on the arrest dataset, and generates a resulting CSV file called "arrest_result_{n}.csv". "n" is a variable defined in "main.py" as an adjustable input parameter such that it represents how many random rows from "NYC_Arrest_Dataset" is going to be considered in this experiment. This is because the total number of records is over 5.5 million, hence, this can help to customize the visualization efficiently. The default value for n is 10000. 

- create_ela_dataset.py: does all the preprocessing steps on the ELA dataset, and generates a resulting CSV file called "ela_result.csv"

- visualize_result_1.py: plots a resulting visualization for the two generated CSV files "arrest_result_{n}.csv" and "ela_result.csv"

- visualize_result_2.py: plots another resulting visualization for the two generated CSV files "arrest_result_{n}.csv" and "ela_result.csv"

- visualize_result_3.py: plots another resulting visualization for the two generated CSV files "arrest_result_{n}.csv" and "ela_result.csv"

- main.py: The main and only file that simply needs to be run. It creates three distinct visualizations for this task. In this file, one can change n to any other desired value below 5.5 million. 

- Results (folder): It contains the three obtained visualizations for n = 10000. 

## Prerequisites
- Python 3.x (Preferably 3.9 or higher)
- (Optional) PostgreSQL 
- Having the following datasets downloaded:
    - https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u
    - https://data.cityofnewyork.us/Education/2006-2011-English-Language-Arts-ELA-Test-Results-b/g8e6-y4ax
    - Keep the name of the datasets as they are.
The following Python libraries using "pip install":
    - seaborn
    - pandas
    - matplotlib

## Usage
Follow these steps to run the code:
Download the two datasets via the links mentioned in the previous section, and place them in the root directory of this project.

2. Install the necessary libraries using the following commands:
<pre>
<code>
pip install pandas
pip install seaborn
pip install matplotlib
</code>
</pre>

3. (optional) Change "n" in "main.py" to your desired value.

4. Run main.py.


## Results
I decided to come up with the following three visualizations (Vis_1, Vis_2, and Vis_3). In this part I have explained and analyzed the visualizations:

**Data Items**:  
Each data item represents the situation of a distinct borough in a specific year

**Data marks**:  
Points

**Data Attributes**:   
Basically, we have 4 attributes:  
Year, Borough, % meeting learning standards, arrest count

**Attribute Types**:  
Borough: Categorical (R, K, M, Q, X)  
% Meeting learning standards: numerical (between 0 and 100)  
Arrest Count: numberical
Year: In this study, year is not practically a numerical value since it only has values 2006, 2007, 2008, 2009, 2010, and 2011. It can be considered as both Categorical and Ordinal (one can consider it as ordinal because it has a limited set of ordered values: 2006 - 2011). 

**Channels**:  
For Vis_1: 
Year => Size
Borough: color Hue
Arrest Count: Position (X-axis)
% Meeting Learning Standards: Position (Y-axis)

For Vis_2:
Year => Spatial region
Borough: color Hue
Arrest Count: Position (X-axis)
% Meeting Learning Standards: Position (Y-axis)

For Vis_3:
Year => Spatial region (horizontal)
Borough: Spatial region (vertical)
Arrest Count: Diverging Color Scheme #1
% Meeting Learning Standards: Diverging Color Scheme #2

I have analyzed the three famous principles for data visualization on this data:
1. Expressiveness principle
2. Effectiveness principle
3. Separability principle  

By the following explanation, it will be clarified why Vis_2 is better than Vis_1 after considering all the aspects.

### Effectiveness principle:

In visualizations_2, identity channels (spatial region & color hue) have been used for categorical attributes:
* Year 
* Borough  
Also, Magnitude channels (position on common scale -> X & Y axis) have been used for numerical attributes:  
* Arrest Count
* Meeting Learning Standards

Moreover, position on the common scale is the highest rank magnitude channel, and Spatial region and color hue are the highest-ranked channels among Identity ones. Therefore, **Visualization_2** completely satisfies the effectiveness principle**. 
In Visualization_1, the year has been considered as an ordered attribute and mapped with channel size. Although size/area is a magnitude channel, it is ranked fifth among all magnitude channels. Therefore, one can claim that **Vis_1 partially satisfies the effectiveness principle**.  
In Visualization_3, the two categorical attributes (year and borough) have been mapped with the spatial region along the horizontal and vertical scale, and arrest_count and level 3+4 % have been mapped to two distinct diverging color scales. Therefore **Visualization_3 completely satisfies the effectiveness principle**. 

### Expressiveness principle:

According to this principle, channels should match data characteristics, and the visualization should properly express the main goal of it. A chart is considered expressive if it can emphasize the important relationships among the attributes of interest for a given task. Here, since this chart clearly expresses the distribution of our desired attributes (education satisfaction level, arrest count) for boroughs in different years, we can claim it is expressive. 

Also, for the two numerical attributes (% meeting educational standards and arrest count) I have simply used magnitude channel position on a common scale for the X and Y axes that clearly match the characteristics of these attributes.

Moreover, for the two categorical attributes year and borough, I have used identity channels spatial region and color hue that also match the attribute characteristics. No matter whether we consider year as a categorical or ordered attribute, both charts express the "year" attribute properly. Since the number of different boroughs is 5, it is completely reasonable to use color hue for them because it makes them distinguishable.  
Therefore, in both visualizations, there is a total match between attributes and the selected channels. Hence, it can be concluded that **both visualizations satisfy the expressiveness principle**. However, in Visualization_3, if one wants to compare arrest_count and level 3+4 % for a specific pair of (borough, year), he/she should look at two different charts at the same time. Therefore, **visualizations_3 **satisfies** the expressiveness** principle**

### Separability principle:

This principle states that the channels that have been used in a visualization should be fully separable. In Vis_1, **Size** and **Color hue** have been used together, but these two channels have some interference and are not fully separable. **Therefore, Vis_1 does not satisfy the separability** principle**.   
In Vis_2, for each mini visualization generated for a different year, **Color hue** and **Position** channels have been used, and these two channels are fully separable. Therefore, it can be derived that **Visualization_2 fully satisfies the separability principle**. 
In visualization three, color and spatial region have been used that are fully separable. Therefore, **Visualization_3 fully satisfies the separability principle**. 

After considering all the details mentioned plus the principles described, it can be concluded that **Visualization_2 is better than Visualization_3 and visualization_3 is better than Visualization_1**.

By taking a deeper look at visualization_2, we can observe that in Queens the arrest rates are much lower, and also, the percentage of meeting learning standards in this area is so high. This behavior can also be observed relatively in Brooklyn, but with a lower magnitude. However, generally this pattern is not that significant among all because the education dataset belongs to a specific test (ELA) and cannot necessarily gurarantee that it can catch the educational level completely. Moreover, if we choose to run the code with a much larger n, this correlation might be much more significant. Also, one can observe that over time since 2006-2011 the ratios have not changed that much, and it can potentially mean that we have to adapt education in a more effective way to reduce the crime rate. However, this study is basically about the analysis of the distribution and correlation, not the causality because causality cannot be simply obtained by checking the results of a specific test.

![Visualization 1](./Results/Visualization_1.png)
![Visualization 2](./Results/Visualization_2.png)
![Visualization 3](./Results/Visualization_3.png)
