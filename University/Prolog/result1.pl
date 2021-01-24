result(tuhin, 3.84).
result(shahed, 3.00).
result(shawon, 3.50).
result(imran, 3.60).
result(shanto, 3.70).
result(sudip, 3.20).
result(vabna, 3.30).
result(ratul, 3.10).
result(shuva, 4.00).
result(arif, 3.90).
result(shoha, 3.30).
result(pranto, 3.90).
result(roman, 3.10).
result(sayed, 3.70).

get_result:-

	write("Enter Name: "), nl,
	read(X), nl,
	result(X, Y), nl,
	write(Y).
	