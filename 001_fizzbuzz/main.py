def fizzbuzz(integers):
    result = ""
    for integer in integers:
        if integer % 3 == 0 and integer % 5 == 0:
            result += "FizzBuzz"
        elif integer % 3 == 0:
            result += "Fizz"
        elif integer % 5 == 0:
            result += "Buzz"
        else:
            result += str(integer)
        result += " "
    return result.rstrip()
