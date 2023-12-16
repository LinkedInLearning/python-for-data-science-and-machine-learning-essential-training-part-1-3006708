# ""this demo will come after the presentation slides"".

# I have already imported the required libraries.
import time
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# Next let’s create an advance line chart, which will grow over time. We will use line chart's add rows function 
# to grow the chart. First, let's generate a numpy array with a single random value. {rows is equal to np dot random 
# dot randn and here we will pass the shape of array 1 cross 1}
rows = np.random.randn(1, 1)
# {Now let’s print the chart name}. Next, let’s create the line chart. {chart is equal to st dot line chart, we will 
# pass the array in it}
'Growing Line chart:'
chart = st.line_chart(rows)

# After that, we will create a loop and we will grow the line chart in the loop. {for i in range 1 to 100}
# Next, let’s generate a random number and append it to the array, then we will pass this array to add rows 
# function. {new rows is equal to rows[0] plus np dot random dot randn and pass the shape of the array}.
# Now, let’s add this array to the chart. {chart dot add rows and let’s pass the array 'new rows'}.
# {After that we will set the rows equal to new rows and then we will call time dot sleep to stop the 
# loop for 5 milliseconds}. So what we are doing here is that we are generating a random number and adding
# it to the chart after 5 milliseconds. We can run this code and view the graph growing over time.
for i in range (1, 100):
	new_rows = rows[0] + np.random.randn(1, 1)
	chart.add_rows(new_rows)
	rows = new_rows
	time.sleep(0.05)


# Streamlit gives us the flexibility of creating graphs in any other python visualization library and show them in 
# streamlit. So, let’s create a line chart using matplotlib library. First, we will create an array with random 
# values. {values is equal to np dot random dot rand and the length of the array will be 10}. Next, let’s plot the 
# values with matplotlib. {first let’s print the chart name}. Now let's create the chart. {fig, ax is equal to plt 
# dot subplots, ax dot plot and let's pass the values array in it}. Now, let's pass the line chart in streamlits 
# 'pyplot' function. {st dot pyplot and pass the figure}. Let's run this code and visualize the chart.
values = np.random.rand(10)
'matplotlib Line chart:'
fig, ax = plt.subplots()
ax.plot(values)
st.pyplot(fig)
