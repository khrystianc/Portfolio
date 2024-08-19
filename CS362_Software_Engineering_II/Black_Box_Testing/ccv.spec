#length
length:
  0-9.          [error]
  10-14.        [error]
  15.           [property AmEx]
  16.           [property Visa, MasterCard]
  17-18.        [error]
  19-inf.       [error]
#prefix
prefix:
  4.          [length 16, property Visa]
  34.         [length 15, property AmEx]
  37.         [length 15, property AmEx]
  51-55.      [length 16, property MasterCard]
  2221-2720.  [length 16, property MasterCard]
#checksum
checksum:
  luhn's algorithm.