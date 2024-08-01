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
    # Handling file not found exception and using context manager
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def main():
    # Correct usage of list append
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    numbers.append(7)
    numbers.append(8)

    # Using variable for file path and context manager
    file_path = 'data.txt'
    result = read_file(file_path)
    if result is not None:
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