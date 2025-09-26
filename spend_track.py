import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("sample_expenses.csv")
total=data["amount"].sum()
group=data.groupby("category")["amount"].sum()
fig,ax=plt.subplots()
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(group)))
ax.pie(group,labels=group.index,autopct='%1.2f%%',colors=colors)
plt.title(f"Expense Distribution by Category\nTotal: ${total:.2f}") 
textstr="\n".join([f"{name}: ${amount:.2f}" for name ,amount in zip(group.index,group.values)])
ax.text(1.8,0,textstr,fontsize=10,verticalalignment="center")
plt.show()
