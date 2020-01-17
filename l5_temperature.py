# ---------------------------------------------------------------
# ANOTHER Input Process Output Example
# CS110Z - Lesson 5
# ---------------------------------------------------------------

# STEP 1:  GET THE INPUTS (i.e., input)
degrees_fahrenheit = float(input())

# STEP 2:  PROCESS (i.e., do math)
degrees_celsius = (degrees_fahrenheit - 32) * 5/9
degrees_kelvin = degrees_celsius + 273.15

# STEP 3:  OUTPUT (i.e., print)
print(degrees_kelvin)
print(degrees_celsius)