

"""
    The function finds the longest substring from a string in alphabetical order
    Name:Muntaha binte ALam
    Email:muntaha.alam@tuni.fi
    Student ID:150448389

    """
def longest_substring_in_order(sample):
    """
                    The function finds the longest substring from a string in alphabetical order
                    :param sample:string
                    :return : string
                   """

    r = ''
    c = ''
    for char in sample:
       if (c == ''):
         c = char
       elif (c[-1] <= char):
        c += char
       elif (c[-1] > char):
          if (len(r) < len(c)):
            r = c
            c = char
          else:
            c = char
    if (len(c) > len(r)):
     r = c
    return r