input:-

	write("Enter A Number: "),
	
	read(X), nl,
	
	write("Enter Another Number: "),
	
	read(Y), nl,
	
	max(X, Y).
	
max(X, Y):-

		X > Y,
			
			write("Max Number: "), write(X);
		
		X < Y,
		
			write("Max Number: "), write(Y);
		
		X = Y,
			
			write("Two Number is same").