"""
The problems analyzes the jogging data of an user
"""
def main():
    number_list=[]
    n = int(input("Enter the number of days: "))
    for i in range(1, n+1):
        item = float(input(f"Enter day {i} running length: "))
        number_list.append(item)
        if number_list[-3:] == [0, 0, 0]:
            print("")
            print("You had too many consecutive lazy days!")
            break
        
        average = sum(number_list)/len(number_list)
        average_f = "{:.2f}".format(average)

    if(number_list[-3:] != [0, 0, 0]  and average_f < 3):
           print("")
           print("Your running mean of",average_f," km was too low! ")
    if(number_list[-3:] != [0, 0, 0]  and average_f >= 3):
          print("")
          print("You were persistent runner! With a mean of",average_f,"km.")



if __name__ == "__main__":
    main()