# Replace 'input.txt' with the actual path to your file
def assgn1():

    file_path = '1.txt'

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()  # Split the line into individual words
                for word in words:
                    if word == 'QS':
                        print('0',end='')
                    else:
                        print('1',end='')
                print(end=' ')


    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def assgn2():

    file_path = '2.txt'
    try:
        with open(file_path, 'r') as file:
            for line in file:
                for character in line:
                    if character == '.':
                        print('1',end='')
                    else:
                        print('0',end='')
                    


    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
