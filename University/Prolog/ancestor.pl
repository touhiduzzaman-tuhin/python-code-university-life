parents(chester, irvin).
parents(chester, clearnce).
parents(chester, mildred).
parents(irvin, ken).
parents(irvin, ron).
parents(clearnce, shirley).
parents(clearnce, sharon).
parents(clearnce, charlie).
parents(mildred, mary).
parents(ken, nora).
parents(ken, elizabeth).


ancestor(X, Y):-
	
	parents(X, Z).
	
ancestor(X, Y):-

	parents(X, Z),
	
	ancestor(Z, Y).
