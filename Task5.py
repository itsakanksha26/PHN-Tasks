import matplotlib.pyplot as plt


categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [23, 56, 41, 62, 19]


data = [12, 17, 21, 18, 14, 13, 16, 9, 12, 15, 19, 11, 14, 16, 20, 18, 15, 13, 16, 11, 10]


labels = ['Apple', 'Banana', 'Orange', 'Mango']
sizes = [30, 25, 15, 30]


x_values = [1, 2, 3, 4, 5]
y_values = [2, 5, 3, 6, 4]

fig, axis = plt.subplots(2, 2)
fig.suptitle('Subplots')


axis[0, 0].bar(categories, values)
axis[0, 0].set_title('Bar Chart')
axis[0, 0].set_xlabel('Categories')
axis[0, 0].set_ylabel('Values')


axis[0, 1].hist(data, bins=10)
axis[0, 1].set_title('Histogram')
axis[0, 1].set_xlabel('Data')
axis[0, 1].set_ylabel('Frequency')

axis[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%')
axis[1, 0].set_title('Pie Chart')

axis[1, 1].scatter(x_values, y_values)
axis[1, 1].set_title('Scatter Plot')
axis[1, 1].set_xlabel('X values')
axis[1, 1].set_ylabel('Y values')

fig.tight_layout()

plt.show()
