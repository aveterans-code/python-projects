import csv

# Define the freight charge rates
freight_rates = {
    (0, 16): 0.20,
    (16, 32): 0.30,
    (32, 64): 0.40,
    (64, float('inf')): 0.50
}

# Define the additional fees
special_handling_fee = 5
tracking_fee = 5
combined_fee = 7.50

# Read the package data from the CSV file
with open('A6-packages.csv', 'r') as file:
    reader = csv.reader(file)
    #next(reader)  # Skip the header row
    package_data = list(reader)

# Calculate the shipping charges and format the output
print("+" + "-" * 48 + "+")
print("| Weight | Special  | Tracking | Shipping |")
print("|(ounces)| Handling |          |  Charge  |")
print("+" + "-" * 48 + "+")

for weight, special_handling, tracking in package_data:
    weight = int(weight)
    special_handling = special_handling == 'yes'
    tracking = tracking == 'yes'

    # Calculate the freight charge
    for weight_range, rate in freight_rates.items():
        if weight_range[0] <= weight < weight_range[1]:
            freight_charge = weight * rate
            break

    # Calculate the additional fees
    additional_fees = 0
    if special_handling:
        additional_fees += special_handling_fee
    if tracking:
        additional_fees += tracking_fee
    if special_handling and tracking:
        additional_fees = combined_fee

    # Calculate the total shipping charge
    total_charge = freight_charge + additional_fees

    # Format the output
    special_handling_str = "yes" if special_handling else "no"
    tracking_str = "yes" if tracking else "no"
    print("| {weight:>6} | {special_handling:>8} | {tracking:>8} | ${total_charge:>7.2f} |".format(
        weight=weight, special_handling=special_handling_str, tracking=tracking_str, total_charge=total_charge))

print("+" + "-" * 48 + "+")
