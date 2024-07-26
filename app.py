import math

def calculate_area(radius):
    # Correct calculation of area using radius squared
    area = math.pi * radius ** 2
    return area

def find_max_in_list(lst):
    # Built-in function for finding maximum in a list
    return max(lst)

def read_file(file_path):
    # Using try-except to handle file not found exception
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found")
        return ""
    return content

def main():
    # Correct usage of list append
    numbers = [1, 2, 3, 4, 5]
    numbers.extend([6, 7, 8])  # Extend the list instead of appending a nested list

    # Variable for file path to make it configurable
    file_path = 'data.txt'
    result = read_file(file_path)
    print(result)

    # Correctly calculated area
    radius = 5
    area = calculate_area(radius)
    print(f"The area of the circle is: {area}")

    # Built-in function to find max in list
    max_number = find_max_in_list(numbers)
    print(f"The maximum number is: {max_number}")

if __name__ == '__main__':
    main()