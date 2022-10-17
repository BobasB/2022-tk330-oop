import unittest
from lab import Rocket

class TestMyLab(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_my_obj_attributes(self):
        name = "Falcon 9"
        mass = 549054
        size = 70
        obj = Rocket(name, mass, size)
        self.assertEqual(obj.name, name)
        self.assertEqual(obj.mass, mass)
        self.assertEqual(obj.size, size)
        self.assertIsInstance(obj, Rocket)
        self.assertNotIsInstance(obj, str)
    
    def testConvertPounds(self):
        r2 = Rocket("Atlas V", 546700, 58.3)
        result = r2.convert_to_pounds()
        self.assertAlmostEqual(result, 546700 * 2.20462262)
        self.assertIsInstance(result, float)
    
    def test_mass_less_zero(self):
        with self.assertRaises(AssertionError):
            Rocket("Atlas V", -1, 58.3)

    def test_object_created(self):
        for name, mass, size in [("a", 1, 1), ("b", 2, 2)]:
            self.assertIsInstance(Rocket(name, mass, size), Rocket)


if __name__ == '__main__':
    unittest.main(verbosity=2)
