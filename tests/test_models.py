import unittest
from app.models import User, Post,Comment, Role
from datetime import datetime



class UserModelTest(unittest.TestCase):
    '''
    Test to run before any other tests
    '''

    
    def setUp(self):
        self.new_user = User(email = 'james@ms.com',
                              username = 'gabi',
                              password = 'cat') 
        
            
    def setUp(self):
        self.new_user = User(password = 'cat')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)
        
        
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('cat'))
        
    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)
        
        

class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Posts class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post(1,
                             'Python Must Be Crazy',
                             '2019-04-25 08:26:19.580874',
                             1,
                             'hospitality',
                             'thrilling')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))
        
        
class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment(1,
                             'Comment body',
                             '2019-04-25 08:26:19.580874 ',
                             1,
                             1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

if __name__ == '__main__':
    unittest.main()