import base64

# Read the Base64 encoded data from your file
with open("encoded_data.txt", "r") as file:
    base64_data = file.read()

# Decode and save as zip
with open("part15.zip", "wb") as zip_file:
    zip_file.write(base64.b64decode(base64_data))
