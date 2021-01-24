input:-

	write("Enter Two Number: "), nl,
	
	read(X), nl,
	
	read(Y), nl,
	
	res(X, Y).
	
res(X, Y):-

	S is div(X,Y),
	
	write("Result is : "), write(S).
	
	