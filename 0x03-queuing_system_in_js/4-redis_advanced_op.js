import { createClient, print } from 'redis';

const client = createClient({
        host: 'localhost',
        port: 6379
});
client.on('error', (err) => {
        console.log('Redis client not connected to the server:' + err);
});
client.on('ready', async () => {
  console.log('Redis client connected to the server');
  main();
});
function main() {
	const obj = {'Portland': 50, 'Seattle': 80,
		     'New York': 20, 'Bogota': 20,
		     'Cali': 40, 'Paris': 2};
	for (let i in obj) {
		client.hset('HolbertonSchools', i, obj[i], print);
	}
	client.hgetall('HolbertonSchools', (err, reply) => {
	        console.log(reply);
	});
}
