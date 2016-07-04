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
                return "(%s)" % self.value.evaluate(0, self.line)
                # ret = "\t" * indexLevel
                # ret += "("
                # ret += self.value.evaluate(0, self.line)
                # ret += ")"

                # return ret

class BooleanNode(Node):
        def __init__(self, value, line):
                self.value = value
                self.line = line
                self.type = 'bool'

        def evaluate(self, indexLevel, line):
                return self.value

class BooleanOperationNode(Node):
        def __init__(self, bool1, bool2, op, line):
                self.bool1 = bool1
                self.bool2 = bool2
                self.op = op
                self.line = line
                self.type = 'bool'

        def evaluate(self, indexLevel, line):
                return (self.bool1.evaluate(indexLevel, line) +
                       " " + self.op + " " +
                       self.bool2.evaluate(indexLevel, line))

class BooleanNegationNode(Node):
        def __init__(self, bool1, line):
                self.bool1 = bool1
                self.line = line
                self.type = 'bool'

        def evaluate(self, indexLevel, line):
                return ("NOT " + self.bool1.evaluate(indexLevel, line))

class BooleanParenExpression(Node):
        def __init__(self, expr, line):
                self.expr = expr
                self.line = line
                self.type = 'bool'

        def evaluate(self, indexLevel, line):
                return "(%s)" % self.expr.evaluate(indexLevel, line)

class BooleanCompNode(Node):
        def __init__(self, exp1, op, exp2, line):
                self.exp1 = exp1
                self.op = op
                self.exp2 = exp2
                self.line = line
                self.type = 'bool'

        def evaluate(self, indexLevel, line):
                # pdb.set_trace()
                return (self.exp1.evaluate(indexLevel, line) +
                       " " + self.op + " " +
                       self.exp2.evaluate(indexLevel, line))

class StrNode(Node):
        def __init__(self, string, line):
                self.string = string
                self.line = line
                self.type = 'str'

        def evaluate(self, indexLevel, line):
                return "\"%s\"" % self.string

class StrConcatNode(Node):
        def __init__(self, str1, str2, line):
                self.str1 = str1
                self.str2 = str2
                self.line = line
                self.type = 'str'

        def evaluate(self, indexLevel, line):
                return "%s + %s" % (
                        self.str1.evaluate(indexLevel, line),
                        self.str2.evaluate(indexLevel, line)
                        )

class VectorNode(Node):
        def __init__(self, items, line, type):
                self.items = items
                self.line = line
                self.type = 'vector'
                self.item_type = type

        def evaluate(self, indexLevel, line):
                return "[%s]" % self.items.evaluate(indexLevel, line)

class VectorItemsNode(Node):
        def __init__(self, head, tail, line, type):
                self.head = head
                self.tail = tail
                self.line = line
                self.type = type

        def evaluate(self, indexLevel, line):
                return "%s, %s" % (
                        self.head.evaluate(indexLevel, line),
                        self.tail.evaluate(indexLevel, line))

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
                ret += "\t" * indexLevel + "} \n"

                return ret

class IfNode(Node):
        def __init__(self, cond, caseTrue, caseFalse, line):
                self.cond = cond
                self.caseTrue = caseTrue
                self.caseFalse = caseFalse
                self.line = line

        def evaluate(self, indexLevel, line):
                return "%sif (%s)%s%s" % (
                        "\t" * indexLevel,
                        self.cond.evaluate(indexLevel, line),
                        self.caseTrue.evaluate(indexLevel, line),
                        self.caseFalse.evaluate(indexLevel, line)
                        )

class ElseNode(Node):
        def __init__(self, content, line):
                self.content = content
                self.line = line

        def evaluate(self, indexLevel, line):
                return " else " + self.content.evaluate(indexLevel, line)

class WhileNode(Node):
        def __init__(self, cond, content, line):
                self.cond = cond
                self.content = content
                self.line = line

        def evaluate(self, indexLevel, line):
                return "%swhile (%s) %s" % (
                        "\t" * indexLevel,
                        self.cond.evaluate(indexLevel, line),
                        self.content.evaluate(indexLevel, line)
                        )

class ForNode(Node):
        def __init__(self, init, cond, post, content):
                self.init = init
                self.cond = cond
                self.post = post
                self.content = content
                self.line = cond.line

        def evaluate(self, indexLevel, line):
                return "%sfor (%s; %s; %s) %s" % (
                        "\t" * indexLevel,
                        self.init.evaluate(indexLevel, line),
                        self.cond.evaluate(indexLevel, line),
                        self.post.evaluate(indexLevel, line),
                        self.content.evaluate(indexLevel, line)
                        )

class DoWhileNode(Node):
        def __init__(self, content, cond, line):
                self.content = content
                self.cond = cond
                self.line = line

        def evaluate(self, indexLevel, line):
                return "%sdo %s while (%s);" % (
                        "\t" * indexLevel,
                        self.content.evaluate(indexLevel, line),
                        self.cond.evaluate(indexLevel, line)
                        )
