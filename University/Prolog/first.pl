male(tuhin).
male(shahed).
female(piya).
female(riya).
likes(tuhin, pizza).
likes(tuhin, biriyani).
likes(shahed, pizza).
pizza_lover(X):-
    likes(X,pizza).
