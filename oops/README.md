OBJECT-ORIENTED PROGRAMMING :-
        Oops is an approach to solve problems using classes and objects.

Imagine you are working at espncricinfo or cricbuzz,and your task is to perform player analysis.

First I will do my task,by following procedural approach(only focusing on logic and creating functions for reusability of code):

Before doing player analysis,we need to store player details like firstName,lastName,scores etc

Here it is better to use dictionary to store player details,because each player has multiple attributes.

                                    virat={
                                        "firstName":"virat",
                                        "lastName":"kholi",
                                        scores:[]
                                    }
so,whenever i need to add virat score in the list i use append() method.

Now,let us create functions,to perform player(virat)  analysis on above data we gather.

                                     def get_average(player):
                                          return sum(player[scores])/len(player[scores])

similar to get_average() function,we can write functions for,in last three matches what is the maximum score or minumum score etc.

For different players (Dhoni,rohit,gaikwad,samson),we used to call same functions(which is reusability of code).

If we clearly observe,attributes(variables to represent player details) are same for all players,but those attributes  values will be different for each player.By following this procedural approach we need to repeat this attributes for each player again and again.

so,attributes and functions for every player is same right.

class : is a blueprint or template of  a object.here it consists attributes and methods(functions).

The idea of class is simple,combining attributes  and methods of an entity(any living or non-living thing)  as single unit.

In above scenario also,every player share common attributes and methods but attribute values are different.so by using class we are creating a template to represent every player.

object : is an instance of a class.

In this scenario,each object represents a different player(virat,dhoni,gaikwad,samson)

                                        class player:
                                            #Intializing state of an object using constructor 
                                              def __init__(self,firstName,lastName,scores):
                                                 self.firstName=firstName
                                                 self.lastName=lastName
                                                 self.scores=scores

                                        #object creation using player class(template)
                                        virat=player("virat","kholi",[20,30,30])
                                        dhoni=palyer("Ms","dhoni",[30,30,50])
                                         
Multiple instances can be created by using a single class,where in every instance its state(attribute values) would be different.

OPERATOR OVERLOADING :

Usually +,-,/,%,*,<,>,==  etc are operators used to perform arthimetic operations like addition,subtraction,multiplication etc

By default,we use less than operator(<) as 10<20,it returns True because 10 is small number than 20 right.

20<10 ->here it returns False

In conclusion we can say less than operator is used to compare two values right,that its default nature.

But,operator overloading means we can overload the opeartor behaviour(we can compare two objects based on particular behavior).
 