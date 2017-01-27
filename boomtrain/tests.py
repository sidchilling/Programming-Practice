import unittest
import json

from parser import Parser

class TestExpressionEvaluator(unittest.TestCase):

    def setUp(self):
	self.input_json = {
	    'user' : {
		'address' : {
		    'address_line' : 'XYZ Street',
		    'city' : 'San Francisco',
		    'state' : 'CA',
		    'zipcode' : '94150'
		},
		'age' : 29
	    },
	    'event' : {
		'category' : 'teen'
	    }
	}

    def runTest(self, expression_json):
	expression_json = json.dumps(expression_json)
	parser = Parser(expression_json, json.dumps(self.input_json))
	expression = parser.get_expression()
	result = expression.val()
	print 'Input Expression: {}'.format(expression_json)
	print 'Parsed Expression: {}'.format(expression)
	print 'Result: {}'.format(result)
	print '\n'
	return result

    def testOne(self):
	expression_json = ["EQ", "user.address.city", "Los Angeles"]
	self.assertFalse(self.runTest(expression_json))

    def testTwo(self):
	expression_json = ["EQ", "user.address.city", "San Francisco"]
	self.assertTrue(self.runTest(expression_json))

    def testThree(self):
	expression_json = ["NOT", False]
	self.assertTrue(self.runTest(expression_json))

    def testFour(self):
	expression_json = ["NOT", True]
	self.assertFalse(self.runTest(expression_json))

    def testFive(self):
	expression_json = ["AND", ["EQ", "user.address.city", "San Francisco"], True]
	self.assertTrue(self.runTest(expression_json))

    def testSix(self):
	expression_json = ["AND", ["EQ", "user.address.city", "San Francisco"], False]
	self.assertFalse(self.runTest(expression_json))

    def testSeven(self):
	expression_json = ["AND", ["EQ", "user.address.city", "Los Angeles"], True]
	self.assertFalse(self.runTest(expression_json))

    def testEight(self):
	expression_json = ["AND", True, ["EQ", "user.address.city", "San Francisco"]]
	self.assertTrue(self.runTest(expression_json))

    def testNine(self):
	expression_json = ["AND", ["EQ", "user.address.city", "Los Angeles"], ["GT", "user.age", 35]]
	self.assertFalse(self.runTest(expression_json))

    def testTen(self):
	expression_json = ["AND", ["EQ", "user.address.city", "San Francisco"], ["GT", "user.age", 35]]
	self.assertFalse(self.runTest(expression_json))

    def testEleven(self):
	expression_json = ["AND", ["EQ", "user.address.city", "Los Angeles"], ["LT", "user.age", 35]]
	self.assertFalse(self.runTest(expression_json))

    def testTwelve(self):
	expression_json = ["AND", ["EQ", "user.address.city", "San Francisco"], ["LT", "user.age", 35]]
	self.assertTrue(self.runTest(expression_json))

    def testThirteen(self):
	expression_json = ["IN", "user.address.city", ["San Francisco", "Los Angeles"]]
	self.assertTrue(self.runTest(expression_json))

    def testFourteen(self):
	expression_json = ["IN", "user.address.city", ["Las Vegas", "Los Angeles"]]
	self.assertFalse(self.runTest(expression_json))

    def testFifteen(self):
	expression_json = ["NOT", ["IN", "user.address.city", ["San Francisco", "Los Angeles"]]]
	self.assertFalse(self.runTest(expression_json))

    def testSixteen(self):
	expression_json = ["IN", "event.category", ["infant", "child", "teen"]]
	self.assertTrue(self.runTest(expression_json))

    def testSeventeen(self):
	expression_json = ["OR", ["IN", "event.category", ["infant", "child", "teen"]], ["LT", "user.age", 18]]
	self.assertTrue(self.runTest(expression_json))

    def testEighteen(self):
	expression_json = ["AND", ["IN", "event.category", ["infant", "child", "teen"]], ["LT", "user.age", 18]]
	self.assertFalse(self.runTest(expression_json))


if __name__ == '__main__':
    unittest.main()
