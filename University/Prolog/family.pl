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


son(X, Y):-

	male(X), parent(Y, X).
	

	
daughter(X, Y):-

	female(X), parent(Y, X).
	

father(X, Y):-

	male(X), parent(X, Y).
		

mother(X, Y):-

	female(X), parent(X, Y).


brother(X, Y):-

	male(X), male(Y), parent(Z, X), parent(Z, Y).
	

sister(X, Y):-

	female(X), female(Y), parent(Z, X), parent(Z, Y).
	

grandfather(X, Y):-

	male(X), parent(X, Z), parent(Z, Y).
	
	
grandmother(X, Y):-

	female(X), parent(X, Z), parent(Z, Y).
	

uncle(X, Y):-

	brother(X, Z), parent(Z, Y).
	

siblings(X, Y):-

    parent(Z, X), parent(Z, Y), X /= Y.