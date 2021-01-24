get:-

	write("Enter A number: "),
	read(N), nl,
	Y = 1,
	
	loop(Y,N).
	
	loop(Y,N):-

		between(Y,N,X),
		write(X),
		N>=X, !.
		loop(Y,X).