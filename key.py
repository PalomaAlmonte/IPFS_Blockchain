import ipfshttpclient

# Connect to the IPFS daemon
client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")

# Retrieve the API key
api_key = client.get_config("API", "Access")

print("API Key:", api_key)
