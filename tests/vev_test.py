from vev import Vev
import unittest

class TestVev(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def teardownClass(cls):
        pass

    def test_route(self):
        self.assertNotIn("/foobar", Vev.routes)

        @Vev.route("/foobar")
        def myroute(foo):
            return 123

        self.assertIn("/foobar", Vev.routes)

if __name__ == "__main__":
    unittest.main()
