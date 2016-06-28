import lexer_rules


from ply.lex import lex

if __name__ == "__main__":

	text = "1+2"
	lexer = lex(module=lexer_rules)
	lexer.input(text)
	token = lexer.token()
	while token is not None:
		print (token.value)
		token = lexer.token()
