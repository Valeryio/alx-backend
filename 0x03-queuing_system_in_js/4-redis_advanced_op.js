import * as redis from  'redis';

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


client.hset('HolbertonSchools', 'Portland', 50,(err, count) => {
  if (err) console.error(err);
  redis.print(`Reply: ${count}`);
});

client.hset('HolbertonSchools', 'Seattle', 80,(err, count) => {
    if (err) console.error(err);
    redis.print(`Reply: ${count}`);
});

client.hset('HolbertonSchools', 'New York', 20,(err, count) => {
    if (err) console.error(err);
    redis.print(`Reply: ${count}`);
});

client.hset('HolbertonSchools', 'Bogota', 20,(err, count) => {
    if (err) console.error(err);
    redis.print(`Reply: ${count}`);
});

client.hset('HolbertonSchools', 'Cali', 40,(err, count) => {
    if (err) console.error(err);
    redis.print(`Reply: ${count}`);
});

client.hset('HolbertonSchools', 'Paris', 2,(err, count) => {
    if (err) console.error(err);
    redis.print(`Reply: ${count}`);
});

client.hgetall("HolbertonSchools", (err, hash) => {
  if (err) console.error(err);
  console.log(hash);
})