import pdb

class Node(object):

	def evaluate(self, indexLevel, line):
		# Aca se implementa cada tipo de expresion.
		raise NotImplementedError

class EmptyNode(Node):
        def __init__(self):
                return
        def evaluate(self, indexLevel, line):
                return ""

class NumberNode(Node):

	def __init__(self, value, nType, line):
		self.value = value
		self.type = nType
		self.line = line

	def evaluate(self, indexLevel, line):
                ret = ""
                # for x in range(0, indexLevel):
                #         res += "\t"
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
                # ret = "\t" * indexLevel
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
                # for x in range(0, indexLevel):
                #         ret += "\t"
                ret += self.left.evaluate(0, self.line)
                ret += " " + self.operator + " "
                ret += self.right.evaluate(0, self.line)

                return ret

class ParenOperationNode(Node):

	def __init__(self, value, nType, line):
		self.value = value
		self.type = nType
		self.line = line

	def evaluate(self, indexLevel, line):
                # ret = "\t" * indexLevel
                ret += "("
                ret += self.value.evaluate(0, self.line)
                ret += ")"

                return ret

class BooleanNode(Node):
        def __init__(self, value, line):
                self.value = value
                self.line = line
        def evaluate(self, indexLevel, line):
                return self.value

class BooleanOperationNode(Node):
        def __init__(self, bool1, bool2, op, line):
                self.bool1 = bool1
                self.bool2 = bool2
                self.op = op
                self.line = line

        def evaluate(self, indexLevel, line):
                pdb.set_trace()

                return (self.bool1.evaluate(indexLevel, line) +
                       " " + self.op + " " +
                       self.bool2.evaluate(indexLevel, line))




class CommentNode(Node):

	def __init__(self, comment, code, line):
		self.comment = comment
                self.code = code
		self.line = line

	def evaluate(self, indexLevel, line):
                ret = "\t" * indexLevel + self.comment + "\n"
                ret += self.code.evaluate(indexLevel, line)

                # pdb.set_trace()
                return ret

# class InitialCodeNode(Node):
# 	def __init__(self, comment, code, line):
# 		self.comment = comment
# 		self.code = code
# 		self.line = line

# 	def evaluate(self, indexLevel, line):
#                 ret = ""
#                 for x in range(0, indexLevel):
#                         ret += "\t"
#                 ret += self.comments.evaluate(indexLevel, self.line)
#                 if ret != "":
#                         ret+="\n"
#                 ret += self.code.evaluate(indexLevel, self.line)

#                 return ret

class CodeNode(Node):
	def __init__(self, statement, code, line):
		self.statement = statement
		self.code = code
		self.line = line

	def evaluate(self, indexLevel, line):
                ret = ""
                # for x in range(0, indexLevel):
                #         ret += "a"
                ret += self.statement.evaluate(indexLevel, self.line)
                ret += self.code.evaluate(indexLevel, self.line)

                return ret

class ExpressionStatementNode(Node):
	def __init__(self, expression, comments, line):
		self.expression = expression
		self.comments = comments
		self.line = line

	def evaluate(self, indexLevel, line):
                ret = ""
                for x in range(0, indexLevel):
                        ret += "\t"
                ret += self.expression.evaluate(indexLevel, self.line)
                ret+=";"
                # ret += self.comments.evaluate(indexLevel, self.line)
                ret+="\n"

                return ret

class BlockNode(Node):
        def __init__(self, code, line):
                self.code = code
                self.line = line

        def evaluate(self, indexLevel, line):
                ret = "{\n"
                ret += self.code.evaluate(indexLevel + 1, self.line)
                ret += "\t" * indexLevel + "}"

                return ret

class IfNode(Node):
        def __init__(self, cond, caseTrue, caseFalse, line):
                self.cond = cond
                self.caseTrue = caseTrue
                self.caseFalse = caseFalse
                self.line = line

        def evaluate(self, indexLevel, line):
                ret = "if (" + self.cond.evaluate(indexLevel, line) + ")"
                ret += self.caseTrue.evaluate(indexLevel, line)
                ret += self.caseFalse.evaluate(indexLevel, line)
                return ret

class ElseNode(Node):
        def __init__(self, content, line):
                self.content = content
                self.line = line

        def evaluate(self, indexLevel, line):
                return " else " + self.content.evaluate(indexLevel, line)
                return ret

