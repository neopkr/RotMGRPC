import platform
import time, os, psutil
from pypresence import Presence
from sys import exit
import requests as r
from datetime import datetime

# Basic discord rich presence requirements
clientID = "954113378438246461"
rpc = Presence(clientID)
rpc.connect()

# Class dictionary (key:value)
classes = {
  'Rogue': 'rogue-icon',
  'Archer': 'archer-icon',
  'Wizard': 'wizard-icon',
  'Priest': 'priest-icon',
  'Warrior': 'warrior-icon',
  'Knight': 'knight-icon',
  'Paladin': 'paladin-icon',
  'Assassin': 'assassin-icon',
  'Necromancer': 'necromancer-icon',
  'Huntress': 'huntress-icon',
  'Mystic': 'mystic-icon',
  'Trickster': 'trickster-icon',
  'Sorcerer': 'sorcerer-icon',
  'Ninja': 'ninja-icon',
  'Samurai': 'samurai-icon',
  'Bard': 'bard-icon',
  'Summoner': 'summoner-icon',
  'Kensei': 'kensei-icon'
}

# Show time elapsed
now = datetime.utcnow()
elapsed = int((now - datetime(1970, 1, 1)).total_seconds())

# Obtain Program's ID (pid)
def _getGame():
  pid = os.getpid()
  return pid

# Get game process according to the OS
def game_():
  if platform.system() == "Windows": return "RotMG Exalt.exe" # Windows process
  else: return "RotMGExalt" # MacOS process
game = game_() in (p.name() for p in psutil.process_iter())

# Verify system to clear the console
def sysVerification():
  if platform.system() == "Windows":
    os.system('cls')
  else:
    os.system('clear')
sysVerification()

# Show introduction of this program to the user with a small disclaimer
print('^*------------RotMG-RPC------------*^')
print('Created by: ether#8677 (IGN: Neruncio) & neokeee#9998 (IGN: Neopkr)')
print('This app loads data from the RealmEye API, not from the game data.')

# Recieve player's IGN
player = input('** Enter you IGN (In-Game Name): ')
print(f'** Loading IGN: {player}')

# Obtain player's data from the RealmEye API, we requested specific data using the API's filter
url = f"https://nightfirec.at/realmeye-api/?player={player}&filter=player+characters+class+fame+rank"

# Possible error responses
error_response = "<Response [500]>"
failed_response = "<Response [400]>"
invalid_player = "Invalid player name"

# -----Main program-----
if game is True:
  print('Realm of the Mad God Exalt RPC Connected!')
  pass
else:
  sysVerification() # Clear console

  # Tell user the game's not open
  print(f'{game_()} is not running! Please start the game and restart the app.')
  time.sleep(2)
  print('Closing...')
  time.sleep(2)
  exit() # Exit program

# While cycle to update data (response delay caused by RealmEye not updating)
while True:
  # Get URL
  res = r.get(url)
  # If the API fails to load data due to reasons, close the program
  if error_response in str(res):
    sysVerification() # Clear console
    
    print("This player cannot be loaded, error: " + error_response)
    exit() # Exit program
  else: pass

  # URL response to JSON
  data = res.json()

  # Exit program if the player is invalid (player non-existent)
  try:
    if invalid_player in data['error']:
      sysVerification() # Clear console

      print(invalid_player)
      print('Invalid player, RPC Closing...')
      time.sleep(2)
      break
  except:
    pass

  # Get the list of characters from the player with the API (keyword: characters)
  charactersList = data['characters']
  
  # If the player has no alive characters, exit the program
  try:
    playingAs = charactersList[0];
  except IndexError:
    sysVerification() # Clear console

    print("This player doesn't have any characters alive.")
    time.sleep(0.5)
    print("Closing...")
    time.sleep(2)
    exit() # Exit program
  
  # Obtain the player's class image using the dictionary
  def _getClass():
    return classes[playingAs['class']]
  
  # Variables
  ign = data['player']
  basefame = playingAs['fame']
  starQty = data['rank']

  # Get small_image with the player's star quantity
  def rank():
    if starQty >= 0 and starQty <= 17:
      return "lightbluestar-icon"
    elif starQty >= 18 and starQty <= 35:
      return "bluestar-icon"
    elif starQty >= 36 and starQty <= 53:
      return "redstar-icon"
    elif starQty >= 54 and starQty <= 71:
      return "orangestar-icon"
    elif starQty >= 72 and starQty <= 89:
      return "yellowstar-icon"
    else:
      return "whitestar-icon"

  # RPC Basic layout
  rpc.update(
    pid = _getGame(), # ProgramID
    state = f"Playing as: {playingAs['class']}", # State
    details = f"IGN: {ign}", # Details
    start = str(elapsed), # Time elapsed
    large_image = _getClass(), # Large Image
    large_text = f'{basefame} BF', # Large Image's hover text
    small_image = rank(), # Small Image
    small_text = str(starQty) # Small Image's hover text 
  )
  
  # Game checker
  game = game_() in (p.name() for p in psutil.process_iter())

  # If the game is not open, exit the program
  if game is False:
    sysVerification()

    print('Game exiting... RPC Exiting.')
    time.sleep(2)
    rpc.close()
    exit() # Exit program
  
  time.sleep(5)