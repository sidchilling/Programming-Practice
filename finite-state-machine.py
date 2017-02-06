import test

class Automaton(object):

    def __init__(self):
	self.states = ['q1']

    def read_commands(self, commands):
	for command in commands:
	    if self.states[len(self.states) - 1] == 'q1' and command == '1':
		self.states.append('q2')
	    elif self.states[len(self.states) - 1] == 'q2' and command == '0':
		self.states.append('q3')
	    elif self.states[len(self.states) - 1] == 'q3':
		self.states.append('q2')
	if self.states[len(self.states) - 1] == 'q2':
	    return True
	return False

my_automaton = Automaton()
test.assert_equals(my_automaton.read_commands(['1']), True)

my_automaton = Automaton()
test.assert_equals(my_automaton.read_commands(['1', '0', '0', '1']), True)