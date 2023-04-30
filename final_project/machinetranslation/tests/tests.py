import unittest

from translator import english_to_french, french_to_english

class TestLanguagesTranslation(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(english_to_french) # Test for Null english
        self.assertNotEqual(english_to_french('Hola'), 'Bonjour')
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # Test if Hello is translated to Bonjour
        self.assertIsNotNone(french_to_english) # Test for Null french  
        self.assertNotEqual(french_to_english('Hola'), 'Hello')
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # Test if Bonjour is translated to Hello

unittest.main()
