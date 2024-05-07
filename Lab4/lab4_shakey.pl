
% TASK A - Shakey

% All actions shakey can take
act( go(X,Y),                                               % action 
     [at(shackey, X), passage(X, Y)],                       % pre-conditions
     [at(shackey, X)],                                      % delete
     [at(shackey, Y)]                                       % add
     ).

act( climbup(B),       
     [at(shackey, X), at(B, X), box(B), on(shackey, floor)], 
     [on(shackey, floor)], 
     [on(shackey, B)]                                       
     ).

act( climbdown(B),
     [on(shackey, B), box(B)],
     [on(shackey, B)],
     [on(shackey, floor)]
     ).


act( turnon(L),                                 
     [at(shackey, X), at(B, X), on(shackey, B), lightswitch(L, X), lightoff(X)],
     [lightoff(X)],
     [lighton(X)]
     ).

act( turnoff(L),
     [at(shackey, X), at(B, X), on(shackey, B), lightswitch(L, X), lighton(X)],
     [lighton(X)],
     [lightoff(X)]
     ).
     
     
act( push(B,X,Y),
     [at(shackey, X), at(B, X), on(shackey, floor), box(B), passage(X,Y)],
     [at(shackey, X),at(B, X)],
     [at(shackey, Y),at(B, Y)]
     ).
     

% Set goal states for shakey!
%goal_state( [at(shackey, room1) ]).
%goal_state( [lightoff(room1) ]).
goal_state( [at(box2, room2) ]).

% Setting up enviroment 
initial_state(
     [
      passage(door1, room1),
      passage(room1, door1),
      passage(door1, corridor),
      passage(corridor, door1),

      passage(door2, room2),
      passage(room2, door2),
      passage(door2, corridor),
      passage(corridor, door2),

      passage(door3, room3),
      passage(room3, door3),
      passage(door3, corridor),
      passage(corridor, door3),

      passage(door4, room4),
      passage(room4, door4),
      passage(door4, corridor),
      passage(corridor, door4),
      
      at(box1, room1),
      at(box2, room1),
      at(box3, room1),
      at(box4, room1),
      at(shackey, room3),
      on(shackey, floor),
      
      box(box1),
      box(box2),
      box(box3),
      box(box4),
      
      lightswitch(light1, room1),
      lightswitch(light2, room2),
      lightswitch(light3, room3),
      lightswitch(light4, room4),
      
      lighton(room1),
      lightoff(room2),
      lightoff(room3),
      lighton(room4)
      
     ]).
