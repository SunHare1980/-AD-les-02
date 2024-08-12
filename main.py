import pandas as pd
import numpy as np

ArrayO = np.random.randint(2,6,(5,10))

Names = ['Маша','Миша','Петя','Коля','Витя','Виталя','Юля','Олеся','Виктория','Юра']
data = {'Name':Names, 'Математика':ArrayO[0],
        'Физика': ArrayO[1],
        'Биология':ArrayO[2],
        'Труд':ArrayO[3],
        'Физкультура':ArrayO[4]}
df = pd.DataFrame(data)
print(df.head())
print(df.info())
print(df.describe())

print("Математика средняя: ",df['Математика'].mean())
print("Физика средняя: ",df['Физика'].mean())
print("Биология средняя: ",df['Биология'].mean())
print("Труд средняя: ",df['Труд'].mean())
print("Физкультура средняя: ",df['Физкультура'].mean(), '\n')

print("Математика медиана: ",df['Математика'].median())
print("Физика медиана: ",df['Физика'].median())
print("Биология медиана: ",df['Биология'].median())
print("Труд медиана: ",df['Труд'].median())
print("Физкультура медиана: ",df['Физкультура'].median(), '\n')

Q1 = df['Математика'].quantile(0.25)
Q3 = df['Математика'].quantile(0.75)
print('Q1:',Q1,' Q3:', Q3, '\n')
IQR = Q3 - Q1
stdA = df['Математика'].std()
print(f"Стандартное отклонение математика - {stdA}")
