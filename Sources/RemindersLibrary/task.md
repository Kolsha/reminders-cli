You are given a `m x n` matrix `grid` consisting of non-negative integers where `grid[row][col]` represents the number of objects the cell `(row, col)` can fit.

An object has the following properties: `name[i]`, `sensitive[i]` and `producer[i]`.

There are the following constrains:
- an object `i` with `sensitive[i]=1` and an object `j` with `producer[j]=1` can't lie next to each other in a row;

Print the matrix with maximal filling.