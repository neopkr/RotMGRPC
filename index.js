const exec = require('child_process').exec;
const request = require('request')
const RPC = require('discord-rpc');
const rpc = new RPC.Client({
  transport: 'ipc'
})
const user = require('./user.json')
const game = 'RotMG Exalt.exe'
const url = `https://nightfirec.at/realmeye-api/?player=${user.name}&filter=player+characters+class+fame+`
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

rpc.on('ready', () => {
    setInterval(function() {
      request(url, function(error, res, body) {
        if (error) {
            return console.error(error);
        }
        converted = JSON.parse(res.body)
        // sacar datos del link
      })
    }, 10000)
    console.log('RPC Connected!')
})

rpc.login({
  clientId: "954113378438246461"
})

/* 
      rpc.setActivity({
        details: "default",
        state: "default",
        startTimestamp: "default",
        largeImageKey: "default",
        largeImageText: "default",
        smallImageKey: "default",
        smallImageText: "default"
      })
*/