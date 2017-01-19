from django.test import TestCase
from mainsite.models import Files

# Create your tests here.

class FilesTest(TestCase):
    def setUp(self):
        Files(1, 0, 'ABCD')        

    def test_deletion(self):
        self.assertTrue(Files(1, 0, 'ABCD'))
