print("--------------")
print("This program converts seconds per revolution to Hertz.")
print()
#This takes an input from the console and converts it to a floating point value.
Input=float(input("Enter the ammount of sec/rev to be converted to Hertz:"))
#No conversion factor was found online, however hertz is in revolution per second. So we took the inverse of Sec/Rev to find hertz.
Hertz=(1/Input)
#This shortens the output to four decimal places.
Output='%.4f' %Hertz
print(Input,"Seconds per revolution equals",Output,"Hertz.")
print("--------------")