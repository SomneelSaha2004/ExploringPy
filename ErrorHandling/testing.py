import unittest
import fullOferrors
class PrimeTester(unittest.TestCase):
    def testPrime(self):
        nums=[1,2,3,4,5,6]
        result=[0, 1, 3, 5, 8, 13]
        for i in range(0,len(nums)):
            out=fullOferrors.fibonacci(nums[i])
            self.assertEqual(out,result[i])
if __name__=="__main__":
    unittest.main()