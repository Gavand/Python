import unittest, sys, io, inspect
from unittest.mock import patch
from contextlib import redirect_stdout
from compare_files import compare_files
from madlib import *

"""
Files needed:
antsAndGrasshopper.txt
compare_files.py
intest_madlib.txt
intest_cm.txt
main_out_correct_madlib.txt
outtest.txt
report_correct.txt
test.txt
test_madlib.py
test1.txt
tortoise.txt
wolfAndLamb.txt
"""

class TestMadlib(unittest.TestCase):

    def test_replace_parts_of_speech(self):
        line = 'The NOUN VERB past the ADJECTIVE NOUN.'
        with patch('builtins.input', 
              side_effect=['roadrunner', 'coyote', 'ran', 'wiley']):
            line = replace_parts_of_speech(line, 'NOUN')
            line = replace_parts_of_speech(line, 'VERB')
            line = replace_parts_of_speech(line, 'ADJECTIVE')
        self.assertEqual('The roadrunner ran past the wiley coyote.', line)
        # test the prompt
        line = 'The NOUN.'
        sys.stdin = io.StringIO('dog')
        with io.StringIO() as buf, redirect_stdout(buf):
            line = replace_parts_of_speech(line, 'NOUN')
            self.assertEqual("The dog.", line)
            self.assertEqual("Enter noun: ", buf.getvalue())
        sys.stdin = sys.__stdin__

    def test_complete_mad_lib(self):
        save_in = sys.stdin
        infile = open('intest_cm.txt', 'r')
        sys.stdin = infile
        complete_mad_lib('tortoise.txt')
        sys.stdin = save_in
        infile.close()
        self.assertTrue(compare_files('outtest.txt', 'MAD_tortoise.txt'))
        #self.assertTrue(filecmp.cmp('outtest.txt', 'MAD_tortoise.txt'))
        
    def test_print_report(self):
        save_in = sys.stdin
        save_out = sys.stdout
        infile = open('intest_cm.txt', 'r')
        outfile = open('report.txt', 'w')
        sys.stdin = infile
        sys.stdout = outfile
        print_report('tortoise.txt')
        sys.stdin = save_in
        sys.stdout = save_out
        infile.close()
        outfile.close()
        self.assertTrue(compare_files('report_correct.txt', 'report.txt'))
        line = open('report.txt').readline()
        self.assertEquals('\n', line[0])
        self.assertTrue('tortoise' not in inspect.getsource(print_report))
        
    def test_main(self):
        # test the prompt
        sys.stdin = io.StringIO('dog')
        with io.StringIO() as buf, redirect_stdout(buf):
            try:
                main()
            except:
                pass
            self.assertEqual("Enter file name: ", buf.getvalue())
        sys.stdin = sys.__stdin__
        
        # test main
        save_in = sys.stdin
        save_out = sys.stdout
        infile = open('intest_madlib.txt', 'r')
        outfile = open('main_out.txt', 'w')
        sys.stdin = infile
        sys.stdout = outfile
        main()
        sys.stdin = save_in
        sys.stdout = save_out
        infile.close()
        outfile.close()
        self.assertTrue(compare_files('main_out_correct_madlib.txt', 'main_out.txt'))
        self.assertTrue(compare_files('outtest.txt', 'MAD_tortoise.txt'))

test = unittest.defaultTestLoader.loadTestsFromTestCase(TestMadlib)
results = unittest.TextTestRunner().run(test)
sys.stdout = sys.__stdout__
sys.stdin = sys.__stdin__
print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 100) + '%')
