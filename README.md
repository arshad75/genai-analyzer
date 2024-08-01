```python
# genai-analyzer
import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv('data.csv')

# Get the numerical columns
numerical_cols = data.select_dtypes(include=[np.number]).columns

# Normalize the numerical columns
data[numerical_cols] = (data[numerical_cols] - data[numerical_cols].mean()) / data[numerical_cols].std()

# Get the categorical columns
categorical_cols = data.select_dtypes(include=[np.object]).columns

# One-hot encode the categorical columns
data = pd.get_dummies(data, columns=categorical_cols)
```