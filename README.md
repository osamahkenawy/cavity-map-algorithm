# Cavity Map

This Python script solves the "Cavity Map" problem, which involves finding cavities in a grid of numbers and replacing them with the character 'X'. A cavity is a cell in the grid that is not on the border and has a greater value than all its directly adjacent cells (up, down, left, right).

## Problem Description

Given a square grid of digits, identify the cells that are cavities and replace them with 'X'. A cell is a cavity if it is greater than its neighboring cells (above, below, left, and right).

### Input

- The first line contains an integer `n`, the size of the grid.
- Each of the next `n` lines contains a string of `n` digits.

### Output

- The output should be the modified grid with cavities replaced by 'X'.

## Implementation

The `cavityMap` function iterates over each cell in the grid, ignoring the border cells. It checks if the current cell is greater than its neighboring cells. If it is, the cell is replaced with 'X'. The function returns the modified grid.

### Functions

1. **cavityMap(grid)**:
   - Takes the grid as input.
   - Loops through each cell, checks for cavities, and replaces them with 'X' if conditions are met.
   - Returns the modified grid.