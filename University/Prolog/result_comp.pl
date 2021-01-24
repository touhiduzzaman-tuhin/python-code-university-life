%SectionA
result(tuhin, 3.84).
result(shahed, 3.00).
result(shawon, 3.50).
result(imran, 3.60).
result(shanto, 3.70).
result(sudip, 3.20).
result(vabna, 3.30).
%SectionB
result(ratul, 3.10).
result(shuva, 4.00).
result(arif, 3.90).
result(shoha, 3.30).
result(pranto, 3.90).
result(roman, 3.10).
result(sayed, 3.70).

get_result:-
		
		write("Write the name whose result you want to know of Section A: "), nl,
		read(X), nl,
		result(X, Y), nl,
		write("Section A Student Result is : "), nl,
		write(Y), nl,
		
		write("Write the name whose result you want to know of Section B: "), nl,
		read(P), nl,
		result(P, Q), nl,
		write("Section B Student Result is: "), nl,
		write(Q), nl,
		
		compare(Y, Q).
		

compare(Y, Q):-
	
		Y > Q, nl,
		write("Section A Student is Best");
		Y < Q, nl,
		write("Section B Student is Best");
		Y =:= Q, nl,
		write("Two Student are same").
		
		
		
		