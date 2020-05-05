import os
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    UPLOAD_FOLDER = "image-file"
    CSRF_ENABLED = True
    DEBUG = False
    
    # Enter your API Key and Custom Classifier ID below
    API_KEY = "jn7vtmD7ULO6AzRvmv0hKYmhy1FD2gQn7zGZ-8JP0JNC"
    CLASSIFIER_ID = "TablesxBedsandChairs_500051892"
