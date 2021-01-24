get_input:-

	write("Enter First Number: "),
	read(X), nl,
	
	write("Enter Second Number: "),
	read(Y), nl,
	
	sub(X, Y).
	
sub(X, Y):-

	S is (X-Y),
	write("Result is: "),
	write(S).