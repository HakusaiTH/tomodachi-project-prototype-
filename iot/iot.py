import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("D:\\tomodachi\\ai\\led-iot-c29ca-firebase-adminsdk-r8xds-687021e5e8.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://led-iot-c29ca-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Read data from the Realtime Database
ref = db.reference('/tem')
data = ref.get()
print(data)

"""
# Write data to the Realtime Database
ref.set({'some_key': 'some_value'})
"""
