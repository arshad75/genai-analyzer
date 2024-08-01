```python
# genai-analyzer
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data.csv')
df['age'] = df['age'].astype('int')
df['gender'] = df['gender'].astype('category')
X = df[['age', 'gender']]
y = df['target']

model = LogisticRegression()
model.fit(X, y)
y_pred = model.predict(X)
```