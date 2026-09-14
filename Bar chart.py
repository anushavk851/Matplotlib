import matplotlib.pyplot as plt

#used for comparing values between category
product=["A","B","C","D"]
sales=[100,125,102,120]
plt.bar(product,sales) #by default it shows vertical bar
plt.show()

#horizontal bar
product=["A","B","C","D"]
sales=[100,125,102,120]
plt.barh(product,sales)
plt.show()

#barchart with dataframe
import matplotlib.pyplot as plt
import pandas as pd 
data={
    "products":["A","B","C","D"],
    "sales":[100,105,102,120]
}
df=pd.DataFrame(data)
df
plt.bar(df['products'],df['sales'])
plt.show()
