get_input:-

	write("Enter First Number: "),
	read(X), nl,
	
	write("Enter Second Number: "),
	read(Y), nl,
	
	mul(X, Y).
	
mul(X, Y):-

	M is (X*Y),
	write("Result is: "),
	write(M).