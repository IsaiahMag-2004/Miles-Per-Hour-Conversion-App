#Unit 1 Challanger 2 Miles Per Hour Converter App

print("Welcome to the Miles Per Hour Conversion App")
print()

#Get speed
miles_per_hour = input("What is your speed in miles per hour: ")

#Convert and round
miles_per_hour = float(miles_per_hour)
kilometers = miles_per_hour / 2.237
kilometers = round(kilometers, 2)

#Cast, and output
kilometers = str(kilometers)
print("Your speed in meters per second is " + kilometers + ".")
