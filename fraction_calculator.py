"""Walkthough of algorithm:
Step 1: Iterate through the string
Step 2: Find any fractions in the string
  Step 2a: If the fraction is a MIXED number, convert it to an improper fraction
Step 3: Convert the fraction to a decimal value of itself
Step 4: Replace the fraction in the string with the decimal
Step 5: Evaluate the string (i.e 1.5 + 2 = 3.5)
Step 6: Convert the solution into an improper fraction (35/10)
Step 7: Convert the solution to a mixed number (3_1/2)
"""

from fractions import Fraction

def splitFraction(str):
    numerator, denominator = str.split("/")

    return [numerator, denominator]

def improperToMixed(input):

    # checking to see if it's a fraction vs a normal divide
    if "/" in input and len(input) > 1:
        numerator, denominator = input.split("/")

        numerator = int(numerator)
        denominator = int(denominator)

        # calculate the multiplier and numerator and denominator
        multiplier = numerator // denominator
        numerator = numerator % denominator

        # cast them to strings for return
        multiplier = str(multiplier)
        numerator = str(numerator)
        denominator = str(denominator)

        # returning the value in a format that matches the mixed number format
        return(multiplier + "_" + numerator + "/" + denominator)

    else:
        return(input)

def calc(s):
    arr = s.split(' ')

    for a in arr:
        postion = arr.index(a)

        # checking for fractions. Added in the > 1 to differenate between normal divde and fraction
        if "/" in a and len(a) > 1:
            vals = splitFraction(a)
            numerator = vals[0]
            denominator = vals[1]

            # Assuming this is a mixed number and converting it to an improper fraction. numerator in this case will contain the multiplier and also the actual_numerator
            # it should be in this notation 1_2.
            if "_" in numerator:
                multiplier, actual_numerator = numerator.split("_")
                improperNumerator = int(multiplier) * int(denominator) + int(actual_numerator)

                #convert the improper fraction numerator to the numerator
                numerator = str(improperNumerator)

            value = (numerator + '/' + denominator)

            # replacing the value in the array/expression with the value of the evaluation of the string

            arr[postion] = str(eval(value))

    # replacing the origanal expression with the values in the array
    s = " ".join(arr)

    # evaluting what the expression will be and creating an answer
    # (i.e it would evaluate 10.25 + 2 = 12.25)
    solution = eval(s)

    # convert the answer from the evaluation into a fraction form of the decimal
    solutionAsFraction = Fraction(solution)

    # limit the denominator to only one value (lowest possible floor)
    solutionAsFraction = str(solutionAsFraction.limit_denominator())

    # returns the fractions converted to a Mixed Number
    return(improperToMixed(solutionAsFraction))


if __name__ == '__main__':
    print("Please enter in your expression")
    x = input()
    print(calc(x))
