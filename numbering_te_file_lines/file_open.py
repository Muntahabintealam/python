"""
The program opens a file and prints the ros of the file with line number

"""
def main():
    f=input("Enter the name of the file: ")
    file1 = open(f)
    Lines = file1.readlines()

    count = 0
# Strips the newline character
    for line in Lines:
     count += 1
     print("{} {}".format(count, line.strip()))

if __name__ == "__main__":
        main()
