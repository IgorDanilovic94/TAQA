import unittest

def division (a,b):
    return a/b

class test_Volume(unittest.TestCase):
    
    def test_nula(self):
        result = division(-1,5)
        
        #result = division(7,0)
        #nastala bi greska
        
        self.assertNotEqual(result,0)
    
    def test_is_string(self):
        result = int(division(1,5)) 
        
        #result =int(division('Banjaluka','Novi Sad'))
        #nastala bi greska
        
        
        self.assertRaises(TypeError,result,True)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_Volume))
    return test_suite
 
 
mySuite=suite()

runner=unittest.TextTestRunner()
runner.run(mySuite)


