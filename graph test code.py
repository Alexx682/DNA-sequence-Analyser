# got to type pip install matplotlib in the terminal to install matplotlib before running this code

######################################
# Basic line graph
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot
plt.plot(x, y)

# Labels and title
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the graph
plt.show()
##########################################
# Basic bar graph

import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
marks = [90, 85, 95]

plt.bar(subjects, marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

############################################
# scatter plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 4, 9, 6]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

###############################################################
# pie chart 

import matplotlib.pyplot as plt

labels = ["Apple", "Banana", "Orange"]
sizes = [40, 35, 25]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Fruit Distribution")
plt.show()

######################################
# box plot


import matplotlib.pyplot as plt

# Your data
gene_lengths = [10, 15, 20, 25, 30, 35, 40, 50, 60, 100]

# Create the box plot
plt.boxplot(gene_lengths)

# Add a title and label
plt.title("Distribution of Gene Lengths")
plt.ylabel("Gene Length (base pairs)")

# Show the graph
plt.show()












