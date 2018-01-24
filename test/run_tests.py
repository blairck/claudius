"""This module uses unittest TestLoader to run tests"""

import sys
import unittest

if __name__ == '__main__':
    sys.dont_write_bytecode = True
    suite = unittest.TestLoader().discover(".", pattern="test*")
    unittest.TextTestRunner(verbosity=1, buffer=True).run(suite)
