input:-

	write("Enter Two Number: "), nl,
	
	read(X), nl,
	
	read(Y), nl,
	
	mul(X, Y).
	
mul(X, Y):-

	S is (X*Y),
	
	write("Result is : "), write(S).
	
	