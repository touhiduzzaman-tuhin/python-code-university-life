input:-

	write("Enter Two Number: "), nl,
	
	read(X), nl,
	
	read(Y), nl,
	
	sub(X, Y).
	
sub(X, Y):-

	S is (X-Y),
	
	write("Result is : "), write(S).
	
	