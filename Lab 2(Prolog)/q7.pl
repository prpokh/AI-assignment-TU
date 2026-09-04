% fib(Index, Value)
fib(0, 0).
fib(1, 1).
fib(N, Val) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fib(N1, V1),
    fib(N2, V2),
    Val is V1 + V2.

% Helper to iterate from 0 to N
generate_fib(Current, Limit) :-
    Current =< Limit,
    fib(Current, Val),
    format('~w ', [Val]),
    Next is Current + 1,
    generate_fib(Next, Limit).
generate_fib(Current, Limit) :-
    Current > Limit, nl.

% Interactive execution predicate
display_fibonacci :-
    write('Enter limit of terms (N): '),
    read(N),
    write('Fibonacci Sequence: '),
    generate_fib(0, N),
    write('-----------------------------'), nl,
    write('Name: [Prasanna Pokharel] | Roll: [24] | Lab: Lab II-7'), nl.