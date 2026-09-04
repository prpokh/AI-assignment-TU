% Facts
animal(giraffe).
animal(horse).
animal(dog).

bigger(giraffe, horse).
bigger(horse, dog).

% Print verification helper
print_footer :-
    nl,
    write('-----------------------------'), nl,
    write('Name: [Prasanna Pokharel] | Roll: [24] | Lab: Lab II-3'), nl.