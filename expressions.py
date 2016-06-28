class Expression(object):

	def evaluate(self, indexLevel, line):
		# Aca se implementa cada tipo de expresion.
		raise NotImplementedError


class Number(Expression):

	def __init__(self, value, nType, line):
		self.value = value
		self.type = nType
		self.line = line
		self.operation = "Number"

	def evaluate(self, indexLevel, line):
                for x in range(0, indexLevel):
                        print ("\t")
                print (self.value)


class UnaryOperation(Expression):

        def __init__(self, right, operator, nType, line):
                self.right = right
                self.operator = operator
                self.type = nType
                self.line = line
                self.operation = "UnaryOperation"

        def evaluate(self, indexLevel, line):
                for x in range(0, indexLevel):
                        print ("\t")
                print (self.operator)
                self.right.evaluate(0, self.line)


class BinaryOperation(Expression):

	def __init__(self, left, right, operator, nType, line):
		self.left = left
		self.right = right
		self.operator = operator
		self.type = nType
		self.line = line
		self.operation = "BinaryOperation"

	def evaluate(self, indexLevel, line):
                for x in range(0, indexLevel):
                        print ("\t")
                self.left.evaluate(0, self.line)
                print (operator)
                self.right.evaluate(0, self.line)

class ParenOperation(Expression):

	def __init__(self, value, nType, line):
		self.value = value		
		self.type = nType
		self.line = line
		self.operation = "ParenOperation"

	def evaluate(self, indexLevel, line):
                for x in range(0, indexLevel):
                        print ("\t")
                print ("(")
                self.value.evaluate(0, self.line)
                print (")")

class CommentaryOperation(Expression):
        def __init__(self, value, nType, line):
                self.value = value		
                self.type = nType
                self.line = line
                self.operation = "CommentaryOperation"

        def evaluate(self, indexLevel, line):
                for x in range(0, indexLevel):
                        print ("\t")
                print(self.value)
                print ("\n")

class BlockOperation(Expression):

	def __init__(self, value, nType, line):
		self.value = value		
		self.type = nType
		self.line = line
		self.operation = "BlockOperation"

	def evaluate(self, indexLevel, line):
                for x in range(0, indexLevel):
                        print ("\t")
                print ("{")
                print ("\n")
                self.value.evaluate(indexLevel+1,self.line)
                for y in range(0, indexLevel):
                        print ("\t")
                print ("}")

def StatementOperation(Expression):
        def __init__(self, expression, nType, line):
                self.value = expression
                self.type = nType
                self.line = line
                self.operation = "StatementOperation"

        def evaluate(self, indexLevel, line):
                if not (self.statement is None):
                        for x in range(0, indexLevel):
                                print ("\t")
                        self.value.evaluate(indexLevel,self.line)
                        print(";")


def StatementsOperation(Expression):
        def __init__(self, statement, statements, nType, line):
                self.statement = statement
                self.statements = statements		
                self.type = nType
                self.line = line
                self.operation = "StatementsOperation"

        def evaluate(self, indexLevel, line):
                if not (self.statement is None):
                        for x in range(0, indexLevel):
                                print ("\t")
                        self.statement.evaluate(indexLevel,self.line)
                        if self.statements.operation == "CommentOperation" and line != self.statements.line or self.statements.operation != "CommentOperation":
                                print("\n")


                        self.statements.evaluate(indexLevel,self.line)
