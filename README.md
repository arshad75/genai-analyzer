```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Scatter plot of x and y
df.plot.scatter(x='x', y='y', title='Scatter Plot of x and y')
plt.xlabel('x')
plt.ylabel('y')

# Histogram of ages
df['age'].hist(bins=10, title='Histogram of Ages', xlabel='Age', ylabel='Frequency')

# Mean values by category
mean_values = df.groupby('category')['value'].mean()
mean_values.plot(kind='bar', title='Mean Values by Category', xlabel='Category', ylabel='Mean Value')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

```