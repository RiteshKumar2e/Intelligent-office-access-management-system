from pymongo import MongoClient

# Define your MongoDB Atlas connection string with correct credentials and cluster info
uri = "mongodb+srv://riteshkumar90359:hYv3imAgIWRKEHmg@cluster0.n9mmmbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB Atlas
client = MongoClient(uri)

# Try to ping the MongoDB server
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Failed to connect to MongoDB:", e)

# Access your specific database and collection
db = client["office_access"]
collection = db["employees"]
