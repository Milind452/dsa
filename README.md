# Data Structures and Algorithms

## How to solve problems
1. Understand the entire problem statement
2. Find out the inputs
3. Find out the outputs
4. Work out examples to define a relationship between inputs and outputs and also get some test cases
5. Design systematic steps as to how a human would solve the problem
6. Break the problem into manageable pieces before starting to code
7. Develop incrementally and keep testing along the way
8. Don't try to optimize prematurely; get a working solution first and if required, build on that solution for more efficiency

## Big O Notation
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
