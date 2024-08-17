import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

num_rolls = 10_000_000

# Roll two dice
dice1 = np.random.randint(1, 7, num_rolls)
dice2 = np.random.randint(1, 7, num_rolls)

sums = dice1 + dice2

sum_counts = np.bincount(sums)[2:13]

probabilities = sum_counts / num_rolls

results_df = pd.DataFrame({
    'Sum': np.arange(2, 13),
    'Probability': probabilities
})

print(results_df)

plt.figure(figsize=(10, 6))
plt.bar(results_df['Sum'], results_df['Probability'], color='blue', alpha=0.7)
plt.title('Ймовірність отримати кожну суму після підкидання кубиків')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.xticks(np.arange(2, 13))
plt.grid(True)
plt.show()

print("Значення в результаті близькі до значаень з таблиці наведеній у завданні")
