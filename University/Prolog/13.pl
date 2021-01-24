%male

male(jamil).
male(sohel).
male(rafi).
male(rumi).
male(raj).
male(jarif).
male(orko).
male(ovi).

%female

female(runa).
female(riya).
female(sufi).
female(najia).
female(ridima).
female(saki).

%parents

parents(jamil, runa).
parents(jamil, sohel).
parents(sohel, najia).
parents(sohel, ridima).
parents(najia, saki).
parents(najia, orko).
parents(orko, ovi).
parents(runa, rafi).
parents(runa, rumi).
parents(runa, riya).
parents(rafi, raj).
parents(rumi, sufi).
parents(sufi, jarif).


input:-

	write("Enter Rwo Family Member Name : "), nl,

	read(X), nl, 
	
	read(Y), nl, 

	family(X, Y).

family(X, Y):-

	%son
	
	male(X), parents(Y, X),
	
	write(X), write(" is the son of Mr./Mrs. "), write(Y).


family(X, Y):-

	%daughter
	
	female(X), parents(Y, X),
	
	write(X), write(" is the daughter of Mr./Mrs. "), write(Y).



family(X, Y):-

	%father
	
	male(X), parents(X, Y),
	
	write(X), write(" is the father of Mr./Mrs. "), write(Y).


family(X, Y):-

	%mother
	
	female(X), parents(X, Y),
	
	write(X), write(" is the mother of Mr./Mrs. "), write(Y).


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
	
	write(X), write(" and "), write(Y), write(" siblings").	
	
	
family(X, Y):-

	%grandfather
	
	male(X), parents(X, Z), parents(Z, Y),
	
	write(X), write(" is grandfather of Mr./Mrs.  "), write(Y).	
	

family(X, Y):-

	%grandson
	
	male(X), parents(Y, Z), parents(Z, X),
	
	write(X), write(" is grandson of Mr./Mrs.  "), write(Y).
	
	
family(X, Y):-

	%granddaughter
	
	female(X), parents(Y, Z), parents(Z, X),
	
	write(X), write(" is granddaughter of Mr./Mrs.  "), write(Y).
	
	
family(X, Y):-

	%grandmother
	
	female(X), parents(X, Z), parents(Z, Y),
	
	write(X), write(" is grandmother of Mr./Mrs.  "), write(Y).		
	
	
family(X, Y):-

	%uncle
	
	male(X), parents(Z, X), parents(Z, P), parents(P, Y),
	
	write(X), write(" is uncle of Mr./Mrs.  "), write(Y).		

	
family(X, Y):-

	%aunty
	
	female(X), parents(Z, X), parents(Z, P), parents(P, Y),
	
	write(X), write(" is aunty of Mr./Mrs.  "), write(Y).	
	
	
family(X, Y):-

	%nepew
	
	male(X), parents(Z, Y), parents(Z, P), parents(P, X),
	
	write(X), write(" is nepew of Mr./Mrs.  "), write(Y).	
	
	
	
family(X, Y):-

	%nice
	
	female(X), parents(Z, Y), parents(Z, P), parents(P, X),
	
	write(X), write(" is nice of Mr./Mrs.  "), write(Y).	
		
	
	
	
	
	
	
	
	
	
	
	
	





