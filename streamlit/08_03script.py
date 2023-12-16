# ""this demo will come after the presentation slides"".

# First let’s import the required libraries. I have already imported numpy and pandas. Now let’s import streamlit and matplotlib. {import streamlit as st and import matplotlib dot pyplot as plt}.
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


# Furthermore, we will create the dataframe with random numbers and set the column names. First we will define the column names. {col names is equal to a list and in the list lets add column1 column2 and column3}.
col_names = ["column1","column2","column3"]
# and now { data is equal to pd dot dataframe, and first we will create a numpy array with size 30 rows and 3 columns containing random numbers, and after that we will set the column names.}
data = pd.DataFrame(np.random.randint(30, size=(30, 3)),columns=col_names)


# Here we will create a line chart, for this we will use streamlits line chart function. { st dot line chart and pass the dataframe.} We can print the text in the application using inverted commas, {so above the chart let's print the chart name 'line graph'}. Let’s run this code and visualize the line chart. We created this chart in streamlit using only one line of code, which shows its ease of use.
'line graph:'
st.line_chart(data)


# In the next step, we will create a bar chart, for this we will use streamlits bar chart function. { st dot bar chart and pass the dataframe, and let’s print 'bar chart' above it.} Let’s run this code and visualize the bar chart.
'bar graph:'
st.bar_chart(data)


#  Streamlit doesn't have its own pie chart function but we can create a pie chart in matplotlib or other python visualization libraries and pass it in the streamlit's chart function for that library to display it in streamlit. To display the pie chart in streamlit, first let's create a simple data of animals and their heights to show in the pie chart. {animals is equal to cat, cow, and dog, and their heights is equal to 30, 150 and 80} in centimeter.
animals = ['cat', 'cow', 'dog']
heights  = [30, 150, 80]

# {here let’s print the chart name}. Now, let’s create a pie chart in matplotlib. {fig, ax is equal to plt.subplots, ax dot pie and first let’s pass the animal heights as first parameter and then let’s pass their names with keyword labels as second parameter}.
'pie chart:'
fig, ax = plt.subplots()
ax.pie(heights,labels=animals)
# Now, let’s pass the pie chart in streamlits 'pyplot' function. {st dot pyplot and pass the pie chart figure}. Let’s run this code and visualize the chart. So, in this demo we displayed three different types of charts in streamlit using less than 10 lines of code, which is really impressive.
st.pyplot(fig)
