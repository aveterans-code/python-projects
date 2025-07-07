"""
Program name: king_program6.py
Program Description: Shipping
Author: Geoff King
Date Created: April 15, 2024

Notes: Imports the python time library and a csv

"""
import csv, time

def main():
    #define the basic freight charge rates in an array
    freight_rates = {
        (0, 16): 0.20,
        (16, 32): 0.30,
        (32, 64): 0.40,
        (64, float('inf')): 0.50
    }

    #define the additional fees
    special_handling_fee = 5
    tracking_fee = 5
    combined_fee = 7.50

    #read the package data from the CSV file
    with open('A6-packages.csv', 'r') as file:
        reader = csv.reader(file)
        #creates a list from the csv
        package_data = list(reader)

    #format the header of the table with top, bottom, and side borders
    print("+" + "-" * 41 + "+")
    print("| Weight | Special  | Tracking | Shipping |")
    print("|(ounces)| Handling |          |  Charge  |")
    print("+" + "-" * 41 + "+")

    #assign weight the int value from the csv and boolean type values for handling and tracking
    for weight, special_handling, tracking in package_data:
        weight = int(weight)
        special_handling = special_handling == 'yes'
        tracking = tracking == 'yes'

        #calculate the basic freight charge
        for weight_range, rate in freight_rates.items():

            if weight_range[0] <= weight < weight_range[1]:
                freight_charge = weight * rate
                break

        #calculate the additional fees
        additional_fees = 0
        if special_handling:
            additional_fees += special_handling_fee
        if tracking:
            additional_fees += tracking_fee
        if special_handling and tracking:
            additional_fees = combined_fee

        #calculate the total shipping charge
        total_charge = freight_charge + additional_fees

        #format the output
        special_handling_str = "yes" if special_handling else "no"
        tracking_str = "yes" if tracking else "no"
        print("| {weight:^6} | {special_handling:^8} | {tracking:^8} | ${total_charge:>7.2f} |".format(
            weight=weight, special_handling=special_handling_str, tracking=tracking_str, total_charge=total_charge))
        
    #adds a bottom border
    print("+" + "-" * 41 + "+")

#adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 program6")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

main()

