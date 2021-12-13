import pandas as pd
import matplotlib.pyplot as plt
heart = pd.read_csv('heart.csv')

#print(heart.head(10))
#print(heart[['Age', 'RestingBP', 'Cholesterol']].head(10))
aux_heart = heart.loc[heart['Age']>=60]

plt.scatter(heart['Age'], heart['MaxHR'])
plt.xlabel('Age')
plt.ylabel('MaxHR')
plt.show()