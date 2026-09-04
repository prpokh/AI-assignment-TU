% (a) Gender specifications
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

% (b) Parent relationships: parent(Parent, Child)
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

print_footer :-
    nl,
    write('-----------------------------'), nl,
    write('Name: [Prasanna Pokharel] | Roll: [24] | Lab: Lab II-4'), nl.