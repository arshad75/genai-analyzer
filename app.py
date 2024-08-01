import math

def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

def find_max_in_list(lst):
    return max(lst)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("File not found")

def main():
    numbers = [1, 2, 3, 4, 5]
    numbers.extend([6, 7, 8])

    result = read_file('data.txt')
    print(result)

    radius = 5
    area = calculate_area(radius)
    print(f"The area of the circle is: {area}")

    max_number = find_max_in_list(numbers)
    print(f"The maximum number is: {max_number}")

if __name__ == '__main__':
    main()