import matplotlib.pyplot as plt
#represents parts of whole
language=["Java","Python","C","R"]
hours=[30,30,10,20]
plt.pie(hours,labels=language)
plt.show()

#autopct-to display percentages
language=["Java","Python","C","R"]
hours=[30,30,10,20]
plt.pie(hours,labels=language,autopct="%1.2f%%")   #2f-number of decimal value needed
plt.show()

#explode-to highlite one section
exp=[0,0,0.1,0]
language=["Java","Python","C","R"]
hours=[30,30,10,20]
plt.pie(hours,labels=language,autopct="%1.2f%%",explode=exp) 
plt.show()
