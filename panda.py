import unittest 
import time
  
class FirstTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self): 
        print("First test case")
        time.sleep(10)
        self.assertTrue(True) 
        
class SecondTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):
        print("second test")
        time.sleep(10)
        self.assertTrue(True) 
class ThirdTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):
        print("Third test")
        time.sleep(10)
        self.assertTrue(True) 
class FourthTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):
        print("fourth test")
        time.sleep(10)
        self.assertTrue(True) 
class FifthTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):
        print("fifth test")
        time.sleep(10)
        self.assertTrue(True) 
class SixthTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):
        print("sixth test")
        time.sleep(10)
        self.assertTrue(True) 
class SeventhTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):
        print("seventh test")
        time.sleep(10)
        self.assertTrue(True) 
  
if __name__ == '__main__': 
    unittest.main() 