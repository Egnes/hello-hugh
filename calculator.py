
try:
    score = float(input('Enter score between 0.0 and 1.0: '))

    if 0.9 <= score < 1.0:
        print("A")
    elif 0.8 <= score < 0.9:
        print("B")
    elif 0.7 <= score < 0.8:
        print("C")
    elif 0.6 <= score < 0.7:
        print("D")
    elif score < 0.6:
        print("F")
    else:
        print("Please insert a value between 0.0 and 1.0")
except:
    print("Error, please enter a numeric value.Thank you.")





