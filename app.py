import redis
import base64
from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

secret = v1.read_namespaced_secret("redis", "dmsng")
password = base64.b64decode(secret.data['password']).decode()

# Connect to Redis
r = redis.Redis(host='redis-headless.dmsng.svc.cluster.local', port=6379, password=password)

# Set a key-value pair
r.set('my_key', 'Hello, Redis!')

# Get the value of the key
value = r.get('my_key')
print(value.decode('utf-8'))