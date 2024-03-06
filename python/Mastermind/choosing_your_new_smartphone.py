opcion = input("Do you prefer:\n"
               "A- ISO\n"
               "B- Android\n"
               "Response: ")

movil_ideal = "None"

# ISO
if opcion == "A":
    opcion = input("Do you have money:\n"
                   "A- Yes\n"
                   "B- No\n"
                   "Response: ")

    if opcion == "A":
        movil_ideal = "Iphone Ultra Pro Max"

    elif opcion == "B":
        movil_ideal = "Iphone segunda mano"

    else:
        print("Your response is invalid")
        exit()

# Android
elif opcion == "B":
    opcion = input("Do you have money:\n"
                   "A- Yes\n"
                   "B- No\n"
                   "Response: ")

    if opcion == "A":
        opcion = input("Do you mind the camera\n"
                       "A- Yes\n"
                       "B- No\n"
                       "Response: ")

        if opcion == "A":
            movil_ideal = "Google Pixel Supercamar"

        elif opcion == "B":
            movil_ideal = "Android price quality"

        else:
            print("Your response is invalid")
            exit()

    elif opcion == "B":
        movil_ideal = "Android chinese of 100$"

    else:
        print("Your response is invalid")
        exit()

else:
    print("your response is invalid")
    exit()

print("\n" + "Your ideal phone is {}".format(movil_ideal))
