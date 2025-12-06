#Daily Challenge: "The Temperature Converter"Scenario: You are building a weather app. You need a tool to convert Celsius to Fahrenheit.

def c_to_f(celsius_temp):
	return (celsius_temp*9/5) + 32


celsius = float(input("Enter temperature in C: "))
fahrenheit_temp = c_to_f(celsius)
print(f"That is {fahrenheit_temp} degrees Fahrenheit,")