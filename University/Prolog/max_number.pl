get_input:-

	write("Enter A Number: "),
	read(X), nl,
	
	write("Enter Another Number: "),
	read(Y), nl,
	
	max(X, Y).
	
max(X, Y):-

	X > Y,
	
	write("Max Number is: "), write(X);
	
	X < Y,
	
	write("Max Number is: "), write(Y).