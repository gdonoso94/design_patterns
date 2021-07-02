# Design patterns

This repository is, indeed, a repository of desing patterns I will be studyigin _hopefully_ during summer 2021. 

Basically it intends to cover _Elements of Reusable Object-Oriented Software_ book, from Erich Gamma et al.

The implementations will be in Python.

---

## Creational patterns

This patterns intend to abstract de class instantiation process.

The common example for all five patterns is a _Maze_.

A _Maze_ is defined as a set of _Rooms_. A _Room_ knows its neighbors. Possible neighbors are another _Room_, a _Wall_
or a _Door_ to another _Room_.

### Abstract factory

* Provides an interface for creating families of related or dependent objects without specifying their concrete class.
* **Applicability**: When
    * a system should be independent of how its products are created, composed and represented
    * a system should be configured with one of multiple families of products
    * a family of related product objects is designed to be used together.
    * you want to provide a class library of products, and you want to reveal just their interfaces, not their 
      implementations
      
### Builder

* Separates the construction of a complex object from its representation so that the same construction process can 
create different representations.
* **Applicability**: When
    * the algorithm for creating a complex object sholud be independent of the parts that make up the object and 
    how they're assembled
    * the construction process must allow different representations for the object that is constructed
  
### Factory method

* Defines an interface for creating an object, but let subclasses decide which class to instantiate. 
Factory method lets a class defer instantiation to subclasses.