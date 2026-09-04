% Base case: 0! = 1
factorial(0, 1).

% Recursive step
factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, SubResult),
    Result is N * SubResult.

% Interactive caller displaying student info
calculate_factorial :-
    write('Enter a number: '),
    read(N),
    factorial(N, Ans),
    format('Factorial of ~w is ~w.~n', [N, Ans]),
    write('-----------------------------'), nl,
    write('Name: [Prasanna Pokharel] | Roll: [24] | Lab: Lab II-6'), nl.