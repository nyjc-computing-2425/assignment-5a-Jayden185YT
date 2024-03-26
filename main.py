def to_hms(seconds: int) -> list:
  """
  Converts seconds to hours, minutes, and seconds, and returns it as a list.

  Parameters
  ---------
  seconds: int
      the seconds to be calculated

  Returns
  ---------
  list
      a list of integers representing hours, minutes, seconds

  Example:
  >>> to_hms(10)
  [0, 0, 10]
  >>> to_hms(61)
  [0, 1, 1]
  >>> to_hms(7199)
  [1, 59, 59]
  """
  # Type your code below
  result = []
  if not isinstance(seconds, int):
    print("Unsupported input type.")
    return result
  result = [0,0,0]
  hours, minutes = divmod(seconds, 3600)
  result[0] = hours
  seconds %= 60
  minutes //= 60
  result[1] = minutes
  result[2] = seconds
  return result

