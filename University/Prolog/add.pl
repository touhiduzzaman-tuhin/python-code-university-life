%addition

get_input:-

	write("Enter First Number: "),
	read(X), nl,
	write("Enter Second number: "),
	read(Y), nl,
	
	add(X, Y).
	
add(X, Y):-

	S is (X+Y),
	write("Result is: "), nl,
	write(S).