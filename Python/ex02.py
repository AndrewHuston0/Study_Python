str_fahrenheit = input("fahrenheit: ")
num_fahrenheit = float(str_fahrenheit)

celsius = (num_fahrenheit - 32) / 1.8

print("{0:.2f}℉ => {1:.2f}℃".format(num_fahrenheit, celsius))
