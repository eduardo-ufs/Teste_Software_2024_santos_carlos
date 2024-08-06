import mymod
import unittest


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertRaises(Exception, mymod.myfunc)


if __name__ == '__main__':
    unittest.main()
