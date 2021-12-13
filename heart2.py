import pandas as pd
import matplotlib.pyplot as plt
heart = pd.read_csv('heart.csv')

#print(heart.head(10))
print(heart[['Age', 'RestingBP', 'Cholesterol']].head(10))


plt.bar(heart['Sex'], heart['Cholesterol'])
plt.xlabel('Sex')
plt.ylabel('Cholesterol')

plt.show()