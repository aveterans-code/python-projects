Geoff King
CIS 110
Assignment 7 - Windchill
April 18, 2024
IPO
I – none
P – formula for windchill
O – table of windchill values

Notes: If the windspeed is less than 3 MPH, the wind chill index is zero and the temperature =
temperature.
Rows should represent wind speed from 0 to 50 in 5 mph increments, and the columns
represent temperatures from -20 to +60 in 10-degree increments.
Outerloop – MPH
Innerloop – Temperature

Pseudocode
• Import time.
• Create windChill(t, v) function – calculates wind chill for given temperature and wind
speed velocity.
	o if wind speed (v) is 3MPH or less just return the temperature (t).
	o else wind speed is more than 3MPH use the formula: 35.74 + 0.6215t – 35.75(v**0.16) + 0.4275t(v**0.16).
		-Return the wind chill as an integer for the given temperature and wind speed.
• Create the main() function.
	o Print the intro.
	o Print the table header and column headers (mph).
	o Create a for loop based on the MPH that starts at zero and increases in increments of 5 up to 50.
	o Print MPH.
		-Create a for loop based on the temperature that increases in increments of 10 from -20 to 60.
		-Initialize the windChill(t, v) function using current MPH and temperature values from the for loops.
		-Print the returned windChill.
• End main