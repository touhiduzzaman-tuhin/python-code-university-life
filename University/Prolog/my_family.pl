%male

male(sarkar).
male(alam).
male(kalam).
male(mokbul).
male(baten).
male(rana).
male(mokter).
male(tuhin).
male(mamun).
male(mijanur).
male(biplob).
male(lablu).
male(babu).
male(sahin).
male(plabon).
male(polash).
male(akter).
male(selim).
male(samsul).
male(nurislam).
male(mukta).
male(sakil).
male(bilas).
male(kabbo).
male(naim).


%female

female(samsunnahar).
female(jahannar).
female(rubi).
female(reba).
female(munjhori).
female(rani).
female(rikta).
female(asa).
female(moni).
female(kona).
female(bonna).
female(ratna).
female(lavli).
female(munmun).
female(rumi).


parents(sarkar, alam).
parents(sarkar, kalam).
parents(sarkar, baten).
parents(sarkar, mokbul).
parents(sarkar, jahannar).
parents(sarkar, samsunnahar).
parents(samsunnahar, nuralam).
parents(samsunnahar, nurislam).
parents(samsunnahar, munjhori).
parents(nuralam, mukta).
parents(nurislam, sakil).
parents(munjhori, kabbo).
parents(munjhori, bilas).
parents(alam, rana).
parents(alam, mokter).
parents(alam, rani).
parents(alam, rikta).
parents(mokter, babu).
parents(mokter, sahin).
parents(rani, asa).
parents(rikta, moni).
parents(kalam, kona).
parents(kalam, tuhin).
parents(mokbul, mamun).
parents(mokbul, mijanur).
parents(mijanur, plabon).
parents(mijanur, polash).
parents(baten, biplob).
parents(baten, lablu).
parents(baten, ratna).
parents(ratna, munmun).
parents(ratna, akter).
parents(akter, selim).
parents(lablu, lavli).
parents(biplob, bonna).
parents(jahannar, samsul).
parents(jahannar, rubi).
parents(jahannar, reba).
parents(rubi, rumi).
parents(samsul, naim).



brother:-

	write("Enter Two Family Member Name: "), nl,
	
	read(X), nl,

	read(Y), nl,
	
	male(X), male(Y), parents(Z, X), parents(Z, Y),
	
	write("Their Relation Brother").















