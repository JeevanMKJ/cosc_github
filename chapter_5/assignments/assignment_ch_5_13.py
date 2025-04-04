"""
In physics, an object that is in motion is said to have kinetic energy.
The following formula can be used to determine a moving object’s kinetic energy:
KE=1⁄2 * mv ** 2
The variables in the formula are as follows:
KE is the kinetic energy,
m is the object’s mass in kilograms, and
v is the object’s velocity in meters per second.

Write a function named kinetic_energy that accepts an object’s mass (in kilograms)
and velocity (in meters per second) as arguments.
The function should return the amount of kinetic energy that the object has.
Write a program that asks the user to enter values for mass and velocity,
then calls the kinetic_energy function to get the object’s kinetic energy.
"""

def main():
    kinetic_energy()


def kinetic_energy():
    constant = 0.5

    while True:
        mass = input("Enter mass in kg: ")
        velocity = input("Enter velocity as m/s: ")
        if mass.isdigit() and velocity.isdigit():
            mass = float(mass)
            velocity = float(velocity)
            break
        else:
            print("ERROR. Enter ONLY numbers.")

    ke = constant * (mass * (velocity ** 2))
    print(f"Kinetic energy of moving object: {ke:.2f} joules.")


if __name__ == '__main__':
    main()
