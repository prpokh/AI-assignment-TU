% Base Knowledge Base
male(tom).
male(bob).
male(pat).
male(jim).
male(dave).

female(pam).
female(liz).
female(mary).
female(ann).
female(sue).
female(angela).

parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, mary).
parent(bob, ann).
parent(bob, pat).
parent(bob, sue).
parent(pat, jim).
parent(sue, dave).
parent(sue, angela).

% Rules
grandparent(GP, GC) :- 
    parent(GP, P), 
    parent(P, GC).

granddaughter(GD, GP) :- 
    female(GD), 
    grandparent(GP, GD).

common_parent(X, Y) :- 
    parent(P, X), 
    parent(P, Y), 
    X \= Y.

sibling(X, Y) :- 
    parent(P, X), 
    parent(P, Y), 
    X \= Y.

sister(Sister, Person) :- 
    female(Sister), 
    parent(P, Sister), 
    parent(P, Person), 
    Sister \= Person.

uncle(Uncle, NieceNephew) :- 
    male(Uncle), 
    parent(P, NieceNephew), 
    sibling(Uncle, P).

print_footer :-
    nl,
    write('-----------------------------'), nl,
    write('Name: [Prasanna Pokharel] | Roll: [24] | Lab: Lab II-5'), nl.