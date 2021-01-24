%Male

male(jamil).
male(sohel).
male(rafi).
male(rumi).
male(raj).
male(ovi).
male(jarif).
male(orko).

%Female

female(runa).
female(riya).
female(najia).
female(ridima).
female(sufi).
female(saki).

%Parents

parent(jamil, runa).
parent(jamil, sohel).
parent(runa, rafi).
parent(runa, rumi).
parent(runa, riya).
parent(sohel, najia).
parent(sohel, ridima).
parent(rafi, raj).
parent(sumi, sufi).
parent(najia, saki).
parent(najia, orko).
parent(sufi, jarif).
parent(orko, ovi).
parent(rumi, sufi).


input:-

	write("Enter Two Family Member name :"), nl,

	read(X), nl,
	
	read(Y), nl,
	
	family(X, Y).
	
	
family(X, Y):-
		
		%son
		
		male(X), parent(Y, X),
		
		write(X), write(" is son and his parent is "), write(Y).
		
		
family(X, Y):- 

		%daughter
		
		female(X), parent(Y, X),
		
		write(X), write(" is daughter and his parent is "), write(Y).
		

family(X, Y):-

		%brother

		male(X), male(Y), parent(Z, X), parent(Z, Y),
		
		write(X), write(" and "), write(Y), write(" are brother").
		
family(X, Y):-

		%sister

		female(X), female(Y), parent(Z, X), parent(Z, Y),
		
		write(X), write(" and "), write(Y), write(" are sister").
		
family(X, Y):-

		%father

		male(X), parent(X, Y),
		
		write(X), write(" is father and "), write(Y), write(" is child ").
		

family(X, Y):-
		
		
		%mother
	
		female(X), parent(X, Y),
		
		write(X), write(" is mother and "), write(Y), write(" is child"). 
		
family(X, Y):-

		%grand_father
		
		male(X), parent(X, Z), parent(Z, Y),
		
		write(X), write(" is grand father and "), write(Y), write(" is grand son"). 
		
		
family(X, Y):-

		%grand_mother
		
		female(X), parent(X, Z), parent(Z, Y),
		
		write(X), write(" is grand mother and "), write(Y), write(" is grand son"). 
		
		
family(X, Y):-

		%siblings
		
		parent(Z, X), parent(Z, Y), X \= Y,
		
		write(X), write(" and "), write(Y), write(" are siblings").
		
family(X, Y):-

		%uncle
		
		male(X),  parent(Z, X), parent(Z, P), parent(P, Y),
		
		write(X), write(" is uncle and "), write(Y), write(" is nepew").
		
		
		
		
family(X, Y):-

		%aunty
		
		female(X),  parent(Z, X), parent(Z, P), parent(P, Y),
		
		write(X), write(" is aunty and "), write(Y), write(" is nepew").
		
		
		
family(X, Y):-

		%nepew
		
		male(X),  parent(Z, Y), parent(Z, P), parent(P, X),
		
		write(X), write(" is nepew and "), write(Y), write(" is uncle").
		
		
family(X, Y):-

		%nice
		
		female(X),  parent(Z, Y), parent(Z, P), parent(P, X),
		
		write(X), write(" is nice and "), write(Y), write(" is uncle").
		
		