# FILE NAME - convert_C_to_F_01.py

# NAME: Akel Lawrence 
# DATE: 03/09/2025
# BRIEF DESCRIPTION: this program converts C to F baised on user input 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########

print("\n===== Temperature Converter =====\n")
print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius")

choice = input("\nPlease choose from the above menu: ")

if choice == '1':
    temp = float(input("Enter a temperature to convert: "))
    converted = temp * 9 / 5 + 32
    print("\n" + str(temp) + " degrees Celsius is " + str(converted) + " degrees Fahrenheit.\n")

elif choice == '2':
    temp = float(input("Enter a temperature to convert: "))
    converted = (temp - 32) * 5 / 9
    print("\n" + str(temp) + " degrees Fahrenheit is " + str(converted) + " degrees Celsius.\n")

else:
    print("\nInvalid choice. Please enter 1 or 2.")











########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?

float in python gives the progeam the ability to display decimal points. so a float is a decimal number.



2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?

To allow the math to work correctly, if all the numbers were rounded up or down to whole number that will cause large errors in the calculations.



'''
