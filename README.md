```python
# genai-analyzer
import numpy as np

def compute_mean(data):
  """Computes the mean of a list of numbers.

  Args:
    data: A list of numbers.

  Returns:
    The mean of the numbers in the list.
  """

  if not isinstance(data, list):
    raise TypeError("Data must be a list.")

  if not all(isinstance(x, int) or isinstance(x, float) for x in data):
    raise TypeError("Data must contain only integers or floats.")

  if len(data) == 0:
    return 0.0

  return np.mean(data)
```