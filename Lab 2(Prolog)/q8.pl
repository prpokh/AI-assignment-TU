% Domain list of all students
student(radha).
student(rakesh).
student(anish).
student(rekha).
student(bibek).

% Explicit positive facts: who studied
studied(radha).
studied(rakesh).
studied(anish).

% Rules
pass(X) :- studied(X).
happy(X) :- pass(X).

% Negation rule: did not study
did_not_study(X) :-
    student(X),
    \+ studied(X).

print_footer :-
    nl,
    write('-----------------------------'), nl,
    write('Name: [Prasanna Pokharel] | Roll: [24] | Lab: Lab II-8'), nl.