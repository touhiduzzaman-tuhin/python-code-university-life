input:-

	write("Enter A Number: "),
	
	read(X), nl,
	
	write("Enter Another Number: "),
	
	read(Y), nl,
	
	max(X, Y).
	
max(X, Y):-

		X > Y,
			
			write("Min Number: "), write(Y);
		
		X < Y,
		
			write("Min Number: "), write(X);
		
		X = Y,
			
			write("Two Number is same").