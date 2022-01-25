print("--------------")
print("This program converts Pascals to milimeters of mercury.")
print()
#This takes an input from the console and converts it to a floating point value.
Input=float(input("Enter the Pascals to be converted to mmHg:"))
#Conversion factor found on https://www.advancedconverter.com/unit-conversions/pressure-conversion/pascals-to-mmhg
Pascals=Input*0.007501
#This shortens the output to four decimal places.
Output='%.4f' %Pascals
print(Input,"Pascals is equal to",Output,"Milimeters of mercury.")
print("--------------")