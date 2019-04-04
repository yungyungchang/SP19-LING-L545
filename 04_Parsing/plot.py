import sys
import matplotlib.pyplot as plt

labels = {0:'vi', 1:'en', 2:'zh',3:'it',4:'es', 5:'fi', 6:'cac', 7:'ko', 8:'tr', 9:'ja'}
x = [0.02, 0.03, 0.04, 0.08, 0.21, 0.34, 0.36, 0.96, 0.99, 1]  # proportion of OV
y = [0.98, 0.97, 0.96, 0.92, 0.79, 0.66, 0.64, 0.04, 0.01, 0]  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
plt.show()
