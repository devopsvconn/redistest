import redis
import os

# Read password from secret
with open('/etc/redis-password/password', 'r') as f:
    redis_password = f.read().strip()

# Connect to Redis
r = redis.Redis(host='bsg-dm01-q-930672-unilevercom-redis-02.privatelink.redis.cache.windows.net', port=6379, password=redis_password)

# Set a key-value pair
r.set('my_key', 'Hello, Redis!')

# Get the value of the key
value = r.get('my_key')
print(value.decode('utf-8'))
