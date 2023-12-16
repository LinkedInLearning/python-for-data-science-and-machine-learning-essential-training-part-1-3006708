# ""this demo will come after the presentation slides"".

# I have imported the required libraries.
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Next,  let’s import the iris data from sklearn's datasets. {from sklearn dot datasets import load_iris}
from sklearn.datasets import load_iris

# After that let’s load the iris data. {iris data is equal to load iris}
iris_data = load_iris()

# Now we will load iris dataset into a dataframe. {data is equal to pd dot DataFrame, and let’s pass the dataset and the column names in it}.
data = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)

# First, we will create histogram chart from the dataframe using seaborn and streamlit's pyplot function. So let's write its code. {fig is equal to plt dot figure. sns dot histogram, and we will pass the dataframe and the number of bins that we want to create in the histogram as parameters}. Next let's show the histogram in the streamlit app. {st dot pyplot and lets pass the figure in it}. Now let’s run this code and view the histogram. Iris dataset has 4 columns and in the histogram, each column is represented by different color.
fig = plt.figure()
sns.histplot(data=data, bins=20)
st.pyplot(fig)


# Next we will create a boxplot on the iris dataset. {fig is equal to plt dot figure. sns dot boxplot, and we will pass the dataframe}. Now let’s show the box plot in the streamlit app. {st dot pyplot and we will pass the figure in it}. Now, we can run this code and view the boxplots for each column of iris data. The box drawn in the box plot shows the first and third quartile of the data. The horizontal line going through the box is the median. Vertical lines that are going out of the box show minimum and maximum peaks, and any data point which lies outside these lines is an outlier.
fig = plt.figure()
sns.boxplot(data=data)
st.pyplot(fig)


# The last plot we will draw is the scatter plot. Let’s write its code, {fig is equal to plt dot figure. sns dot scatterplot and let’s pass the dataframe in it}. Now let’s show the plot in streamlit application. {st dot pyplot and we will pass the figure in it plot}. Let’s run this code and view the scatter plot. 
fig = plt.figure()
sns.scatterplot(data=data)
st.pyplot(fig)