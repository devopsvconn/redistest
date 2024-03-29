import redis

# Connect to Redis
r = redis.Redis(host='bsg-dm01-q-930672-unilevercom-redis-02.privatelink.redis.cache.windows.net', port=6379, password='V2g2sqxeXeYPMlVMDjz3UmvjCy86n8KYMAzCaDq2ZAk=')

# Set a key-value pair
r.set('my_key', 'Hello, Redis!')

# Get the value of the key
value = r.get('my_key')
print(value.decode('utf-8'))

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-redis-app
  labels:
    app: python-redis
spec:
  replicas: 1
  selector:
    matchLabels:
      app: python-redis
  template:
    metadata:
      labels:
        app: python-redis
    spec:
      containers:
      - name: python-redis-app
        image: devopsvconn/redistest:latest
        ports:
        - containerPort: 80  # Assuming your Python application runs on port 8080
        env:
        - name: REDIS_HOST
          value: bsg-dm01-q-930672-unilevercom-redis-02.privatelink.redis.cache.windows.net
        - name: REDIS_PORT
          value: "6379"

---
apiVersion: v1
kind: Service
metadata:
  name: python-redis-app
spec:
  selector:
    app: python-redis
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

