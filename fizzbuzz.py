def FizzBuzz(l, limit):
    for count in range(1, limit):
        print(GenerateOutput(l, count))

def GenerateOutput(l, count):
    out = ""
    for x in l:
        out += x[0] if count % x[1] == 0 else ""
    return out or count # Returns count if out is an empty string

if __name__ == "__main__":
    list = [
        ["Fizz", 3],
        ["Buzz", 5]
    ]
    
    FizzBuzz(list, 100)
    print(list)
