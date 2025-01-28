weight = int(input("Enter the weight of the clothes: "))
water_level = input("Enter the water level (L/M/H): ")
#using Elif functions and nested Ifs to add the conditions given in the question for the answer
if weight < 0:
    print("INVALID INPUT")
elif weight == 0:
    print("Time : 0 minutes")
elif weight > 7000:
    print("OVERLOADED")
else:
    if water_level == "L":
        if weight <= 2000:
            print("Time : 25 minutes")
        else:
            print("INVALID INPUT")
    elif water_level == "M":
        if 2001 <= weight <= 4000:
            print("Time : 35 minutes")
        else:
            print("INVALID INPUT")
    elif water_level == "H":
        if 4001 <= weight <= 7000:
            print("Time : 45 minutes")
        else:
            print("INVALID INPUT")
    else:
        print("INVALID INPUT")
