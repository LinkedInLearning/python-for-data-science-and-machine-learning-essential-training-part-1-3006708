# ""this demo will come after the presentation slides"".

#I have already imported the required libraries.
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt



# Earlier, we created the bar chart using streamlits bar chart function. Let’s create a bar chart in matplotlib and display it in streamlit. the bar chart we will create is a group bar chart comparing the heights and weights of the animals.
# First let’s define the data for the charts. {animals is equal to cat, cow, dog and goat, their heights in centimeter is equal to 30, 150, 80 and 60 and their weights in kilogram is equal to 5, 400, 40 and 50.}

animals = ['cat', 'cow', 'dog', 'goat']
heights = [30, 150, 80, 60]
weights = [5, 400, 40, 50]

# We will start by defining the subplots, {fig, ax is equals to plt dot subplots}. next we will define the label locations and the width of the bars. {x is equal to np dot arange, and in here we will pass the length of heights list.} this will create an array of length equal to heights list containing values from 1 to the length of the heights list, which will be the labels locations. after that lets set the width of the bars. {width is equal to 0.40}.

# now lets draw the first set of the group bars for the animals heights, {ax dot bar, and here we will first pass the position of the bars x-0.2, then we will pass the heights list, after that we will pass the width of the the bars and the color of the bars which let's set to red. let's copy and paste this line for the second set of the group bars of the animals weights. here we will change the bars positions to x+0.2, we will replace the heights list with weights list and we will change the color of the bars to orange.}

# next let's set the legends, {ax dot legend and here we will pass the labels height and weight.} now we wiil set the labels and their positions on the x axis. {ax dot set xticks and in it we will pass the array x, ax dot set xticklabels and here we will pass the list of animals names}. Now, let’s call the streamlits pyplot function to display the matplotlib chart in streamlit app. {st dot pyplot and we will pass the figure in it}.
# If we run this code block, then we can see that a beautiful bar chart is displayed on streamlit app. 

fig, ax = plt.subplots()

x = np.arange(len(heights))
width = 0.40

ax.bar(x-0.2, heights, width, color='red')
ax.bar(x+0.2, weights, width, color='orange')

ax.legend(["height", "weight"])
ax.set_xticks(x)
ax.set_xticklabels(animals)

st.pyplot(fig)


# Next let’s create an advance pie chart of some animals and their heights in centimeter. We will create the 
# pie chart using matplotlib library and then we will display it in streamlit. In the pie chart, the 
# slices will be ordered and plotted counter-clockwise. A wedge of a pie chart can be
# made to explode from the rest of the wedges of the pie chart using the explode parameter of the pie function.
# Let’s define how much we want to explode each wedge of the pie chart. {explode is equal to 0.2, 0.1, 0.1, 0.1}.
# Now, let’s create the plot. {plot pie comma ax is equal to plt dot subplots. ax dot pie and in this function first
# we will pass the heights of animals, then we will pass the explode list using the keyword explode. After that we 
# will pass the animals names. next we will pass is autopct as a parameter which enables you to display the 
# percentage values Using python string formatting. autopct is equal to, and let’s define its string format. The 
# next parameter is, shadow which is equal to true, which means we want to show the shadow of wedges in the chart. 
# In the next line let's write ax dot axis and let's pass the keyword equal in it}. Equal aspect ratio ensures that 
# pie is drawn as a circle. Now, let’s call the streamlits pyplot function to display the matplotlib chart in 
# streamlit app. {st dot pyplot and we will pass the plot in it}. Now we can view our pie chart by running this piece of code.

explode = [0.2, 0.1, 0.1, 0.1]
plot_pie, ax = plt.subplots()
ax.pie(heights, explode=explode,  labels=animals, autopct='%1.1f%%', shadow=True)
ax.axis('equal')
st.pyplot(plot_pie)
