import matplotlib.pyplot as plt
import numpy as np

#Scatter plot example
x1 = np.array(np.arange(1,20,2))
y1 = np.array(np.random.randint(1,100,10))
plt.subplot(3,3,1)
plt.scatter(x1,y1)
plt.title('Scatter plot example with 1 array')

#Scatter plot example with 2 data set and colored dots
x1 = np.array(np.random.randint(1, 20, 20))
y1 = np.array(np.random.randint(10, 200, 20))
x2 = np.array(np.random.randint(1, 20, 20))
y2 = np.array(np.random.randint(10, 200, 20))
color = np.array(np.arange(0,100,5))
color1 = np.array(np.arange(100,0,-5))
plt.subplot(3,3,2)
plt.scatter(x1,y1, c=color, cmap='viridis')
plt.scatter(x2,y2, c=color1, cmap='Accent')
plt.colorbar()
plt.title('Scatter plot with 2 dataset and colored dots')

#Scatter plot using 3 dimensions showing sizes
z1 = np.array(np.random.randint(200,2000,20))
plt.subplot(3,3,3)
plt.scatter(x1,y1, c = color, cmap='BuGn', s=z1, alpha=0.5)
plt.title('Scatter plot using 3 dimension with different sizes and opacity')

#Bar Graphs Vertical with different size than default
x = ["Apples", "Banana", "Oranges", "34", "32j"]
y = [2, 4, 7, 4, 3]
plt.subplot(3,3,4)
plt.bar(x, y, color='red', width= 0.3)
plt.title('Bar graph vertical')

#Bar Chart horizontal with default size
plt.subplot(3,3,5)
plt.barh(x,y)
plt.title('Bar Graph Horizontal')

#Histogram Chart
h1 = np.random.normal(170,10,250)
plt.subplot(3,3,6)
plt.hist(h1)
plt.title('Histogram chart')
#Simple Pie Graph
y = np.array([30,25,20,10,40])
labels = ["a","b","c","d","e"]
plt.subplot(3,3,7)
plt.pie(y, labels = labels)
plt.title('A simple pie chart')

#Pie Graph with different start angle and explode feature
exp = [0.2, 0.1, 0.0, 0.0, 0.0]
plt.subplot(3,3,8)
plt.pie(y, labels=labels, explode= exp, startangle= 90)
plt.title('Same pie chart with different start angle and explode feature')

#Pie Graph with shadow and custom colors
colors = ["red", "green", "blue", "orange", "purple"]

plt.subplot(3,3,9)
plt.pie(y, labels=labels, colors=colors, shadow=True, explode=exp, startangle=45)
plt.legend(title = 'legends', loc = "lower right", bbox_to_anchor = (1.5,0))
print("code completed")
plt.suptitle('Various graphs in Python')
plt.savefig('output.png')
plt.show()



