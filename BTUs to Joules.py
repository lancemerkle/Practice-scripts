print("--------------")
print("This program converts BTUs to Joules.")
print()
#This takes an input from the console and converts it to a floating point value.
Input=float(input("Enter the BTUs to be converted to Joules:"))
#Conversion factor found on https://www.rapidtables.com/convert/energy/BTU_to_Joule.html
BTUs=Input*1055.05585
#This shortens the output to four decimal places.
Output='%.4f' %BTUs
print(Input,"BTUs is equal to",Output,"Joules.")
print("--------------")