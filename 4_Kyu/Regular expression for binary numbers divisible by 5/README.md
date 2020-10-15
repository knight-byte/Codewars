Define a regular expression which tests if a given string representing a binary number is divisible by 5.

## Examples:

```
# 5 divisible by 5
PATTERN.match('101') == true

# 135 divisible by 5
PATTERN.match('10000111') == true

# 666 not divisible by 5
PATTERN.match('0000001010011010') == false
```

## Note:
This can be solved by creating a Finite State Machine that evaluates if a string representing a number in binary base is divisible by given number.
