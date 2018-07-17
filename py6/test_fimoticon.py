import unittest, sys, json, os, io
from unittest.mock import patch
import fishcatch, emoticons
from contextlib import redirect_stdout
from compare_files import compare_files

'''
Files needed:
'fish_dict.json', 'fishcatch_main_out_correct.txt'
'eti.json', 'ite.json', 'emoticons_main_out_correct.txt'
'compare_files.py'

Files needed for the programs to run (and hence for the test):
'fishcatch.dat', 'twitter_emoticons.dat'

Files needed for background:
'fishcatch.txt'
'''

class TestFimoticon(unittest.TestCase):

    def test_fish_dict_from_file(self):
        fd = fishcatch.fish_dict_from_file('fishcatch.dat')
        with open('fish_dict.json') as fp:
            fd_correct = json.load(fp)
        self.assertEqual(fd_correct, fd)
            
    def test_fishcatch_main(self):
        files = os.listdir()
        if 'fishcatch_main_out.txt' in files:
            os.remove('fishcatch_main_out.txt')
        with open('fishcatch_main_out.txt', 'w') as fp:
            sys.stdout = fp
            fishcatch.main()
        sys.stdout = sys.__stdout__
        self.assertTrue(compare_files('fishcatch_main_out_correct.txt', 'fishcatch_main_out.txt'))
        
    def test_find_most_common(self):
        dct = {'a': [1, 2, 3], 'b': [1, 2, 3, 4], 'c': [1, 2, 3, 4, 5]}
        with io.StringIO() as buf, redirect_stdout(buf):
            key = emoticons.find_most_common(dct)
            self.assertEqual('c' + ' ' * 20 + 'occurs        5 times\n', buf.getvalue())
            self.assertEqual('c', key)
            
    def test_load_twitter_dicts_from_file(self):
        eti = {}
        ite = {}
        emoticons.load_twitter_dicts_from_file('twitter_emoticons.dat', eti, ite)
        with open('eti.json') as fp:
            emoticons_to_ids = json.load(fp)
            self.assertEqual(emoticons_to_ids, eti)
        with open('ite.json') as fp:
            ids_to_emoticons = json.load(fp)
            self.assertEqual(ids_to_emoticons, ite)
            
    def test_emoticons_main(self):
        files = os.listdir()
        if 'emoticons_main_out.txt' in files:
            os.remove('emoticons_main_out.txt')
        with open('emoticons_main_out.txt', 'w') as fp:
            sys.stdout = fp
            emoticons.main()
        sys.stdout = sys.__stdout__
        self.assertTrue(compare_files('emoticons_main_out_correct.txt', 'emoticons_main_out.txt'))

test = unittest.defaultTestLoader.loadTestsFromTestCase(TestFimoticon)
results = unittest.TextTestRunner().run(test)
sys.stdout = sys.__stdout__
sys.stdin = sys.__stdin__
print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 100) + '%')
