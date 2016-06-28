import lexer_rules_v2


from ply.lex import lex

if __name__ == "__main__":

	text = "++1+2"
	lexer = lex(module=lexer_rules_v2)
	lexer.input(text)
	token = lexer.token()
	while token is not None:
		print (token.value)
		token = lexer.token()
