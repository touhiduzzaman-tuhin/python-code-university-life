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

	

ancestor(X, Y):-
	
	parents(X, Y).
	
ancestor(X, Y):-

	parents(X, Z),
	
	ancestor(Z, Y).








