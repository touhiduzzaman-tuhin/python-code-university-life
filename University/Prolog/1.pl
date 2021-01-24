input:-

	write("Enter Two Number: "), nl,
	
	read(X), nl, 
	
	read(Y), nl, 
	
	add(X, Y).
	
add(X, Y):-

	S is (X+Y),
	
	write("Result is : "), write(S).