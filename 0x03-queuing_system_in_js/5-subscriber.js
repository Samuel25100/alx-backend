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
});

client.subscribe('holberton school channel');

client.on('message', (err, msg) => {
	if (msg === "KILL_SERVER") {
		client.unsubscribe('holberton school channel');
		console.log(msg);
		client.quit();
	}
	console.log(msg);
});
