print("--------------")
print("This program converts MPH to m/s.")
print()
#This takes an input from the console and converts it to a floating point value.
Input=float(input("Enter the ammount of MPH to be converted to m/s:"))
#Conversion factor found on https://www.convertunits.com/from/mph/to/m/s
MpS=(Input*.44704)
#This shortens the output to four decimal places.
Output='%.4f' %MpS
print(Input,"Miles per hour equals",Output,"Meters per Second.")
print("--------------")