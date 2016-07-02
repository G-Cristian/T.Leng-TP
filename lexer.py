import lexer_rules_v2


from ply.lex import lex

if __name__ == "__main__":

	text = """1++;
#Nueva lines #mas comentario en misma linea
2+3;     #comentario misma linea
3+4; #comentario mimsa linea


#comentario otra linea

4+2;
#comentario otra linea

"""
	lexer = lex(module=lexer_rules_v2)
	lexer.input(text)
	token = lexer.token()
	while token is not None:
		print (token.value)
		token = lexer.token()
