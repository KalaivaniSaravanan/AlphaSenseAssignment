# AlphaSenseAssignment

SDET Home Assignment - QA Strategy and Coding Task
Problem 1: Happy QA (Coding Assignment)
Problem Description
This task is to help Bob, a QA, select the maximum number of releases that can be validated within a 10-day sprint. Bob can only work on one release at a time, and releases cannot extend beyond the 10th day of the sprint. The input consists of a list of releases, and the goal is to find the maximum number of releases Bob can validate within the given constraints.

Input
The input comes from a file releases.txt, which contains multiple lines with two integers per line:

The day of the sprint the release is delivered.
The number of days required to validate the release.
Example of releases.txt:
1 1
2 1
3 1
9 1
10 4
10 2
9 5
10 3
4 5

Output
The program produces an output file solution.txt, which contains:
The maximum number of releases that Bob can validate.
The start and end days for each validated release.
Example of solution.txt:
5
1 1
2 2
3 3
4 8
9 9

