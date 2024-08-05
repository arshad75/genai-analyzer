```python
import math

def calculate_area(radius):
    # Corrected calculation of area
    area = math.pi * radius ** 2
    return area

def find_max_in_list(lst):
    # Using built-in function for finding max
    max_val = max(lst)
    return max_val

def read_file(file_path):
    # Handling file not found exception and using context manager
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found")
        return None
    return content

def main():
    # Correct usage of list append
    numbers = [1, 2, 3, 4, 5]
    numbers.extend([6, 7, 8])

    # Using context manager and variable for file path
    with open('data.txt', 'r') as file:
        result = file.read()
    print(result)

    # Correctly calculated area
    radius = 5
    area = calculate_area(radius)
    print(f"The area of the circle is: {area}")

    # Efficient way to find max in list
    max_number = find_max_in_list(numbers)
    print(f"The maximum number is: {max_number}")

if __name__ == '__main__':
    main()
```