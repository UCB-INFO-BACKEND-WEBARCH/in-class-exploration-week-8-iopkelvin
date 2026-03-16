from rq.decorators import job
from redis import Redis
import time
import os

redis_conn = Redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/0'))

#Task 1
@job('notifications', connection=redis_conn)
def send_notification(notification_id, email, message):
    print('Starting')
    time.sleep(3)
    print("Done")
    return {"notification_id": notification_id,
            "email": email,
            "status": message.status,
            "sent_at": message.sent_at
            }
