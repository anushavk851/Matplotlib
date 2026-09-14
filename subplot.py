import matplotlib.pyplot as plt

ages=[20,2,28,24,25,100,27]
hours=[2,3,4,5,6]
marks=[38,42,49,55,60]
days=[1,2,3,4,5]
temperature=[30,32,38,39,31]

plt.subplot(2,2,1)
plt.boxplot(ages)

plt.subplot(2,2,2)
plt.scatter(hours,marks)

plt.subplot(2,2,3)
plt.plot(days,temperature)

plt.subplot(2,2,4)
language=["Java","Python","C","R"]
hours=[30,30,10,20]
plt.pie(hours,labels=language)

plt.show()
