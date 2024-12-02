import * as redis from 'redis';

// create a redis client
const client = redis.createClient({
  url: 'redis://127.0.0.1:6379',
});

// Connexion to the server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});


// Manage the erros
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) console.log(err);
    redis.print(`Reply: ${reply}`);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) console.log(err);
    redis.print(reply)
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');