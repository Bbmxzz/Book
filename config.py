import os

class Config:
    FIREBASE_ADMIN_CREDENTIALS = "bookai-7cf88-firebase-adminsdk-a4x7v-0b958e4360.json"
    ROBOFLOW_API_KEY = "GjIhJ9A525bYsGiVQIRA"
    FIREBASE_STORAGE_BUCKET = "bookai-7cf88.appspot.com"

# Load environment variables if needed
Config.FIREBASE_ADMIN_CREDENTIALS = os.getenv("FIREBASE_ADMIN_CREDENTIALS", Config.FIREBASE_ADMIN_CREDENTIALS)
Config.ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY", Config.ROBOFLOW_API_KEY)
Config.FIREBASE_STORAGE_BUCKET = os.getenv("FIREBASE_STORAGE_BUCKET", Config.FIREBASE_STORAGE_BUCKET)
