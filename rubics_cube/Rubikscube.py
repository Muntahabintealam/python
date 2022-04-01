"""
The program calculatess performes of a rubics cube contests
"""
def main():
    number_list=[]

    for i in range(1, 5+1):
        item = float(input(f"Enter the time for performance {i}: "))
        number_list.append(item)
    number_list.remove(max(number_list))
    number_list.remove(min(number_list))

    average = sum(number_list)/len(number_list)
    average_f = "{:.2f}".format(average)
    print("The official competition score is",average_f,"seconds.")

if __name__ == "__main__":
    main()