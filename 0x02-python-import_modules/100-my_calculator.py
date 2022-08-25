#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal
    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sys.argv[2] not in ['+', '-', '/', '*']:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        match sys.argv[2]:
            case '+':
                print("{:d} + {:d} = {:d}".format(a, b, cal.add(a, b)))
            case '/':
                print("{:d} / {:d} = {}".format(a, b, cal.div(a, b)))
            case '-':
                print("{:d} - {:d} = {}".format(a, b, cal.sub(a, b)))
            case '*':
                print("{:d} * {:d} = {}".format(a, b, cal.mul(a, b)))
            case _:
                pass
