import pdb

class Node(object):

	def evaluate(self, indexLevel, line):
		# Aca se implementa cada tipo de expresion.
		raise NotImplementedError

class EmptyNode(Node):
        def __init__(self):
                self.type = 'empty'

        def evaluate(self, indexLevel, line):
                return ""

class VarNode(Node):

	def __init__(self, value,line):
		self.value = value
		self.type = 'VAR'
		self.line = line

	def evaluate(self, indexLevel, line):
                ret = ""
                # for x in range(0, indexLevel):
                #         res += "\t"
                ret += str(self.value)

                return ret

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
                ret = ""
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
                # el tipo de un vector se representa con una tupla (tipo basico, cantidad de vectores anidados)
                # por ejemplo, vector<vector<vector<int> > > seria (int, 3)
                if isVector(type):
                        self.type = (type[0], type[1] + 1)
                else:
                        self.type = (type, 1)

        def evaluate(self, indexLevel, line):
                return "[%s]" % self.items.evaluate(indexLevel, line)

def isVector(t):
        return t.__class__.__name__ == "tuple" and t[0] != "register"


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

class VectorAtNode(Node):
        def __init__(self, vect, index, line, type):
                self.vect = vect
                self.index = index
                self.line = line
                self.type = type
                if type != 'undef':
                        self.type = (type[0], type[1]-1)
                        if self.type[1] == 0:
                                self.type = self.type[0]

        def evaluate(self, indexLevel, line):
                return "%s[%s]" % (
                        self.vect.evaluate(indexLevel, line),
                        self.index.evaluate(indexLevel, line))

class AssignOperationNode(Node):

	def __init__(self, left, right, operator, type, line):
		self.left = left
		self.right = right
		self.operator = operator
		self.type = type
		self.line = line

	def evaluate(self, indexLevel, line):
                ret = ""
                # for x in range(0, indexLevel):
                #         ret += "\t"
                ret += self.left.evaluate(0, self.line)
                ret += " " + self.operator + " "
                ret += self.right.evaluate(0, self.line)

                return ret

# class AssignOperationNode2(Node):

#     def __init__(self, right, operator):
#         self.right = right
#         self.operator = operator
#         self.type = "assign2"
#         # self.type = type
#         # self.line = line

class CommentNode(Node):

	def __init__(self, comment, code, line):
		self.comment = comment
		self.code = code
		self.line = line
		self.type = 'comment'

	def evaluate(self, indexLevel, line, hasComment = False):
                return  "%s%s\n%s" % (
                        "" if hasComment else "\t" * indexLevel,
                        self.comment,
                        self.code.evaluate(indexLevel, line))

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
		self.type = 'code'

	def evaluate(self, indexLevel, line):
                hasComment = (self.code.type == 'comment' and self.code.line == self.statement.line)
                evalCode = ""
                if hasComment:
                        evalCode = self.code.evaluate(indexLevel, self.line, hasComment)
                else:
                        evalCode = self.code.evaluate(indexLevel, self.line)
                return  "%s%s%s" % (self.statement.evaluate(indexLevel, self.line),
                        " " if hasComment else "\n",
                        evalCode)


class StatementNode(Node):
	def __init__(self, expression, line):
		self.expression = expression
		# self.comments = comments
		self.line = line
		self.type = 'statement'

	def evaluate(self, indexLevel, line):
                return "%s%s;" % (
                        "\t" * indexLevel,
                        self.expression.evaluate(indexLevel, self.line)
                        )

class BlockNode(Node):
        def __init__(self, code, line):
                self.code = code
                self.line = line
                self.type = 'block'

        def evaluate(self, indexLevel, line):
                ret = "{\n%s%s}" % (
                        self.code.evaluate(indexLevel, self.line),
                        "\t" * (indexLevel - 1))

                return ret

class IfNode(Node):
        def __init__(self, cond, caseTrue, caseFalse, line):
                self.cond = cond
                self.caseTrue = caseTrue
                self.caseFalse = caseFalse
                self.line = line
                self.type = 'statement'

        def evaluate(self, indexLevel, line):
                return "%sif (%s) %s%s%s" % (
                        "\t" * indexLevel,
                        self.cond.evaluate(indexLevel, line),
                        "\n" if (self.caseTrue.type == 'statement' or self.caseTrue.type == 'comment') else "",
                        self.caseTrue.evaluate(indexLevel + 1, line),
                        self.caseFalse.evaluate(indexLevel, line)
                        )

class ElseNode(Node):
        def __init__(self, content, line):
                self.content = content
                self.line = line
                self.type = 'else'

        def evaluate(self, indexLevel, line):
                return "\n%selse %s%s" % ("\t"*indexLevel,
                        "\n" if (self.content.type == 'statement' or self.content.type == 'comment') else "",
                        self.content.evaluate(indexLevel + 1, line))

class TernaryConditionalNode:
        def __init__(self, cond, caseTrue, caseFalse, type, line):
                self.cond = cond
                self.caseTrue = caseTrue
                self.caseFalse = caseFalse
                self.line = line
                self.type = type

        def evaluate(self, indexLevel, line):
                return "%s%s ? %s : %s" % (
                        "\t" * indexLevel,
                        self.cond.evaluate(indexLevel, line),
                        self.caseTrue.evaluate(indexLevel, line),
                        self.caseFalse.evaluate(indexLevel, line)
                        )

class WhileNode(Node):
        def __init__(self, cond, content, line):
                self.cond = cond
                self.content = content
                self.line = line
                self.type = 'statement'

        def evaluate(self, indexLevel, line):
                return "%swhile (%s) %s%s" % (
                        "\t" * indexLevel,
                        self.cond.evaluate(indexLevel, line),
                        "\n" if (self.content.type == 'statement' or self.content.type == 'comment') else "",
                        self.content.evaluate(indexLevel + 1, line)
                        )

class ForNode(Node):
        def __init__(self, init, cond, post, content):
                self.init = init
                self.cond = cond
                self.post = post
                self.content = content
                self.line = cond.line
                self.type = 'statement'

        def evaluate(self, indexLevel, line):
                return "%sfor (%s; %s; %s) %s%s" % (
                        "\t" * indexLevel,
                        self.init.evaluate(indexLevel, line),
                        self.cond.evaluate(indexLevel, line),
                        self.post.evaluate(indexLevel, line),
                        "\n" if (self.content.type == 'statement' or self.content.type == 'comment') else "",
                        self.content.evaluate(indexLevel + 1, line)
                        )

class DoWhileNode(Node):
        def __init__(self, content, cond, line):
                self.content = content
                self.cond = cond
                self.line = line
                self.type = 'statement'

        def evaluate(self, indexLevel, line):
                return "%sdo %s%s%swhile (%s);" % (
                        "\t" * indexLevel,
                        "\n" if (self.content.type == 'statement' or self.content.type == 'comment') else "",
                        self.content.evaluate(indexLevel + 1, line),
                        ("\n" + "\t"*indexLevel) if (self.content.type == 'statement' or self.content.type == 'comment') else " ",
                        self.cond.evaluate(indexLevel, line)
                        )

class ScalarMultiplicationNode(Node):
        def __init__(self, arg1, arg2, arg3, type, line):
                self.arg1 = arg1
                self.arg2 = arg2
                self.arg3 = arg3
                if arg3 == "":
                        self.arg3 = None
                self.line = line
                self.type = type

        def evaluate(self, indexLevel, line):
                arg3 = ""
                if self.arg3 is not None:
                        arg3 = ", " + self.arg3.evaluate(indexLevel, line)
                return "multiplicacionEscalar(%s, %s%s)" % (    self.arg1.evaluate(indexLevel, line),
                                                                self.arg2.evaluate(indexLevel, line),
                                                                arg3)

class CapitalizeNode(Node):
        def __init__(self, arg1, line):
                self.arg1 = arg1
                self.line = line
                self.type = 'str'

        def evaluate(self, indexLevel, line):
                return "capitalizar(%s)" % (self.arg1.evaluate(indexLevel, line))

class CollinearNode(Node):
        def __init__(self, arg1, arg2, line):
                self.arg1 = arg1
                self.arg2 = arg2
                self.line = line
                self.type = 'bool'

        def evaluate(self, indexLevel, line):
                return "colineales(%s, %s)" % (self.arg1.evaluate(indexLevel, line),
                                               self.arg2.evaluate(indexLevel, line))

class PrintNode(Node):
        def __init__(self, arg1, line):
                self.arg1 = arg1
                self.line = line
                self.type = 'print'

        def evaluate(self, indexLevel, line):
                return "print(%s)" % (self.arg1.evaluate(indexLevel, line))

class LengthNode(Node):
        def __init__(self, arg1, line):
                self.arg1 = arg1
                self.line = line
                self.type = 'int'

        def evaluate(self, indexLevel, line):
                return "length(%s)" % (self.arg1.evaluate(indexLevel, line))

class RegisterNode(Node):
        currentReg = 0
        def __init__(self, arg1, line):
                self.arg1 = arg1
                self.line = line
                self.type = ('register', RegisterNode.currentReg)
                RegisterNode.currentReg += 1

        def evaluate(self, indexLevel, line):
                return "{%s}" % (self.arg1.evaluate(indexLevel, line))

class MemberAccessNode(Node):
        def __init__(self, reg, member, type, line):
                self.reg = reg
                self.member = member
                self.line = line
                self.type = type

        def evaluate(self, indexLevel, line):
                return "%s.%s" % (self.reg.evaluate(indexLevel, line),
                                  self.member.evaluate(indexLevel, line))

class RegisterItemsNode(Node):
        def __init__(self, field1, rest, line):
                self.field1 = field1
                self.rest = rest
                # self.line = line
                self.type = 'regitem'
                self.line = line

        def evaluate(self, indexLevel, line):
                return "%s, %s" % (
                        self.field1.evaluate(indexLevel, line),
                        self.rest.evaluate(indexLevel, line)
                        )
        def fields(self):
                return [self.field1] + self.rest.fields()

class RegFieldNode(Node):
        def __init__(self, key, exp, type, line):
                self.key = key
                self.value = exp
                self.type = type
                self.line = line

        def evaluate(self, indexLevel, line):
                return "%s:%s" % (
                        self.key.evaluate(indexLevel, line),
                        self.value.evaluate(indexLevel, line)
                        )
        def fields(self):
                return [self]
