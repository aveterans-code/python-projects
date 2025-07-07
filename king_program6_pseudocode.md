Geoff King
CIS 110
Assignment 6 - Shipping
April 18, 2024

IPO
I – CSV holding a table of data.
P – use the values in each row to calculate the cost of each package.
O – The shipping charge in a table.

Pseudocode
• Import math, time, and csv
• Assign freight rates into an array
• Define additional fees
• Open the csv into read mode
	o Convert the data into a list named package_data
• Get the header formatted
• Assign the column names from the csv to meaningful names and data types
	o Calculate the basic freight charge
	o Calculate any additional fees
	o Combine charges and fees
	o Format the output center aligned except the total
• Add a bottom border
• End main