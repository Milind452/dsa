# Data Structures and Algorithms

## How to solve problems
---
1. Understand the entire problem statement
2. Find out the inputs
3. Find out the outputs
4. Work out examples to define a relationship between inputs and outputs and also get some test cases
5. Design systematic steps as to how a human would solve the problem
6. Break the problem into manageable pieces before starting to code
7. Develop incrementally and keep testing along the way
8. Don't try to optimize prematurely; get a working solution first and if required, build on that solution for more efficiency

## Big O Notation
---
It's a notation used to quantify the efficiency of an algorithm

 `O(<expression with n>)`

 `O` stands for order of the algorithm and `n` is the size of the input to the algorithm

 Examples:

```
def foo(n):
	for i in range(n):
		print(i)
# O(n)
```
```
def bar(n):
	for i in range(n):
		for j in range(n):
			print(i)
# O(n^2)
```

## Data Structures
---
Data structures are containers that organize and group data together in different ways

### Arrays and Linked Lists
---

> #### **Lists**
> - Data structure with an order and no fixed length.
> - Lists can store any type of data.
> - They also do not have an index.
> - They are not stored in continuous blocks of memory.
> - NOTE: Python lists are slightly different. They are basically (dynamic) arrays with some high level language features.

> #### **Arrays**
> - Arrays are lists with an order and fixed length
> - They have an index
> - They are stored in continuous memory locations

