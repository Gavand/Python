import unittest, sys, io
from contextlib import redirect_stdout
from unittest.mock import patch
from conditions import *


class TestConditions(unittest.TestCase):

    def test_word_length(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(word_length('liversnaps', 7))
            self.assertEqual('Longer than 7 characters: liversnaps\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            word_length('earwax', 5)
            self.assertEqual('Longer than 5 characters: earwax\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            word_length('chickenfat', 10)
            self.assertEqual('Exactly 10 characters: chickenfat\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            word_length('Gross!', 13)
            self.assertEqual('Shorter than 13 characters: Gross!\n', buf.getvalue())

    def test_stop_light(self):
        self.assertEqual('yellow', stop_light('green',61))
        self.assertEqual('green', stop_light('green',60))
        self.assertEqual('green', stop_light('green',59))
        self.assertEqual('yellow', stop_light('yellow',5))
        self.assertEqual('red', stop_light('yellow',6))
        self.assertEqual('red', stop_light('red',12))
        self.assertEqual('green', stop_light('red',56))
        self.assertEqual('red', stop_light('red',54))

    def test_is_normal_blood_pressure(self):
        self.assertFalse(is_normal_blood_pressure(120, 80))
        self.assertFalse(is_normal_blood_pressure(119, 80))
        self.assertTrue(is_normal_blood_pressure(119, 79))
        self.assertFalse(is_normal_blood_pressure(120, 79))
        self.assertFalse(is_normal_blood_pressure(120, 80))
        self.assertFalse(is_normal_blood_pressure(133, 79))
        self.assertTrue(is_normal_blood_pressure(110, 78))

    def test_doctor(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('builtins.input', side_effect=[119, 79]): 
                self.assertIsNone(doctor())
                self.assertEquals("Your blood pressure is normal.\n",buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('builtins.input', side_effect=[133, 79]): 
                doctor()
                self.assertEquals("Your blood pressure is high.\n",buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('builtins.input', side_effect=[120, 80]): 
                doctor()
                self.assertEquals("Your blood pressure is high.\n",buf.getvalue())


    def test_pants_size(self):
        self.assertIsNotNone(pants_size(38))
        self.assertEqual("large", pants_size(34))
        self.assertEqual("large", pants_size(38))
        self.assertEqual("large", pants_size(50000))
        self.assertEqual("medium", pants_size(30))
        self.assertEqual("medium", pants_size(33))
        self.assertEqual("small", pants_size(1))
        self.assertEqual("small", pants_size(29))
        self.assertEqual("small", pants_size(-20))
        self.assertEqual("small", pants_size(0))
 
    def test_pants_fitter(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('builtins.input', side_effect=['Ziggy', 34, 2, 'fancy']): 
                self.assertIsNone(pants_fitter())
                self.assertEquals('Greetings Ziggy welcome to Pants-R-Us\n' +
                    '2 pairs of large fancy pants: $ 200\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('builtins.input', side_effect=['Elmer', 31, 10, 'regular']): 
                pants_fitter()
                self.assertEquals('Greetings Elmer welcome to Pants-R-Us\n' +
                    '10 pairs of medium regular pants: $ 400\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('builtins.input', side_effect=['Minnie', 12, 1, 'fancy']): 
                pants_fitter()
                self.assertEquals('Greetings Minnie welcome to Pants-R-Us\n' +
                    '1 pairs of small fancy pants: $ 100\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('builtins.input', side_effect=['Henry', 30, 4, 'regular']): 
                pants_fitter()
                self.assertEquals('Greetings Henry welcome to Pants-R-Us\n' +
                    '4 pairs of medium regular pants: $ 160\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('builtins.input', side_effect=['Ali Smith', -10, 90, 'fancy']): 
                pants_fitter()
                self.assertEquals('Greetings Ali Smith welcome to Pants-R-Us\n' +
                    '90 pairs of small fancy pants: $ 9000\n', buf.getvalue())

    def test_digdug(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(digdug(1))
            self.assertEqual('', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            digdug(2)
            self.assertEqual('', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            digdug(3)
            self.assertEqual('3 : dig\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            digdug(5)
            self.assertEqual('3 : dig\n5 : dug\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            digdug(8)
            self.assertEqual('3 : dig\n5 : dug\n6 : dig\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            digdug(15)
            self.assertEqual('3 : dig\n5 : dug\n6 : dig\n9 : dig\n'  
                + '10 : dug\n12 : dig\n15 : digdug\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            digdug(30)
            self.assertEqual('3 : dig\n5 : dug\n6 : dig\n9 : dig\n'  
                + '10 : dug\n12 : dig\n15 : digdug\n18 : dig\n'
                + '20 : dug\n21 : dig\n24 : dig\n25 : dug\n' 
                + '27 : dig\n30 : digdug\n', buf.getvalue())

    def test_beef_type(self):
        self.assertIsNotNone(beef_type(91.2))
        self.assertEqual("Sirloin", beef_type(91.2))
        self.assertEqual("Chuck", beef_type(78.0))
        self.assertEqual("Round", beef_type(87))
        self.assertEqual("Hamburger", beef_type(0))
        self.assertEqual("Hamburger", beef_type(50.1))
        self.assertEqual("Chuck", beef_type(80))
        self.assertEqual("Chuck", beef_type(84))
        self.assertEqual("Round", beef_type(85.0))
        self.assertEqual("Round", beef_type(89.9999))
        self.assertEqual("Sirloin", beef_type(90))
        self.assertEqual("Sirloin", beef_type(95))
        self.assertEqual("Unknown", beef_type(95.1))
        self.assertEqual("Unknown", beef_type(100))

    def test_species_height(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(species_height('Human', 62.1))
            self.assertEqual('Below Average\n', buf.getvalue()) 
        with io.StringIO() as buf, redirect_stdout(buf):
            species_height('Human', 67)
            self.assertEqual('Average\n', buf.getvalue()) 
        with io.StringIO() as buf, redirect_stdout(buf):
            species_height('Human', 67.999999)
            self.assertEqual('Above Average\n', buf.getvalue()) 
        with io.StringIO() as buf, redirect_stdout(buf):
            species_height('Klingon', 73)
            self.assertEqual('Above Average\n', buf.getvalue()) 
        with io.StringIO() as buf, redirect_stdout(buf):
            species_height('Klingon', 71)
            self.assertEqual('Average\n', buf.getvalue())   
        with io.StringIO() as buf, redirect_stdout(buf):
            species_height('Klingon', 70.9)
            self.assertEqual('Below Average\n', buf.getvalue())   

    def test_sooner_date(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(sooner_date(1, 1, 1, 2))
            self.assertEqual('1 / 1\n', buf.getvalue()) 
        with io.StringIO() as buf, redirect_stdout(buf):
            sooner_date(2, 5, 1, 3)
            self.assertEqual('1 / 3\n', buf.getvalue()) 
        with io.StringIO() as buf, redirect_stdout(buf):
            sooner_date(8, 25, 7, 30)
            self.assertEqual('7 / 30\n', buf.getvalue())   
        with io.StringIO() as buf, redirect_stdout(buf):
            sooner_date(9, 1, 9, 1)
            self.assertEqual('9 / 1\n', buf.getvalue()) 
        with io.StringIO() as buf, redirect_stdout(buf):
            sooner_date(12, 2, 12, 1)
            self.assertEqual('12 / 1\n', buf.getvalue())     
            
test = unittest.defaultTestLoader.loadTestsFromTestCase(TestConditions)
results = unittest.TextTestRunner().run(test)
sys.stdout = sys.__stdout__
sys.stdin = sys.__stdin__
print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 100) + '%')
