import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y =[2,3,5,7,11]
plt.plot(x,y)
plt.show()

plt.plot(x,y,'ro')
plt.show()

#limit numbers on each axis
plt.plot(x,y)
plt.axis([0,6,0,12])
plt.show()

#add the labels,title,linewidth and legend.
plt.plot(x,y,linewidth=5,label='line 1')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.legend()
plt.show()

#plot multiple graphs on a single plot
y2=[1,4,9,16,25]
plt.plot(x,y,linewidth=5,label='line 1')
plt.plot(x,y2,linewidth=5,label='line 2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines Plot')
plt.legend()
plt.show()

x = np.arange(0,10,0.2)
print(x)
y1 = x**2
y2 = x**3
plt.plot(x,y1,label='y=x^2')
plt.plot(x,y2,label='y=x^3')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Polynomial Functions')
plt.legend()
plt.show()


#bar graph
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 20]
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph')
plt.show()

#multiple bar graphs in a single plot
values2 = [12, 18, 5, 10, 25]
bar_width = 0.35
index = np.arange(len(categories))
plt.bar(index, values, bar_width, label='Values 1')
plt.bar(index + bar_width, values2, bar_width, label='Values 2')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Multiple Bar Graphs')
plt.xticks(index + bar_width / 2, categories)
plt.legend()
plt.show()

plt.bar(["male literacy","female literacy"],[90,95])
plt.show()