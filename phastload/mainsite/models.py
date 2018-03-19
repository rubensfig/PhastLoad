from django.db import models

# Create your models here.
class Files:
    def __init__(self, uuid, expiration, ac):
        self.uuid = uuid
        self.expiration = expiration
        self.access_code = ac

    def deletion(self):
        if self.expiration == 0:
            return True

        return False
