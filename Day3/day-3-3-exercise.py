# leap year check Challenge

LeapCheck = int(input("Which year do you want to check ? "))

if not LeapCheck % 4:
    if not LeapCheck % 100:
        if not LeapCheck % 400:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
