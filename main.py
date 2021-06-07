from replit import clear
from art import logo


bidders = []
is_bidder_rest = True
def add_bidder(name, price):
  bidders.append(
    {
      "name": name,
      "price": price
    }
  )
def max_bidder(bidders_arr):
  max = 0
  winner = ''
  for bidder in bidders_arr:
    if bidder['price'] > max:
      max = bidder['price']
      winner = bidder['name']

  print(f"The winner is {winner}")


print(logo)
print("Welcome to the secret auction program")
name = " "
price = 0

while is_bidder_rest:
  name = input("What is your name? ")
  price = int(input("What's your bid? $"))

  add_bidder(name, price)
  others_bidders = input("Are there any other bidders").lower()

  if others_bidders == 'yes':
    clear()
    add_bidder(name, price)
  elif others_bidders == 'no':
    max_bidder(bidders)
    is_bidder_rest = False

  
