"""
The program calculates the word density of a sentences


"""


def word_count(str):
    """
    calculates the number of times each word appear in a sentence
    :param str:
    :return: integer
    """



    counts = dict()
    words = str.split()

    for word in words:
       word = word.lower()
       if word in counts:
          counts[word] += 1
       else:
          counts[word] = 1
    return counts


def main():

    print("Enter rows of text for word counting. Empty row to quit.")

    user_values = []
    prompt = ""
    line = input(prompt)

    while line:
        user_values.append(line)
        line = input(prompt)

    user_list = " ".join(user_values)

    user_list=word_count(user_list)

    for k, v in sorted(user_list.items()):
        print(k,":",v,"times")


if __name__ == "__main__":
    main()
