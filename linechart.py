import matplotlib.pyplot as plt

days=[1,2,3,4,5]
temperature=[30,32,38,39,31]
plt.plot(days,temperature)
plt.show()  #to remove object from result

#Title()
days=[1,2,3,4,5]
temperature=[30,32,38,39,31]
plt.title("Daily Temperature")
plt.plot(days,temperature)
plt.show()

#xlabel() and ylabel() - to give names to axis
days=[1,2,3,4,5]
temperature=[30,32,38,39,31]
plt.title("Daily Temperature")
plt.plot(days,temperature)
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

#Grid()-to add grid lines for reading datapoints easily
days=[1,2,3,4,5]
temperature=[30,32,38,39,31]
plt.title("Daily Temperature")
plt.plot(days,temperature)
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid()
plt.show()

#changing style
#1 LINESTYLE
days=[1,2,3,4,5]
temperature=[30,32,38,39,31]
plt.title("Daily Temperature")
plt.plot(days,temperature,linestyle="-.")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid()
plt.show()

#2 LINEWIDTH
days=[1,2,3,4,5]
temperature=[30,32,38,39,31]
plt.title("Daily Temperature")
plt.plot(days,temperature,linewidth=4)
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid()
plt.show()

#3 MARKER
days=[1,2,3,4,5]
temperature=[30,32,38,39,31]
plt.title("Daily Temperature")
plt.plot(days,temperature,marker="*")  #o,s,*,^,D,x
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid()
plt.show()

#4 COLOR
days=[1,2,3,4,5]
temperature=[30,32,38,39,31]
plt.title("Daily Temperature")
plt.plot(days,temperature,color="red")  #o,s,*,^,D,x
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid()
plt.show()

#5 FIGURE
days=[1,2,3,4,5]
temperature=[30,32,38,39,31]
plt.title("Daily Temperature")
plt.plot(days,temperature)
plt.Figure(figsize=(8,5)) #8,5 is width and height
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid()
plt.show()

#6 SAVEFIG
days=[1,2,3,4,5]
temperature=[30,32,38,39,31]
plt.title("Daily Temperature")
plt.plot(days,temperature)
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid()
plt.savefig("Temperature.png")

#multiple line chart
month=["jan","feb","mar","apr"]
product_a=[100,86,125,142]
product_b=[90,103,145,111]
plt.plot(month,product_a)
plt.plot(month,product_b)
plt.show()

#Labels and legends
month=["jan","feb","mar","apr"]
product_a=[100,86,125,142]
product_b=[90,103,145,111]
plt.plot(month,product_a,label="Product A")
plt.plot(month,product_b,label="Product B")
plt.legend()
plt.show()


#1 create a monthly sales chart
month=["jan","feb","mar","apr","may"]
sales=[10000,12000,13000,14000,16000]
plt.Figure(figsize=(8,6))
plt.title("Sales Chart")
plt.xlabel=("Sales")
plt.ylabel=("Month")
plt.plot(sales,month,linestyle="--",linewidth=2,color="black",marker="^")
plt.grid()
plt.savefig("sales chart.png")
plt.show()
