print("--------------")
print("This program converts Fahrenheit to Celsius.")
print()
#This takes an input from the console and converts it to a floating point value.
Input=float(input("Enter the Degrees F to be converted to Degrees C:"))
#Conversion factor found on https://www.thoughtco.com/fahrenheit-to-celsius-formula-609230
Celsius=((Input-32)*(5/9))
#This shortens the output to four decimal places.
Output='%.4f' %Celsius
print(Input,"Fahrenheit equals",Output,"Celsius.")
print("--------------")