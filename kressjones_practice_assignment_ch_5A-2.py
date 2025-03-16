# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program is a command line kilometer to miles converter. 
# The user is prompted to input the desired kilometer distance that they want converted into miles. 
# The conversion is calculated. At the end the km and converted mile distance is printed to the command line. 

KM_TO_MILES_FACTOR = 0.6214

def main():
    print("This program converts a kilometer distance into miles.")
    km = float(input("Please enter the kilometer distance: "))
    km_to_miles(km)

def km_to_miles(distance):
    distance_miles = distance * KM_TO_MILES_FACTOR
    print(f"\n{distance} km are {distance_miles:.2f} miles.")

if __name__=="__main__":
    main()
