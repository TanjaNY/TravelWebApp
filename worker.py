import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn1 = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn1):
        worker = Worker(map(Queue, listen))
        worker.work()
