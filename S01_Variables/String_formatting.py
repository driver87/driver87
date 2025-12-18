#Formatting numbers for printing in python

x = 3121.14592653589793

print(f"x is approximately {x:.6}") # Show 6 figures.

print("{: .6}".format(x)) #using format method

print(f"{x: .3}") # Show 3 figures only as our number has more figures before the decimal point so we get the exponent notation

print(f"{x: .3f}") # Shows 3 figures after the decimal point. Also rounds the number.

print(f"{x: f}") # Default is 6 figures after the decimal point.

print(f"{x: _}") # Seperate thousands by underscore

print(f"{x: ,}") # Seperate thousands by comma

print(f"{x: _.6f}") # Combine both underscore and 6 figures after decimal point.

print(f"{x: ,.6f}") # Combine both comma and 6 figures after decimal point.

