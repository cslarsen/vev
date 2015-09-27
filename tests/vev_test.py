from vev import Route
import unittest

class TestVev(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def teardownClass(cls):
        pass

    def test_route(self):
        self.assertNotIn("/foobar", Route.routes)

        @Route.bind("/foobar")
        def myroute(foo):
            return 123

        self.assertIn("/foobar", Route.routes)

if __name__ == "__main__":
    unittest.main()
