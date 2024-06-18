"""Prompt 2: Please give me an example of python code to make a  simple script where if you put in Fahrenheit it gives Celsius but if you put in Celsius temperature it gives you Fahrenheit. 

This will need a Python interpreter or IDE. 

Copy it in and run it, see how well it works. 

Code 2: 
Written by Vincent Hall of Build Intellect Ltd. and ABT NEWS Ltd. 12 Feb 2024.""" 

def convert_temperature(temperature, unit): 

  if unit.lower() == "f": 

    celsius = (temperature - 32) * 5 / 9 

    return celsius, "Celsius" 

  elif unit.lower() == "c": 

    fahrenheit = temperature * 9 / 5 + 32 

    return fahrenheit, "Fahrenheit" 

  else: 

    return None, "Invalid unit" 

 

# Example usage 

temperature = float(input("Enter temperature: ")) 

unit = input("Enter unit (F/C): ") 

 

result, new_unit = convert_temperature(temperature, unit) 

 

if result is not None: 

  print(f"{temperature} {unit} is equal to {result} {new_unit}") 

else: 

  print("Invalid input") 

 
