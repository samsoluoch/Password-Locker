import unittest
from credential_data import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):

        self.new_credential = Credential("samsoluoch", "password", "twitter")

    def test_init(self):
        self.assertEqual(self.new_credential.username, "samsoluoch")
        self.assertEqual(self.new_credential.password, "password")
        self.assertEqual(self.new_credential.website, "twitter")

    def tearDown(self):
        '''
        tearDown() method that cleans up after every run
        '''
        Credential.credential_list = []

# test 1
#save_credential
    def test_save_credential(self):
        '''
        save_credential method for saving the new credential object by appending it to the credential_list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)


# test 2
# save_multiple_credentials
    def test_save_multiple_credentials(self):
        '''
        save_multiple_credentials test method that tests if we can save multiple credentials
        '''
        self.new_credential.save_credential()
        test_credential = Credential("samsoluoch", "pass1", "twitter")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

# test 3
# delete_credential
    def test_delete_credential(self):
        '''
        delete_credential method that removes a credential object from the credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("samsoluoch", "pass1", "twitter")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)


# test 3
# finding credential using website
    def test_find_by_website(self):
        '''
        test for finding credentials using website whose credentials are in the object.
        '''
        self.new_credential.save_credential()
        test_credential = Credential("samsoluoch", "pass1", "twitter")
        test_credential.save_credential()

        found_credential = Credential.find_by_website("twitter")
        
        self.assertEqual(found_credential.website, test_credential.website)


# test 4
# testing existence of a credential
    def test_credential_exists(self):
        '''
        test method that checks if a credential exists
        '''
        self.new_credential.save_credential()
        test_credential = Credential("samsoluoch", "pass1", "twitter")
        test_credential.save_credential()

        credential_exists = Credential.credential_exists("twitter")
        self.assertTrue(credential_exists)

# test 5
# receining a list of credentials
    def test_display_credential(self):
        '''
        test method that checks if we can display a list of all the credentials
        '''
        self.assertTrue(Credential.display_credential(), Credential.credential_list)






if __name__ == '__main__':
    unittest.main()