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
// var playername = 
// var fame =
// var class =
// var class_img =
// var rank =
// var star_img =

/*
  $: VALOR OBTENIDO DESDE LA API
  $$: ICONO A ELEGIR DESDE EL DEVELOPER PORTAL
*/

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
        char = converted['character']
        function _getClass() {
          return classes[char];
        }
        rpc.setActivity({
          details: "IGN: $PLAYER",
          state: "Playing as: char",
          startTimestamp: timeStamp,
          largeImageKey: "$$_getClass",
          largeImageText: "$FAME",
          smallImageKey: "$$STAR_IMG",
          smallImageText: "$RANK"
        })
      })
    }, 1000)
    console.log('RPC Connected!')
})

rpc.login({
  clientId: "954113378438246461"
})