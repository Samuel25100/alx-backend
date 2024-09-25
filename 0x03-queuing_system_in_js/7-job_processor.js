import { createQueue } from 'kue';
const que = createQueue();
const blk_list = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  if (blk_list.includes(phoneNumber)) {
	  done(new Error(`Phone number ${phoneNumber} is blacklisted`));
	  return;
  }
  const intrv = setInterval(() => {
     let comp = 0;
     const tot = 2;
     job.progress(tot, comp);
     if (comp == 1) {
        console.log(`Sending notification to ${phoneNumber},`,
        ` with message: ${message}`);
     }
     if (comp >= tot) {
	clearInterval(intrv);
	done();
     } else {
	comp += 1;
     }
  }, 1000);
}

que.process('push_notification_code_2', 2, (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
