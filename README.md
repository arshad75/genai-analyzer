```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Scatter plot of x and y
plt.scatter(df['x'], df['y'])
plt.title('Scatter Plot of x and y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Histogram of ages
plt.hist(df['age'], bins=10)
plt.title('Histogram of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Mean values by category
mean_values = df.groupby('category')['value'].mean()
mean_values.plot(kind='bar')
plt.title('Mean Values by Category')
plt.xlabel('Category')
plt.ylabel('Mean Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```