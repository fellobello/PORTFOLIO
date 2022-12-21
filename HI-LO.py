# List to store the cards that have been played
cards = []
valid_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 'j', 'q', 'k', 'a']

# Current count and number of decks remaining
count = 0
decks_remaining = 4

def update_count(card):
  """Updates the count based on the Hi-Lo system"""
  global count
  if card not in valid_ranks:
    print("Invalid card rank. Please enter a valid card rank.")
    return
  if card in ['2', '3', '4', '5', '6']:
    count += 1
  elif card in ['7', '8', '9']:
    count += 0
  elif card in ['10', 'J', 'Q', 'K', 'A', 'j', 'q', 'k', 'a']:
    count -= 1

def calc_true_count():
  """Calculates the true count based on the current count and number of decks remaining"""
  true_count = count / decks_remaining
  return round(true_count)

# Main game loop
while True:
 
  # Prompt the user to input the rank of the next card
  card = input("Enter the rank of the next card (or 'done' to end the game): ")
  if card == 'done':
    break
  # Check if the input is a valid card rank
  update_count(card)
  if card not in valid_ranks:
    continue

  # Update the list of cards and the count
  cards.append(card)
  
  # Check if a full deck has been played and update the number of decks remaining accordingly
  if len(cards) % 52 == 0 and decks_remaining > 1:
    decks_remaining -= 1
  
  # Calculate and print the true count
  true_count = calc_true_count()
  print("True count:", true_count)
