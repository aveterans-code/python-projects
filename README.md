Chapter-11 python-projects
Contains basic, entry-level, python modules and sample output

ch11ex5.py (List Manipulation Functions) A collection of custom list manipulation functions.

- Count occurrences of an item
- Check if an item exists in a list
- Find index of an item
- Reverse a list in-place

Methods
  - `count(list, x)`: Count occurrences of x
  - `isin(list, x)`: Check if x is in list
  - `index(list, x)`: Find first index of x
  - `reverse(list)`: Reverse list in-place

Example
Input List: [27, 64, 60, 13, 20, 62, 64, 17, 80, 58, 71, 90]
- Count of 64: 2
- Is 17 in list: True
- Index of 20: 4

ch11ex10.py (Sieve of Eratosthenes Prime Number Generator) An efficient algorithm for finding prime numbers within a given range.

- Generates all prime numbers up to a specified limit
- Implements the classic Sieve of Eratosthenes algorithm
- Demonstrates list manipulation techniques
- Efficient prime number filtering

Example
Input: Upper Limit 200
Output: 
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

ch11ex15.py (Deck of Cards Simulator) An object-oriented implementation of a card deck with shuffling and dealing.

- Create a complete deck of cards
- Shuffle the deck
- Deal a specified number of cards
- Demonstrates object composition
- Uses random card generation

Example
Input: 5 cards to deal
Output:
Jack of Spades (value: 10)
Nine of Hearts (value: 9)
Jack of Diamonds (value: 10)
Ace of Diamonds (value: 1)
Queen of Diamonds (value: 10)
