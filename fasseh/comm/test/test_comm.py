import unittest
from fasseh.comm import comm


class TestComm(unittest.TestCase):
        def test_comm(self):
                self.assertEqual('comm'.upper(), 'COMM')

if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestComm)
        unittest.TextTestRunner(verbosity=2).run(suite)
