```python
import math

def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

def find_max_in_list(lst):
    max_val = max(lst)
    return max_val

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("File not found")
        return None

def main():
    numbers = [1, 2, 3, 4, 5]
    numbers.extend([6, 7, 8])

    file_path = input('Enter file path: ')
    result = read_file(file_path)
    if result is not None:
        print(result)

    radius = 5
    area = calculate_area(radius)
    print(f"The area of the circle is: {area}")

    max_number = find_max_in_list(numbers)
    print(f"The maximum number is: {max_number}")

if __name__ == '__main__':
    main()
```