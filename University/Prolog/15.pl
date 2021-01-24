%male

male(sarkar).
male(kalam).
male(alam).
male(tuhin).
male(pranto).
male(sayed).
male(rana).
male(roni).
male(babu).

%female

female(samsunnahar).
female(kona).
female(runa).
female(rumi).
female(rekha).
female(asa).

%parents

parents(sarkar, kalam).
parents(sarkar, alam).
parents(sarkar, samsunnahar).
parents(kalam, tuhin).
parents(kalam, kona).
parents(tuhin, pranto).
parents(tuhin, sayed).
parents(samsunnahar, rumi).
parents(samsunnahar, runa).
parents(alam, rana).
parents(alam, roni).
parents(alam, rekha).
parents(rana, asa).
parents(rana, babu).


%input

input:-

	write("Enter Two Family Member Name: "), nl,
	
	read(X), nl,
	
	read(Y), nl,
	
	family(X, Y).
	
family(X, Y):-

	%son
	
	male(X), parents(Y, X),
	
	write("Mr. "), write(X), write(" is the son of Mr./Mrs. "), write(Y).
	
family(X, Y):-

	%father
	
	male(X), parents(X, Y),
	
	write("Mr. "), write(X), write(" is the father of Mr./Mrs. "), write(Y).
	
family(X, Y):-

	%daughter
	
	female(X), parents(Y, X),
	
	write("Mrs. "), write(X), write(" is the daughter of Mr./Mrs. "), write(Y).
	
family(X, Y):-

	%mother
	
	female(X), parents(X, Y),
	
	write("Mr. "), write(X), write(" is the mother of Mr./Mrs. "), write(Y).
	
family(X, Y):-

	%brother
	
	male(X), male(Y), parents(Z, X), parents(Z, Y),
	
	write("Mr. "), write(X), write(" and Mr. "), write(Y), write(" brother").

	
family(X, Y):-

	%sister
	
	female(X), female(Y), parents(Z, X), parents(Z, Y),
	
	write("Mrs. "), write(X), write(" and Mrs. "), write(Y), write(" sister").
	
	
family(X, Y):-

	%siblings
	
	parents(Z, X), parents(Z, Y), X \= Y,
	
	write("Mr./Mrs. "), write(X), write(" and Mr./Mrs. "), write(Y), write(" siblings").
	
	
family(X, Y):-

	%grandfather
	
	male(X), parents(X, Z), parents(Z, Y),
	
	write("Mr. "), write(X), write(" is the grandfather of Mr./Mrs. "), write(Y).
	
	
family(X, Y):-

	%grandmother
	
	female(X), parents(X, Z), parents(Z, Y),
	
	write("Mrs. "), write(X), write(" is the grandmother of Mr./Mrs. "), write(Y).
	
	
family(X, Y):-

	%grandson
	
	male(X), parents(Y, Z), parents(Z, X),
	
	write("Mr. "), write(X), write(" is the grandson of Mr./Mrs. "), write(Y).
	
	
family(X, Y):-

	%granddaughter
	
	female(X), parents(Y, Z), parents(Z, X),
	
	write("Mrs. "), write(X), write(" is the granddaughter of Mr./Mrs. "), write(Y).
	
	
family(X, Y):-

	%uncle
	
	male(X), parents(Z, X), parents(Z, P), parents(P, Y),
	
	write("Mr. "), write(X), write(" is the uncle of Mr./Mrs. "), write(Y).
	
	
family(X, Y):-

	%aunty
	
	female(X), parents(Z, X), parents(Z, P), parents(P, Y),
	
	write("Mrs. "), write(X), write(" is the aunty of Mr./Mrs. "), write(Y).
	
	
family(X, Y):-

	%nephew
	
	male(X), parents(Z, Y), parents(Z, P), parents(P, X),
	
	write("Mr. "), write(X), write(" is the nephew of Mr./Mrs. "), write(Y).
	
	
family(X, Y):-

	%niece
	
	female(X), parents(Z, Y), parents(Z, P), parents(P, X),
	
	write("Mr. "), write(X), write(" is the niece of Mr./Mrs. "), write(Y).
	