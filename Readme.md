Consider a 2D array of integers.

Implement a function to calculate a sum of even numbers, accessible from given coordinates in the array. A cell is not accessible if its value is odd. A cell can be accessed through the other even cells, so that odd numbers can be considered  as walls in the labyrinth, where you can travel up/down/left/right. Diagonals are not passable. If your initial coordinate is odd the the result is zero.

```
def calc_sum(array2d, x, y):
    # where x is the row, y is the column(second array)
    ...
    return ...

test_array=[
[4,2,2,2,2],
[2,1,1,1,2],
[2,1,6,1,2],
[2,1,1,1,2],
[2,1,2,1,2],
[2,2,2,2,2]
]
```


