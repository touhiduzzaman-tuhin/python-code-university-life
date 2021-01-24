%male

male(jamil).
male(sohel).
male(rafi).
male(rumi).
male(raj).
male(jarif).
male(saki).
male(orko).
male(ovi).

%female

female(runa).
female(riya).
female(najia).
female(ridima).
female(sufi).


%parents

parents(jamil, runa).
parents(jamil, sohel).
parents(sohel, najia).
parents(sohel, ridima).
parents(najia, saki).
parents(najia, orko).
parents(orko, ovi).
parents(rafi, raj).
parents(runa, rafi).
parents(runa, rumi).
parents(runa, riya).
parents(rumi, sufi).
parents(sufi, jarif).


input:-

	write("Enter two Name : "), nl,
	
	read(X), nl,
	
	read(Y), nl,
	
	family(X, Y).
	
	
family(X, Y):-

	%son
	
	male(X), parents(Y, X),
	
	write(X), write(" is son of Mr. "), write(Y).
	
	
family(X, Y):-

	%father
	
	male(X), parents(X, Y),
	
	write(X), write(" is Father of Mr. "), write(Y).
	
family(X, Y):-

	%daughter
	
	female(X), parents(Y, X),
	
	write(X), write(" is daughter of Mr. "), write(Y).
	
family(X, Y):-

	%mother
	
	female(X), parents(X, Y),
	
	write(X), write(" is mother of Mr. "), write(Y).
	
family(X, Y):-

	%brother
	
	male(X), male(Y), parents(Z, X), parents(Z, Y),
	
	write(X), write(" and "), write(Y), write(" are brother").
	
family(X, Y):-

	%sister
	
	female(X), female(Y), parents(Z, X), parents(Z, Y),
	
	write(X), write(" and "), write(Y), write(" are sister").
	


family(X, Y):-

	%siblings
	
	parents(Z, X), parents(Z, Y), X \= Y,
	
	write(X), write(" and "), write(Y), write(" are siblings").
	
family(X, Y):-

	%grandfather
	
	male(X), parents(X, Z), parents(Z, Y),
	
	write(X), write(" is grandfather and "), write(Y), write(" is grandson").

	
family(X, Y):-

	%grandmother
	
	female(X), parents(X, Z), parents(Z, Y),
	
	write(X), write(" is grandmother and "), write(Y), write(" is grandson").

	

ancestor(X, Y):-
	
	parents(X, Z).
	
ancestor(X, Y):-

	parents(X, Z),
	
	ancestor(Z, Y).








