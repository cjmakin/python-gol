## Conway's Game of life using PyGame

Rules:
- Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
- Any live cell with more than three live neighbours dies, as if by overcrowding.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any dead cell with exactly three live neighbours becomes a live cell.
- Each cell's neighborhood is the 8 cells immediately around it (Moore Neighborhood).

Goals: 
- Use a toroidal array. 
- Allow user to select the number of generations and starting conditions (by point and click)
- Allow user to choose from a selection of field sizes.
