# CSE 101, Assignment 1, Problem 2

def celsiusToFahrenheit(celsius):
    farhan = (celsius * 9/5) + 32
    return farhan
    
# Now, test the celsiusToFarenheit function defined above.
# This is an example of 3 different test cases to test the function.
print('celsiusToFahrenheit:')
print('celsiusToFahrenheit(100) = ' + str(celsiusToFahrenheit(100)))    # Should be 212
print('celsiusToFahrenheit(0) = ' + str(celsiusToFahrenheit(0)))        # Should be 32
print('celsiusToFahrenheit(-40) = ' + str(celsiusToFahrenheit(-40)))    # Should be -40
