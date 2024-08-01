```python
def calculate_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number")
    area = math.pi * radius ** 2
    return area

def find_max_in_list(lst):
    if not lst:
        raise ValueError("Cannot find the maximum value in an empty list")
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content.strip()
    except FileNotFoundError:
        return "File not found"
    except PermissionError:
        return "Permission denied"
    except UnicodeDecodeError:
        return "Invalid encoding"

def main():
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    numbers.append(7)
    numbers.append(8)

    result = read_file('data.txt')
    if result != "File not found":
        print(result)

    radius = 5
    try:
        area = calculate_area(radius)
        print(f"The area of the circle is: {area}")
    except ValueError as e:
        print(e)

    try:
        max_number = find_max_in_list(numbers)
        print(f"The maximum number is: {max_number}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
```