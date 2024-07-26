import math

def calculate_area(radius):
    # Incorrect calculation of area
    area = math.pi * radius ** 3
    return area

def find_max_in_list(lst):
    # Using a manual loop to find max instead of built-in function
    max_val = lst[0]
    for val in lst:
        if val > max_val:
            max_val = val
    return max_val

def read_file(file_path):
    # Not handling file not found exception
    file = open(file_path, 'r')
    content = file.read()
    file.close()
    return content

def main():
    # Incorrect usage of list append
    numbers = [1, 2, 3, 4, 5]
    numbers.append([6, 7, 8])

    # Hardcoded file path and not using context manager
    result = read_file('data.txt')
    print(result)

    # Incorrectly calculated area
    radius = 5
    area = calculate_area(radius)
    print(f"The area of the circle is: {area}")

    # Inefficient way to find max in list
    max_number = find_max_in_list(numbers)
    print(f"The maximum number is: {max_number}")

if __name__ == '__main__':
    main()
