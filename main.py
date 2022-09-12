# Read fruit data csv file
def read_fruits_data(filename):
    fruits = []
    with open(filename, 'r') as f:
        for line in f:
            fruits.append(line.strip().split('\t'))
    return fruits


if __name__ == "__main__":
    fruits = read_fruits_data('fruit_data_with_colors.txt')
    print(fruits)
