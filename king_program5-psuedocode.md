Geoff King
CIS 110
Assignment 5 - square
March 31, 2024

IPO
Input- a number ‘n’ from user.
Process- replace the current value with the square of the current value in a list of values, in
place.
Output- modified list of square values.

Pseudocode
• Import math and time libraries.
• Create the square(nums) function with the parameter of nums.
	o Create a for loop to modify each nums in the list.
		▪ Replace each number in the nums list with its squared value, inplace.
		▪ No return statement needed
• Create the main() function.
	o Print intro.
	o Prompt user for input of how many numbers ‘n’ to square. Assign to ‘n’.
	o Declare a list ‘nums’ that will hold ‘n’ amount of numbers.
	o Print the original list ‘nums’.
	o Create a counted for loop (3).
		▪ Each iteration should call the square function with parameter nums.
		▪ Each iteration should print the updated list.
• Personal/course info.
• End main.