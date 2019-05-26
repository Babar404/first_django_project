from django.test import SimpleTestCase

# Create your tests here.

'''
    That’s a fancy way of saying it ensures that a given webpage actually exists, but says
nothing about the content of said page.
'''

class SimpleTests(SimpleTestCase): #ye test case ki class hai


    def test_home_page_status_code(self):   #home page k liye test func banaya hai
        response = self.client.get('/')  
        self.assertEqual(response.status_code, 200)


    def test_about_page_status_code(self):  #about page k liye test func banaya hai
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)