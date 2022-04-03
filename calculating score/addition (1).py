"""
The program ask for a file name and sums up user input in that file.

"""
def main():
    kdic = {}
    f=input("Enter the name of the score file: ")
    with open(f, "r") as data:
        data = data.readlines()
        for d in data:
            d = d.rstrip(" ")
            d = d.split()
            try:
                kdic[d[0]] = int(d[1]) + int(kdic[d[0]])
            except KeyError:
                kdic[d[0]] = int(d[1])
    print("Contestant score:")
    for k, v in sorted(kdic.items()):
        print(k, v)
if __name__ == "__main__":
    main()