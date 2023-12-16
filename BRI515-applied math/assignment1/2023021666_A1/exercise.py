# THIS FILE FOR CALCULATING MEAN AND STANDARD DEVIATIONS OF EXERCISE, WEIGHT, HEART RATE VARIABLES OF PARTICIPANTS
# AND PRINTING THE PLOTS AND MAKING COMPARISONS
#FIRST PLOT:
# The first figure consists of three subplots, each representing a variable (Heart rate, Weight, Exercise). Scatter plots used to illustrate the distribution of data points for each variable.
# Dots represent the original data points, red horizontal lines represent the mean, and blue dashed lines represent the mean ± standard deviation.
# Custom ticks are added to the x-axis for better visualization.

#SECOND PLOT
# The second figure also consists of three subplots, each representing a comparison within variables.

# Variable mean and standard Deviation results also printed for each variable
# NOTE: before starting to write code, I installed numpy module in terminal using "pip install numpy" and "pip install matplotlib/python -m pip install --upgrade pip"

import matplotlib.pyplot as plt
import numpy as np


# Writing data
# np.array CAN NOT include mixed data !only numerical or title
data = np.array([
    [72, 61, 3.2],
    [82, 91, 3.5],
    [69, 71, 7.1],
    [82, 67, 2.4],
    [75, 77, 1.2],
    [56, 80, 8.5],
    [93, 101, 0.1],
    [81, 75, 3],
    [75, 55, 2.7],
    [59, 65, 3.1],
    [95, 79, 1.5],
    [66, 62, 6.3],
    [80, 75, 2],
    [65, 81, 6.5],
    [69, 57, 4.8]
])

# note to myself: writing data columns as different arrays (heartrate=.., weight=...) may be more easy and useful.

# defining variables
variables = ["Heart rate(bpm)", "Weight (kg)", "Exercise (hrs)"]

# assigning variable titles TO columns

variables_to_columns = {} # creating dictionary to adding variables names and their corresponding indexes
for i in range(len(variables)):
    variable = variables[i] # retrieving variable names in current index
    variables_to_columns[variable] = i # adding variable names to their column index


# calculating the mean and standard deviation
# it will give mean_values and std_values for each column

def meanSTD(data):

    # Calculating mean and standard deviation along axis 0 (starting from first column)
    mean_values = np.mean(data, axis=0)
    std_values = np.std(data, axis=0)


    # Printing results for each variable / taking one input and return two output for each variable
    for variable in variables:
        print(f"Variable: {variable}")
        print(f"Mean: {mean_values[variables_to_columns[variable]]}, Standard Deviation: {std_values[variables_to_columns[variable]]}\n")
# why I use [variables_to_columns[variable] like this= because that dictionary has both data points and titles
    return mean_values, std_values


# assigning values to variables by calling meanSTD function
mean_values, std_values = meanSTD(data)

# plt.subplots function to create a new figure
# its more convenient to create multiple plots in a single figure

fig, ax = plt.subplots(3, 1, figsize=(8, 10)) # number of rows-columns so 3x1 grid, 8 inc=width and 10 inch=height

# To iterate over each variable in the first row of the dataset
# note: enumerate() for keeping track of the index (position) of an element in an iterable while iterating over it.
for i, variable in enumerate(variables):

    # Retrieving data values for all participants from dataset "data" (var_data: variable data which includes all participants)
    var_data = np.array(data[:, variables_to_columns[variable]], dtype=float) # starting from the first row

    # Define a color for each variable
    colors = ['c', 'm', 'g'] # c=cyan ,m=magenta ,g=green

    # Plotting the original data (as a scatter plot) with different colors
    ax[i].scatter(np.arange(1, len(var_data) +1 ), var_data, label=variable, color=colors[i])

    # Adding ticks to the x-axis
    ax[i].set_xticks(np.arange(1, len(var_data) + 1)) # 1 to length of var_data to tick every participant

    # Setting custom ticks for the y-axis for each variable
    if variable == "Exercise (hrs)":
        ax[i].set_yticks([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5])
    elif variable == "Weight (kg)":
        ax[i].set_yticks([55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
    elif variable == "Heart rate(bpm)":
        ax[i].set_yticks([55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

    # Plotting the mean
    # axhline() used for creating horizontal lines
    ax[i].axhline(mean_values[variables_to_columns[variable]], color='r', linestyle='-', label='Mean') # r=red

    # Plotting the standard deviation around the mean
    ax[i].axhline(mean_values[variables_to_columns[variable]] + std_values[variables_to_columns[variable]], color='b', linestyle='--', label='Mean + STD')
    ax[i].axhline(mean_values[variables_to_columns[variable]] - std_values[variables_to_columns[variable]], color='b', linestyle='--', label='Mean - STD')
    # b=blue

    # Adding labels and title
    ax[i].set_xlabel('Participants')
    ax[i].set_ylabel(variable)
    ax[i].set_title(f'Variable: {variable}')

    # Adding legend and arranging its location
    ax[i].legend(loc=(1.05, 0.5))

# Using for automatic adjust the spacing between subplots:
plt.tight_layout()

# saving the figure as analysis.png
plt.savefig('analysis.png')

# Show the plot
plt.show()
                                     # CREATING SECOND FIGURE:


# 1x3, 16 inc=width and 5 inch=height
fig2, ax2 = plt.subplots(1, 3, figsize=(16, 5))

# Scatter plot heart rate against weight
ax2[0].scatter(data[:, 0], data[:, 1], color='r') # data[:, 0] for heart rates (column 0) - data[:, 1] represents the weights with FIRST ROW/ title
#r=red

ax2[0].set_xlabel('Heart Rate (bpm)')
ax2[0].set_ylabel('Weight (kg)')
ax2[0].set_title('Heart Rate vs Weight')
ax2[0].set_xticks([55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) # custom ticks for heartrate
ax2[0].set_yticks([55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]) # custom ticks for weight

# adding regression line
# The polyfit() function uses: the x value, the y value, and 1. (the degree of the polynomial fit)
a, b = np.polyfit(data[:, 0], data[:, 1], 1)

# Plotting the regression line
# plt.plot(x, m*x + b) - wrote what is in x-axis
ax2[0].plot(data[:, 0], a * data[:, 0] + b, color='c')

# Scatter plot heart rate against exercise rate
ax2[1].scatter(data[:, 0], data[:, 2], color='b') # data[:, 0] for heart rates - data[:, 2] represents the exercise rate with FIRST ROW
#b=blue
ax2[1].set_xlabel('Heart Rate (bpm)')
ax2[1].set_ylabel('Exercise Rate (hrs)')
ax2[1].set_title('Heart Rate vs Exercise Rate')
ax2[1].set_xticks([55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) # custom ticks for heartrate
ax2[1].set_yticks([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5]) # custom ticks for exercise

# adding regression line
a, b = np.polyfit(data[:, 0], data[:, 2], 1)

# Plotting the regression line
ax2[1].plot(data[:, 0], a * data[:, 0] + b, color='c')

# Scatter plot weight against exercise rate
ax2[2].scatter(data[:, 1], data[:, 2], color='g') # data[:, 1] for weight - data[:, 2] represents the exercise rate with FIRST ROW
#g=green
ax2[2].set_xlabel('Weight (kg)')
ax2[2].set_ylabel('Exercise Rate (hrs)')
ax2[2].set_title('Weight vs Exercise Rate')
ax2[2].set_xticks([55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]) # custom ticks for weight
ax2[2].set_yticks([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5]) # custom ticks for exercise

# adding regression line
a, b = np.polyfit(data[:, 1], data[:, 2], 1)

# Plotting the regression line
ax2[2].plot(data[:, 1], a * data[:, 1] + b, color='c')

# Using for automatic adjust the spacing between subplots:
plt.tight_layout()

# saving the figure as analysis2.png
plt.savefig('analysis2.png')

# Showing the second plot
plt.show()

'''
COMMENTS FOR PLOTS
     FIRST PLOT SHOWS:
 HeartRate(bpm) has a mean of 74.6 and a standard deviation of 10.83 with minimum 96; maximum 95 data results
 Weight(kg) has a mean of 73.13 and a standard deviation of 12.19 with minimum 55; maximum 101 data results
 Exercise(hrs) shows results with a mean of 3.73 and a standard deviation of 2.33 with minimum 0.1; maximum 8.5 data results
 The standard deviations of the variables, heart rate and weight, indicate a more homogeneous trend in terms of the variability of individual heart rate and weight data around their means. Conversely, the variable 'exercise' shows a higher standard deviation, implying a more heterogeneous trend toward its mean which is indicative of a more diverse distribution.


    SECOND PLOT SHOWS:
There is no  linear relationship among the three comparisons: heart rate-weight, heart rate-exercise, and weight-exercise. Interestingly, a decreasing trend is observed across the data points between 70 to 80 when examining the x-axis in all three comparisons.
In the heart rate-weight comparison, an increasing trend is evident. 
Conversely, there is a decreasing trend in the heart rate-exercise comparison and a slight decreasing trend in the weight-exercise comparison.
Even though we don't know about participants age, gender and stress rate (which is also influences variables like weight and heart rate) and also small amount of participants, it can be observed that weight has a positive correlation with heart rate, while exercise exhibits a negative correlation. (further analyses must done to be sure)
However, a slight decrease is noted in weight when exercise hours are shortened. Given the high standard deviation in exercise,  we may conclude that individual differences may play a more significant role in exercise duration than weight  impacting exercise hours.    
'''


