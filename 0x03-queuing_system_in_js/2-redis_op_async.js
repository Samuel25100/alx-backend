import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient({
	host: 'localhost',
	port: 6379
});
client.on('error', (err) => {
	console.log('Redis client not connected to the server:' + err);
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, (err, reply) => {
		print('Reply: ' + reply);
	});
}

async function displaySchoolValue(schoolName) {
	console.log(await promisify(client.get).bind(client)(schoolName));

}
async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});
