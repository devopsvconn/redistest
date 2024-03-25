import redis

# Connect to Redis
r = redis.Redis(host='bsg-dm01-q-930672-unilevercom-redis-02.privatelink.redis.cache.windows.net', port=6379, password='V2g2sqxeXeYPMlVMDjz3UmvjCy86n8KYMAzCaDq2ZAk=')

# Set a key-value pair
r.set('my_key', 'Hello, Redis!')

# Get the value of the key
value = r.get('my_key')
print(value.decode('utf-8'))
