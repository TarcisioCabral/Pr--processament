#https://www.kaggle.com/fedesoriano/heart-failure-prediction
import pandas as pd
import matplotlib.pyplot as plt
heart = pd.read_csv('heart.csv')

#print(heart.head(10))
print(heart[['Age', 'RestingBP', 'Cholesterol']].head(10))


plt.bar(heart['Age'], heart['Cholesterol'])
plt.xlabel('Idade')
plt.ylabel('Cholesterol')
plt.xlim(27,78)
plt.show()
