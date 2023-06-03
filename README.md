# EEM16-Design-TestSuite
*Test Suite for Design Assessment 1 for EE M16 Spring 23'*

**Creates random test cases for the design assessment task 1 and task 2 (as of now).**

## Installation
To install the repository, run
```
git clone https://github.com/arnavmarda/EEM16-Design-TestSuite.git
```
in your terminal.

*Note - You need to have python installed to run this.*

You need to also download the python package gmpy2. To do this run:
```
pip install gmpy2
```

## Usage
Currently I have only uploaded tests for Task 1 and Task 2. To run the code run:
```
python3 test_1.py n > test.txt
```
or 
```
python3 test_2.py n > test.txt
```
where *n* is the number of test cases you want and *test.txt* is the name of the file you want to send the test cases to.

You can then use the "Test Vectors" feature on Logisim to test your circuit.

## Task-wise Testing Information
1. Task 1 - *n* test cases randomly generated. Only valid test cases implemented. No edge cases implemented.
2. Task 2 - *n* test cases randomly generated. In addition to *n* test cases, there are 64 other cases checking for circuit working on "+00", "-00", "+99", and "-99". Apart from these 4 cases, there are 20 cases with incorrect SIGN input, 20 cases with incorrect D1 and D0 and 20 cases with incorrect SIGN, D1 and D0. 
