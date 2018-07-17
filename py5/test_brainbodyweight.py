
import unittest, sys, json, os
from unittest.mock import patch
from brainbodyweight import *
from compare_files import compare_files

'''
Files needed for the test:
'csv_out_correct.csv', 'compare_files.py'
'names_correct.json', 'body_weights_correct.json', 'brain_weights_correct.json',
'intest_bbw.txt', 'BrainBodyWeightPounds_correct.csv', 'main_out_correct_bbw.txt'

This one is needed by the hw (and therefore the test):
'BrainBodyWeightKilos.csv'
'''

class TestMadlib(unittest.TestCase):

    def test_find_insert_position(self):
        # test their prompt next semester
        names = []
        self.assertEqual(0, find_insert_position('Rocket', names))
        self.assertEqual([], names)
        names = ['Rocket']
        self.assertEqual(0, find_insert_position('Rocket', names))
        self.assertEqual(['Rocket'], names)
        names = ['Lilly', 'Rocket']
        self.assertEqual(1, find_insert_position('Rocket', names))
        self.assertEqual(['Lilly', 'Rocket'], names)
        names = ['Lilly', 'Rocket']
        self.assertEqual(2, find_insert_position('Rocketman', names))
        self.assertEqual(['Lilly', 'Rocket'], names)
        names = ['Lilly', 'Rocketman']
        self.assertEqual(1, find_insert_position('Rocket', names))
        self.assertEqual(['Lilly', 'Rocketman'], names)

    def test_write_converted_csv(self):
        files = os.listdir()
        if 'csv_out.csv' in files:
            os.remove('csv_out.csv')
        names = ['Arctic Fox', 'Bat', 'Cougar']
        body_weights = [28, 5.34, 94.3]
        brain_weights = [2.8, .78, 9.43]
        write_converted_csv('csv_out.csv', names, body_weights, brain_weights)
        self.assertTrue(compare_files('csv_out_correct.csv', 'csv_out.csv'))
        
    def test_populate_lists(self):
        names = []
        body_weights = []
        brain_weights = []
        populate_lists(names, body_weights, brain_weights)
        with open('names_correct.json') as fp:
            names_correct = json.load(fp)
        with open('body_weights_correct.json') as fp:
            body_weights_correct = json.load(fp)
        with open('brain_weights_correct.json') as fp:
            brain_weights_correct = json.load(fp)
        self.assertEqual(names_correct, names)
        self.assertEqual(body_weights_correct, body_weights)
        self.assertEqual(brain_weights_correct, brain_weights)
        
    def test_main(self):
        files = os.listdir()
        if 'main_out.txt' in files:
            os.remove('main_out.txt')
        if 'BrainBodyWeightPounds.csv' in files:
            os.remove('BrainBodyWeightPounds.csv')
        save_in = sys.stdin
        save_out = sys.stdout
        infile = open('intest_bbw.txt', 'r')
        outfile = open('main_out.txt', 'w')
        sys.stdin = infile
        sys.stdout = outfile
        main()
        sys.stdin = save_in
        sys.stdout = save_out
        infile.close()
        outfile.close()
        self.assertTrue(compare_files('main_out_correct_bbw.txt', 'main_out.txt'))
        self.assertTrue(compare_files('BrainBodyWeightPounds_correct.csv', 'BrainBodyWeightPounds.csv'))

test = unittest.defaultTestLoader.loadTestsFromTestCase(TestMadlib)
results = unittest.TextTestRunner().run(test)
sys.stdout = sys.__stdout__
sys.stdin = sys.__stdin__
print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 100) + '%')
