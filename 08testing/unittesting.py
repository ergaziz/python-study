import unittest
import os

def analyze_text(filename):
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)


class TextAnalysisTests(unittest.TestCase):  # this is how we define a test case
    """Tests for the ``analyze_text()`` function"""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')
    
    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the func run."""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 131)

    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))
        
if __name__ == '__main__':
    unittest.main()  # this is needed for unit tests

# if we didnt have func defined:
# D:\Ergazi\Workspace\python-study\08testing>python unittesting.py
# E
# ======================================================================
# ERROR: test_function_runs (__main__.TextAnalysisTests)
# Basic smoke test: does the func run.
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "unittesting.py", line 8, in test_function_runs
#     analyze_text()
# NameError: name 'analyze_text' is not defined
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
# FAILED (errors=1)

# If we have it defined:
# D:\Ergazi\Workspace\python-study\08testing>python unittesting.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# OK

