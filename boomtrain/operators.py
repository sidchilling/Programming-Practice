# Classes to represent an operator (logical, arithematic)

class Operator(object):

    def val(self, first_operand, second_operand):
	pass

    def __str__(self):
	pass

class AndOperator(Operator):

    def val(self, first_operand, second_operand):
	return first_operand.val() and second_operand.val()

    def __str__(self):
	return 'AND'

class OrOperator(Operator):

    def val(self, first_operand, second_operand):
	return first_operand.val() or second_operand.val()

    def __str__(self):
	return 'OR'

class NotOperator(Operator):

    def val(self, first_operand, second_operand):
	return not first_operand.val()

    def __str__(self):
	return 'NOT'

class EqualsOperator(Operator):

    def val(self, first_operand, second_operand):
	return first_operand.val() == second_operand.val()

    def __str__(self):
	return 'EQ'

class GreaterThanOperator(Operator):

    def val(self, first_operand, second_operand):
	return first_operand.val() > second_operand.val()

    def __str__(self):
	return 'GT'

class LessThanOperator(Operator):

    def val(self, first_operand, second_operand):
	return first_operand.val() < second_operand.val()

    def __str__(self):
	return 'LT'

class InOperator(Operator):

    def val(self, first_operand, second_operand):
	return first_operand.val() in second_operand.val()

    def __str__(self):
	return 'IN'
