# Parser class which returns one expression

from expression import *
from operators import *
from operand import *

import json

class Parser(object):

    def __init__(self, expression_string, input_string):
	self.input_json = json.loads(input_string)
	self.expression_json = json.loads(expression_string)

    def get_expression(self):
	# Generate the Expression from the input string
	return self._generate_expression_or_operand(self.expression_json)

    def _generate_expression_or_operand(self, expression_json):
	if type(expression_json) == type([]):
	    # this looks like either an Expression or a ListOperand
	    if expression_json[0] in ['AND', 'OR', 'NOT', 'EQ', 'GT', 'LT', 'IN']:
		operator = self._generate_operator(expression_json[0])
		first_operand = self._generate_expression_or_operand(expression_json[1])
		# there might not be a second operator (in case of NOT)
		second_operand = None
		if len(expression_json) == 3:
		    second_operand = self._generate_expression_or_operand(expression_json[2])
		return Expression(operator = operator, first_operand = first_operand,
			second_operand = second_operand)
	    else:
		# this is a ListOperand
		return ListValueOperand(expression_json, self.input_json)
	else:
	    # this looks like an operand
	    return self._generate_operand(expression_json)

    def _generate_operator(self, operator_str):
	if operator_str == 'AND':
	    return AndOperator()
	elif operator_str == 'OR':
	    return OrOperator()
	elif operator_str == 'NOT':
	    return NotOperator()
	elif operator_str == 'EQ':
	    return EqualsOperator()
	elif operator_str == 'GT':
	    return GreaterThanOperator()
	elif operator_str == 'LT':
	    return LessThanOperator()
	elif operator_str == 'IN':
	    return InOperator()

    def _generate_operand(self, operand):
	if type(operand) in [type(''), type(u'')] and '.' in operand:
	    return InputValueOperand(operand, self.input_json)
	else:
	    return AbsoluteValueOperand(operand, self.input_json)
