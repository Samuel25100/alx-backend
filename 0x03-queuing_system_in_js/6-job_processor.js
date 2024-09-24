import { createQueue } from 'kue';
const que = createQueue();


function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

que.process('push_notification_code', (job) => {
	sendNotification(job.data.phoneNumber, job.data.message);
});
