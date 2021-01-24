get_input:-

	write("Enter A Number: "),
	read(X), nl,
	
	even_odd(X).
	
even_odd(X):-

		M is mod(X, 2), 
		M = 0,
		write("Even Number: ");
		
		M is mod(X, 2),
		M = 1,
		write("Odd Number: ").