def hailstone (start, end):
    count = 0
    num = 0
    for i in range (start, (end + 1)):
        length = 0
        initial = i
        while i != 1:
            if i % 2 == 0:
                i = (i // 2)
            else:
                i = (3 * i + 1)
            length += 1
            if length > count:
                count = length
                num = initial

    print("The number " + str(num) + " has the longest cycle length of " + str(count) + ".")

def main ():
    start = input("Please enter a starting number: ")
    while not start.isdigit():
        start = input("Please enter a starting number: ")
    end = input("Please enter an ending number: ")
    while not end.isdigit():
        end = input("Please enter an ending number: ")

    hailstone (int(start), int(end))
main()
