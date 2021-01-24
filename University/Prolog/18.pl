%male

male(jamil).
male(sohel).
male(rafi).
male(rafi).
male(raj).
male(sufi).
male(jarif).
male(orko).
male(ovi).
male(rana).


%female

female(runa).
female(rumi).
female(riya).
female(najia).
female(ridima).
female(saki).

%parents

parents(jamil, runa).
parents(jamil, sohel).
parents(runa, rafi).
parents(runa, rumi).
parents(runa, riya).
parents(sohel, najia).
parents(sohel, ridima).
parents(rafi, raj).
parents(rumi, sufi).
parents(sufi, jarif).
parents(najia, saki).
parents(najia, orko).
parents(orko, ovi).
parents(orko, rana).


input:-

	write("Enter Two Familly Member Name: "), nl,
	
	read(X), nl,
	
	read(Y), nl,
	
	family(X, Y).
	
family(X, Y):-

	%son
	
	male(X), parents(Y, X),
	
	write("Mr. "), write(X), write(" is the son of "), write(Y).



family(X, Y):-

	%daughter
	
	female(X), parents(Y, X),
	
	write("Mrs. "), write(X), write(" is the daughter of "), write(Y).



family(X, Y):-

	%father
	
	male(X), parents(X, Y),
	
	write("Mr. "), write(X), write(" is the father of "), write(Y).




family(X, Y):-

	%mother
	
	female(X), parents(X, Y),
	
	write("Mr. "), write(X), write(" is the mother of "), write(Y).



family(X, Y):-

	%brother
	
	male(X), male(Y), parents(Z, X), parents(Z, Y),
	
	write("Mr. "), write(X), write(" and Mr. "), write(Y), write(" are brother").



family(X, Y):-

	%sister
	
	female(X), female(Y), parents(Z, X), parents(Z, Y),
	
	write("Mrs. "), write(X), write(" and Mrs. "), write(Y), write(" are sister").


family(X, Y):-

	%siblings
	
	parents(Z, X), parents(Z, Y), X \= Y,
	
	write(X), write(" and "), write(Y), write(" are siblings").


family(X, Y):-

	%grandfather
	
	male(X), parents(X, Z), parents(Z, Y),
	
	write("Mr. "), write(X), write(" is the grandfather of "), write(Y).


family(X, Y):-

	%grandmother
	
	female(X), parents(X, Z), parents(Z, Y),
	
	write("Mrs. "), write(X), write(" is the grandmother of "), write(Y).



family(X, Y):-

	%grandson
	
	male(X), parents(Z, X), parents(Y, Z),
	
	write("Mr. "), write(X), write(" is the grandson of "), write(Y).



family(X, Y):-

	%granddaughter
	
	female(X), parents(Z, X), parents(Y, Z),
	
	write("Mrs. "), write(X), write(" is the granddaughter of "), write(Y).



family(X, Y):-

	%uncle
	
	male(X), parents(Z, X), parents(Z, P), parents(P, Y),
	
	write("Mr. "), write(X), write(" is the uncle of "), write(Y).



family(X, Y):-

	%aunty
	
	female(X), parents(Z, X), parents(Z, P), parents(P, Y),
	
	write("Mrs. "), write(X), write(" is the aunty of "), write(Y).

	
family(X, Y):-

	%nephew
	
	male(X), parents(Z, Y), parents(Z, P), parents(P, X),
	
	write("Mr. "), write(X), write(" is the nephew of "), write(Y).



family(X, Y):-

	%niece
	
	female(X), parents(Z, Y), parents(Z, P), parents(P, X),
	
	write("Mrs. "), write(X), write(" is the niece of "), write(Y).



family(X, Y):-

	%ancestor
	
	parents(X, Z), family(Z, Y), nl,
	
	write("They Are Ancestor").
	

family(X, Y):-

	%cousin
	
	parents(A, X), parents(B, Y), parents(Z, A), parents(Z, B),
	
	write("They Are Cousin").


























































































































































