%male 

male(tuhin).
male(pranto).
male(shawon).
male(akash).
male(sayed).
male(babu).
male(juyel).
male(imran).
male(polash).
male(rana).


%female


female(suva).
female(maya).
female(sarmin).
female(nupur).
female(mim).
female(keya).
female(bipa).
female(rima).


%parents


parents(tuhin, pranto).
parents(tuhin, shawon).
parents(tuhin, suva).
parents(pranto, akash).
parents(pranto, maya).
parents(akash, sarmin).
parents(akash, nupur).
parents(akash, mim).
parents(shawon, sayed).
parents(shawon, babu).
parents(sayed, juyel).
parents(sayed, imran).
parents(imran, keya).
parents(suva, polash).
parents(suva, rana).
parents(rana, bipa).
parents(rana, rima).


%input

input:-

	write("Enter Two Family Member Name: "), nl,
	
	read(X), nl,
	
	read(Y), nl,
	
	family(X, Y).

	
family(X, Y):-

	%son
	
	male(X), parents(Y, X),
	
	write(X), write(" is son of Mr./Mrs. "), write(Y).
	

family(X, Y):-

	%daughter
	
	female(X), parents(Y, X),
	
	write(X), write(" is daughter of Mr./Mrs. "), write(Y).


family(X, Y):-

	%father
	
	male(X), parents(X, Y),
	
	write("Mr. "), write(X), write(" is father of "), write(Y).



family(X, Y):-

	%mother
	
	female(X), parents(X, Y),
	
	write("Mrs. "), write(X), write(" is mother of "), write(Y).


family(X, Y):-

	%brother
	
	male(X), male(Y), parents(Z, X), parents(Z, Y),
	
	write("Mr. "), write(X), write(" Mr. "), write(Y), write(" are brother").

	
family(X, Y):-

	%sister
	
	female(X), female(Y), parents(Z, X), parents(Z, Y),
	
	write("Mrs. "), write(X), write(" Mrs. "), write(Y), write(" are sister").



family(X, Y):-

	%siblings
	
	parents(Z, X), parents(Z, Y), X \= Y,
	
	write("Mr./Mrs. "), write(X), write(" Mr./Mrs. "), write(Y), write(" are siblings").



family(X, Y):-

	%grandfather
	
	male(X), parents(X, Z), parents(Z, Y),
	
	write("Mr. "), write(X), write(" is grandfather of "), write(Y).


family(X, Y):-

	%grandmother
	
	female(X), parents(X, Z), parents(Z, Y),
	
	write("Mrs. "), write(X), write(" is grandmother of "), write(Y).


	
family(X, Y):-

	%grandson
	
	male(X), parents(Z, X), parents(Y, Z),
	
	write("Mr. "), write(X), write(" is grandson of "), write(Y).


family(X, Y):-

	%granddaughter
	
	female(X), parents(Z, X), parents(Y, Z),
	
	write("Mrs. "), write(X), write(" is granddaughter of "), write(Y).	
	
	
	
family(X, Y):-

	%uncle
	
	male(X), parents(Z, X), parents(Z, P), parents(P, Y),
	
	write("Mr. "), write(X), write(" is uncle of "), write(Y).
	
family(X, Y):-

	%aunty
	
	female(X), parents(Z, X), parents(Z, P), parents(P, Y),
	
	write("Mrs. "), write(X), write(" is uncle of "), write(Y).
	
	
	
family(X, Y):-

	%nephew
	
	male(X), parents(Z, Y), parents(Z, P), parents(P, X),
	
	write("Mr. "), write(X), write(" is nephew of "), write(Y).	
	
	
	
	
family(X, Y):-

	%niece
	
	female(X), parents(Z, Y), parents(Z, P), parents(P, X),
	
	write("Mr. "), write(X), write(" is niece of "), write(Y).
	
	
	
	
	
	
	
	
	


