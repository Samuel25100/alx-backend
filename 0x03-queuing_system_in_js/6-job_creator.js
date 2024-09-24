import { createQueue } from 'kue';
const que = createQueue();
const job = que.create('push_notification_code', {
  'phoneNumber': '0758938234',
  'message': 'Mels Phone Number',
});

job.on('failed', () => {
	console.log("Notification job failed");
});
job.on('enqueue', () => {
	console.log("Notification job created: " + job.id);
});
job.on('complete', (id) => {
        console.log("Notification job completed");
});
job.save();
