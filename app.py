import math

def calculate_area(radius):
    # Correct calculation of area
    area = math.pi * radius ** 2
    return area

def find_max_in_list(lst):
    # Using built-in function to find max
    return max(lst)

def read_file(file_path):
    # Handling file not found exception using try/except
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File not found at {file_path}")
        return None
    return content

def main():
    numbers = [1, 2, 3, 4, 5]
    # Correctly appending to list
    numbers.extend([6, 7, 8])

    file_path = input("Enter the file path: ")
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