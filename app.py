```python
def calculate_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number")
    return math.pi * radius ** 2


def find_max_in_list(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content.strip()
    except FileNotFoundError:
        return "File not found"
    except PermissionError:
        return "Permission denied"
    except UnicodeDecodeError:
        return "Could not decode the file"


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    result = read_file('data.txt')
    if isinstance(result, str):
        print(result)
    else:
        print(float(result))  # Convert the result to float for the calculation

    try:
        radius = 5
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