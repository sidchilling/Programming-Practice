# Classes to represent different types of operands

class Operand(object):

    def __init__(self, value, input_json):
	self.value = value
	self.input_json = input_json

    def val(self):
	pass

    def __str__(self):
	pass

class AbsoluteValueOperand(Operand):

    def val(self):
	return self.value

    def __str__(self):
	return 'AbsoluteValueOperand({})'.format(self.value)

class InputValueOperand(Operand):

    def val(self):
	parts = self.value.split('.')
	res = self.input_json
	for part in parts:
	    res = res.get(part, {})
	return res

    def __str__(self):
	return 'InputValueOperand({})'.format(self.value)

class ListValueOperand(Operand):

    def __init__(self, value, input_json):
	self.input_json = input_json
	self.value = []
	for v in value:
	    if type(v) in [type(''), type(u'')] and '.' in v:
		self.value.append(InputValueOperand(v, self.input_json))
	    else:
		self.value.append(AbsoluteValueOperand(v, self.input_json))
    
    def val(self):
	res = []
	for v in self.value:
	    res.append(v.val())
	return res

    def __str__(self):
	list_els = []
	for v in self.value:
	    list_els.append('{}'.format(v))
	return 'ListValueOperand({})'.format(list_els)
