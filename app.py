import redis

# Connect to Redis
r = redis.Redis(host='redis-master.dmsng.svc.cluster.local', port=6379, password='UCFl1FUSGe')

# Set a key-value pair
r.set('my_key', 'Hello, Redis!')

# Get the value of the key
value = r.get('my_key')
print(value.decode('utf-8'))