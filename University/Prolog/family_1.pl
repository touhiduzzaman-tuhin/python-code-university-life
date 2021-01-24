male(rahim).
male(karim).
male(kabir).
male(roy).
female(tisa).
female(jesi).
parent(rahim, karim).
parent(rahim, kabir).
parent(kabir, roy).
parent(karim, tisa).
parent(karim, jesi).

son(X, Y):-

	male(X), parent(Y, X).
	
daughter(X, Y):-

	female(Y), parent(Y, X).
	
siblings(X, Y):

	parent(Z, X), parent(Z, Y), X != Y.