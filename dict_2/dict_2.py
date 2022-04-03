"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def main():
    english_spanish = {"hey": "hola", "home": "casa", "thanks": "gracias"}
    def printing():
      print("Dictionary contents:")
      elements = list(english_spanish.keys())
      elements.sort()
      print(*elements, sep=", ")
    while True:
        print("Dictionary contents:")
        elements = list(english_spanish.keys())

        print(*elements, sep=", ")
        while True:

          command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

          if command == "W":

            user_choice=input("Enter the word to be translated: ")
            if user_choice in english_spanish:
              choice_in_spanish =english_spanish[user_choice]
              print(f"{user_choice} in Spanish is {choice_in_spanish}")
            else:
             print("The word", user_choice, "could not be found from the dictionary.")

          elif command == "A":

            user_choice=input("Give the word to be added in English: ")
            new_word=input("Give the word to be added in Spanish: ")
            english_spanish[user_choice]=new_word
            printing()

          elif command == "P":


            print("")
            print("English-Spanish")
            for key in sorted(english_spanish.keys()):
                print("%s %s" % (key, english_spanish[key]))
            print("")
            print("Spanish-English")

            d_sorted = sorted(english_spanish.items(), key=lambda kv: kv[1])
            for k, v in d_sorted:
                print( v,k)
            print("")


          elif command == "R":

            user_choice=input("Give the word to be removed: ")
            if user_choice in english_spanish:
                del english_spanish[user_choice]
            else:
                print("The word",user_choice, "could not be found from the dictionary.")
                return

          elif command == "Q":
            print("Adios!")
            return
          elif command == "T":

            user_choice=input("Give the word to be added in English: ")

            for i in len(user_choice):
             english_spanish[user_choice]=new_word
          else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
