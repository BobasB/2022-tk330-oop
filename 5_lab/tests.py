from cgitb import reset
import unittest
from lab import Rocket

class TestMyLab(unittest.TestCase):
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


#if __name__ == '__main__':
#    unittest.main(verbosity=2)
