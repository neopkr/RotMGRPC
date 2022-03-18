const exec = require('child_process').exec;
const request = require('request')
const RPC = require('discord-rpc');
const rpc = new RPC.Client({
  transport: 'ipc'
})
const user = require('./user.json')
const game = 'RotMG Exalt.exe'
const url = `https://nightfirec.at/realmeye-api/?player=${user.name}&filter=player+characters+class+fame+rank`
const isRunning = (query, cb) => {
  let platform = process.platform;
  let cmd = '';
  switch (platform) {
    case 'win32' : cmd = `tasklist`; break;
    case 'darwin' : cmd = `ps -ax | grep ${query}`; break;
    case 'linux' : cmd = `ps -A`; break;
    default: break;
  }
  exec(cmd, (err, stdout, stderr) => {
    cb(stdout.toLowerCase().indexOf(query.toLowerCase()) > -1);
  });
}

var timeStamp = Date.now() / 1000 | 0;

const classes = {
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

rpc.on('ready', () => {
    setInterval(function() {
      request(url, function(error, res, body) {
        if (error) {
          return console.error(error);
        }
        converted = JSON.parse(res.body)

        // Del array de personajes, sacar el primero
        char = converted[`characters`]
        playingAs = char[0]
        function _getClass() {
          return classes[playingAs[`class`]];
        }
        //console.log(_getClass())

        IGN = converted[`player`]
        basefame = playingAs[`fame`]
        starQuantity = converted[`rank`]

        function rank() {
          if (starQuantity >= 0 && starQuantity <= 17) {
            return "lightbluestar-icon"
          }
          else if (starQuantity >= 18 && starQuantity <= 35){
            return "bluestar-icon"
          }
          else if (starQuantity >= 36 && starQuantity <= 53){
            return "redstar-icon"
          }
          else if (starQuantity >= 54 && starQuantity <= 71){
            return "orangestar-icon"
          }
          else if (starQuantity >= 72 && starQuantity <= 89){
            return "yellowstar-icon"
          }
          else {
            return "whitestar-icon"
          }
        }

        rpc.setActivity({
          details: `IGN: ${IGN}`,
          state: `Playing as: ${playingAs[`class`]}`,
          startTimestamp: timeStamp,
          largeImageKey: _getClass(),
          largeImageText: `${basefame} BF`,
          smallImageKey: rank(),
          smallImageText: starQuantity.toString()
        })
      })
    }, 5000)
    console.log('RPC Connected!')
})

rpc.login({
  clientId: "954113378438246461"
})