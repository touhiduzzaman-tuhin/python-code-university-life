get_input:-

	write("Enter First Number: "),
	read(X), nl,
	
	write("Enter Second Number: "),
	read(Y), nl,
	
	division(X, Y).
	
division(X, Y):-

	D is div(X,Y),
	write("Result is: "),
	write(D).