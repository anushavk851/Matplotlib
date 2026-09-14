import matplotlib.pyplot as plt

#shows distribution of numerical data
ages=[20,21,22,27,24,25,22,24,21,20,19]
plt.hist(ages)
plt.show()

#bins--histogram divides values into intervals called bins
ages=[20,21,22,27,24,25,22,24,21,20,19]
plt.hist(ages,bins=8)
plt.show()
