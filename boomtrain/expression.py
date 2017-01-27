# Class to denote an expression 
# An expression has a operator and two operands 

class Expression(object):
    
    def __init__(self, operator, first_operand, second_operand):
	self.operator = operator
	self.first_operand = first_operand
	self.second_operand = second_operand


    def val(self):
	# Returns the value of the Expression
	res = self.operator.val(first_operand = self.first_operand,
		  second_operand = self.second_operand)
	#print '{} : {}'.format(self, res)
	return res

    def __str__(self):
	if self.second_operand:
	    return '[{}, {}, {}]'.format(self.operator, self.first_operand,
				  self.second_operand)
	else:
	    return '[{}, {}]'.format(self.operator, self.first_operand)
