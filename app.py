import redis
import base64

redis_password_secret = "redis"  # Replace with the name of your secret
namespace = "dmsng"

secret_data = kubectl.get_secret(redis_password_secret, namespace)
redis_password = base64.b64decode(secret_data["data"]["redis-password"]).decode("utf-8")

# Connect to Redis
r = redis.Redis(host='redis-headless.dmsng.svc.cluster.local', port=6379, password=redis_password)

# Set a key-value pair
r.set('my_key', 'Hello, Redis!')

# Get the value of the key
value = r.get('my_key')
print(value.decode('utf-8'))