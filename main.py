import time, os
from pypresence import Presence
import requests as r
from datetime import datetime

clientID = "954113378438246461"
rpc = Presence(clientID)
rpc.connect()

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

now = datetime.utcnow()
elapsed = int((now - datetime(1970, 1, 1)).total_seconds())

def _getGame():
  pid = os.getpid()
  return pid

print('^*------------RotMG-RPC------------*^')
print('Created by: ether#8677 (IGN: Neruncio) & neokeee#9998 (IGN: Neopkr)')
print('This app loads data from RealmEye API, not from the game data.')
player = input('** IGN (In-Game Name): ')
print(f'** Loading IGN: {player}')

url = f"https://nightfirec.at/realmeye-api/?player={player}&filter=player+characters+class+fame+rank"
error_response = "<Response [500]>"
failed_response = "<Response [400]>"

while True:
  res = r.get(url)
  if error_response in str(res):
    print("This player cannot be loaded")
    quit()
  else: pass
  data = res.json()

  charactersList = data['characters']
  try:
    playingAs = charactersList[0];
  except IndexError:
    print("This player doesn't have any characters alive.")
    quit()
  
  def _getClass():
    return classes[playingAs['class']]
    
  ign = data['player']
  basefame = playingAs['fame']
  starQty = data['rank']

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

  rpc.update(
    pid = _getGame(),
    state = f"Playing as: {playingAs['class']}",
    details = f"IGN: {ign}",
    start = str(elapsed),
    large_image = _getClass(),
    large_text = f'{basefame} BF',
    small_image = rank(),
    small_text = str(starQty)
  )
    
  time.sleep(60)