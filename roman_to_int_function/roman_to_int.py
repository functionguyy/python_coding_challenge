#!/usr/bin/python3

def intToRomanNumeralStr(e: int, number: int) -> str:
    romanNumeralMap = {1000: {1: 'M'},
                       100: {9: 'CM', 4: 'CD', 5: 'D', 1: 'C'},
                       10: {9: 'XC', 4: 'XL', 5: 'L', 1: 'X'},
                       1: {9: 'IX', 4: 'IV', 5: 'V', 1: 'I'}}

    romanStr = romanNumeralMap[e][number]

    return romanStr


def selectRomanNumeralChar(d: int, r: int) -> str:
    romanNumeralChar = ""

    if r == 9:
        romanNumeralChar += intToRomanNumeralStr(d, r)
    elif r == 4:
        romanNumeralChar += intToRomanNumeralStr(d, r)
    elif r >= 5:
        romanNumeralChar += intToRomanNumeralStr(d, 5)
        if r - 5 > 0:
            i = 1
            while i <= (r - 5):
                romanNumeralChar += intToRomanNumeralStr(d, 1)
                i += 1
    else:
        i = 1
        while i <= r:
            romanNumeralChar += intToRomanNumeralStr(d, 1)
            i += 1

    return romanNumeralChar


def encoder(num: int) -> str:
    divisor = 1000
    loopControl = 1

    n = num
    romanNumeralString = ""

    while loopControl != 0:
        result = n // divisor

        if result > 0:
            n = n - (result * divisor)

            if divisor == 1000:
                if result > 3:
                    return romanNumeralString
                i = 1
                while i <= result:
                    # Pick M and add to the string
                    romanNumeralString += intToRomanNumeralStr(divisor, 1)
                    i += 1
            if divisor == 100:
                romanNumeralString += selectRomanNumeralChar(divisor, result)

            if divisor == 10:
                romanNumeralString += selectRomanNumeralChar(divisor, result)

            if divisor == 1:
                romanNumeralString += selectRomanNumeralChar(divisor, result)

        divisor = divisor // 10
        if divisor == 0:
            loopControl = 0

    return romanNumeralString


def roman_to_int(roman_string: str) -> int:
    """Function that converts a Roman numeral to an integer

    Args:
        roman_string: roman numeral string
    Return:
        integer representation of roman numeral string or 0
    """
    romanNumeralDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                        'M': 1000}
    number = 0
    if (type(roman_string) is not str or roman_string is None):
        return number
    RNStrList = list(enumerate(roman_string))
    for i, s in RNStrList:
        currentNumber = romanNumeralDict[s]
        # print("Current number before comparison {:d}".format(currentNumber))
        currentLetterIndex = i
        if currentLetterIndex + 1 < len(RNStrList):
            nextLetterIndex = currentLetterIndex + 1
            # print("Next letter index {:d}".format(nextLetterIndex))
            nextLetter = RNStrList[nextLetterIndex][1]
            nextNumber = romanNumeralDict[nextLetter]
            # print("next number {:d}".format(nextNumber))
            if currentNumber < nextNumber:
                # convert current number to a negative number
                currentNumber *= -1
                # print("Current number is {:d}".format(currentNumber))
        number += currentNumber
        # print(number)

    if encoder(number) != roman_string:
        number = 0

    return number
