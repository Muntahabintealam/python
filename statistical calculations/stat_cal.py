
"""
The program calculates the mean standard_deviation and histogram data for a group of data.


"""
import math


def main():
    print("Enter the data, one value per line.\n"
          "End by entering empty line.")
    user_values = []
    prompt = ""
    line = input(prompt)

    while line:
        user_values.append(float(line))
        line = input(prompt)
    length =len(user_values)
    if(length<2):
        print("Error: needs two or more values.")
    else:
      meanfunction(user_values)
      stdev(user_values)
      print(f"The mean of given data was: {meanfunction(user_values):.2f}")
      print(f"The standard deviation of given data was: {stdev(user_values):.2f}")
      hist(user_values)

def meanfunction(data):
    """
                The function meanfunction calculates the mean of a group of data
                    :param data:list of float

                    :return : float
                """
    mean = sum(data) / len(data)
    return mean


def variance(data):
    """
                    The function variance calculates the variance of a group of data
                        :param data:list of float

                        :return : float
                    """
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / (n - 1)
    return variance


def stdev(data):
    """
                        The function stdev calculates the standard_deviation of a group of data
                            :param data:list of float

                            :return : float
                        """
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev


def hist(data):
    """
                            The function stdev calculates the histogram data for a group of data
                                :param data:list of float

                                :return : null
                            """

    count = 0

    mean_list = []
    standard_deviation = stdev(data)
    mean = meanfunction(data)
    output = ""
    if(standard_deviation==0):
        print("Deviation is zero.")
    else:
      for x in data:
        calculated_value = abs(x - mean)
        mean_list.append(calculated_value)
      for category_number in range(0, 6):
        count = 0
        output = ""
        lower_bound = category_number * 0.5 * standard_deviation
        upper_bound = (category_number + 1) * 0.5 * standard_deviation
        for x in mean_list:
            if lower_bound <= x < upper_bound:
                count = count + 1

        for i in range(count):
            output += "*"
        print(f"Values between std. dev. {lower_bound:.2f}-{upper_bound:.2f}:", output)
if __name__ == "__main__":
    main()