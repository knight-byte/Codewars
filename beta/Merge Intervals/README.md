Write a function called merge_intervals that accepts an array of intervals, and returns an array with all overlapping intervals merged into one. The resulting array should be ordered by the first value of interval.

## Interval
The intervals are represented as a pair of integers, the first value of the interval will always be less than the second value.

## Limits
- -10^9<=F <S <=10^9, Where F and S are first and second value of intervals.
- 1<=N <=3200, Where N is the size of intervals array

## Example
````
merge_intervals( [
   `1, 2),
   (11, 15),
   (6, 10)  
] ) # => [(1, 2), (6, 10), (11, 15)]

merge_intervals( [
   (1, 5),
   (6, 10),
   (3, 7)  
] ) # => [(1, 10)]

merge_intervals( [
   (1, 5),
   (1, 5)
] ) # => [(1, 5)]
```
