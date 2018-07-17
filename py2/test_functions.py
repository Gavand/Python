import unittest, sys, io
from contextlib import redirect_stdout
from functions import *

class TestFunctions(unittest.TestCase):

    def test_print_word(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(print_word(3, 'banana'))
            self.assertEqual('1 --> banana\n2 --> banana\n3 --> banana\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            print_word(1, 'banana')
            self.assertEqual('1 --> banana\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            print_word(-1, 'banana')
            self.assertEqual('', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            print_word(5, '')
            self.assertEqual('1 --> \n2 --> \n3 --> \n4 --> \n5 --> \n', buf.getvalue())
            
    def test_bacteria(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(bacteria(3, 3))
            self.assertEqual('after 3 minutes:  2 bacteria\nafter 6 minutes:  4 bacteria\n' +
                'after 9 minutes:  8 bacteria\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            bacteria(10, 5)
            self.assertEqual('after 10 minutes:  2 bacteria\nafter 20 minutes:  4 bacteria\n' +
                'after 30 minutes:  8 bacteria\nafter 40 minutes:  16 bacteria\n' +
                'after 50 minutes:  32 bacteria\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            bacteria(0, 3)
            self.assertEqual('after 0 minutes:  2 bacteria\nafter 0 minutes:  4 bacteria\n' +
                'after 0 minutes:  8 bacteria\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            bacteria(-1, 3)
            self.assertEqual('after -1 minutes:  2 bacteria\nafter -2 minutes:  4 bacteria\n' +
                'after -3 minutes:  8 bacteria\n', buf.getvalue())
            
    def test_convert_to_copper(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(convert_to_copper(5, 10, 7))
            self.assertEqual('5 gp, 10 sp, 7 cp converted to copper is: 307 cp\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            convert_to_copper(15, 23, 12)
            self.assertEqual('15 gp, 23 sp, 12 cp converted to copper is: 877 cp\n', buf.getvalue())
            
    def test_convert_from_copper(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(convert_from_copper(200))
            self.assertEqual('200 copper pieces is: 4 gp, 0 sp, 0 cp\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(convert_from_copper(208))
            self.assertEqual('208 copper pieces is: 4 gp, 1 sp, 3 cp\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            convert_from_copper(1107)
            self.assertEqual('1107 copper pieces is: 22 gp, 1 sp, 2 cp\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            convert_from_copper(3242)
            self.assertEqual('3242 copper pieces is: 64 gp, 8 sp, 2 cp\n', buf.getvalue())
            
    def test_repeat_word(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(repeat_word('Goblin', 3, 5))
            self.assertEqual('GoblinGoblinGoblinGoblinGoblin\n' +
                             'GoblinGoblinGoblinGoblinGoblin\n' +
                             'GoblinGoblinGoblinGoblinGoblin\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            repeat_word('Kobold', 5, 3)
            self.assertEqual('KoboldKoboldKobold\n' +
                             'KoboldKoboldKobold\n' +
                             'KoboldKoboldKobold\n' +
                             'KoboldKoboldKobold\n' +
                             'KoboldKoboldKobold\n', buf.getvalue())
            
    def test_text_triangle(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(text_triangle(3))
            self.assertEqual('x\nxx\nxxx\n', buf.getvalue().lower())
        with io.StringIO() as buf, redirect_stdout(buf):
            text_triangle(5)
            self.assertEqual('x\nxx\nxxx\nxxxx\nxxxxx\n', buf.getvalue().lower())
        with io.StringIO() as buf, redirect_stdout(buf):
            text_triangle(-1)
            self.assertEqual('\n', buf.getvalue().lower())
            
    def test_surface_area_of_cylinder(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(surface_area_of_cylinder(10.0, 10.0))
            self.assertEqual('The surface area of a cylinder with radius 10.0' +
                             ' and height 10.0 is 1256.6370614359173\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            surface_area_of_cylinder(3.0, 1.0)
            self.assertEqual('The surface area of a cylinder with radius 3.0' +
                             ' and height 1.0 is 75.39822368615503\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            surface_area_of_cylinder(0.0, 10.0)
            self.assertEqual('The surface area of a cylinder with radius 0.0' +
                             ' and height 10.0 is 0.0\n', buf.getvalue())
            
    def test_tree_height(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(tree_height(300, 500))
            self.assertEqual('Kite string: 500\nDistance: 300\nHeight: 400.0\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(tree_height(100, 141.421356))
            self.assertEqual('Kite string: 141.421356\nDistance: 100\nHeight: 99.99999966439368\n', buf.getvalue())

test = unittest.defaultTestLoader.loadTestsFromTestCase(TestFunctions)
results = unittest.TextTestRunner().run(test)
sys.stdout = sys.__stdout__
sys.stdin = sys.__stdin__
print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 100) + ' / 100')
