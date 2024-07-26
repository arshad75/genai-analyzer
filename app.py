```python
import math

def calculate_area(radius):
    # Correct calculation of area
    area = math.pi * radius ** 2
    return area

def find_max_in_list(lst):
    # Using built-in function to find max
    max_val = max(lst)
    return max_val

def read_file(file_path):
    # Handling file not found exception
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found at {file_path}")

def main():
    # Correctly using list append
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    numbers.append(7)
    numbers.append(8)

    # Using context manager and relative file path
    with open('data.txt', 'r') as file:
        result = file.read()

    # Correctly calculated area
    radius = 5
    area = calculate_area(radius)

    # Efficiently calculated max in list
    max_number = find_max_in_list(numbers)

    print(f"The area of the circle is: {area}")
    print(f"The maximum number is: {max_number}")

if __name__ == '__main__':
    main()
```