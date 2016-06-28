class Node(object):

	def evaluate(self, indexLevel, line):
		# Aca se implementa cada tipo de expresion.
		raise NotImplementedError


class NumberNode(Node):

	def __init__(self, value, nType, line):
		self.value = value
		self.type = nType
		self.line = line

	def evaluate(self, indexLevel, line):
                ret = ""
                for x in range(0, indexLevel):
                        res += "\t"
                ret += str(self.value)

                return ret


class UnaryOperationNode(Node):

        def __init__(self, right, operator, nType, line, leftOp):
                self.right = right
                self.operator = operator
                self.type = nType
                self.line = line
                self.leftOp = leftOp

        def evaluate(self, indexLevel, line):
                ret = ""
                for x in range(0, indexLevel):
                        ret += "\t"
                if self.leftOp:
                        ret += self.operator
                        ret += self.right.evaluate(0, self.line)
                else:
                        ret += self.right.evaluate(0, self.line)
                        ret += self.operator
                        
                return ret


class BinaryOperationNode(Node):

	def __init__(self, left, right, operator, nType, line):
		self.left = left
		self.right = right
		self.operator = operator
		self.type = nType
		self.line = line

	def evaluate(self, indexLevel, line):
                ret = ""
                for x in range(0, indexLevel):
                        ret += "\t"
                ret += self.left.evaluate(0, self.line)
                ret += self.operator
                ret += self.right.evaluate(0, self.line)

                return ret

class ParenOperationNode(Node):

	def __init__(self, value, nType, line):
		self.value = value		
		self.type = nType
		self.line = line

	def evaluate(self, indexLevel, line):
                ret = ""
                for x in range(0, indexLevel):
                        ret += "\t"
                ret += "("
                ret += self.value.evaluate(0, self.line)
                ret += ")"

                return ret
