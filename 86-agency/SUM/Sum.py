def find_sum_pair(arr, x):
  """
  This function checks if there exist two elements in the array that add up to the given sum 'x' using a hash table.

  Args:
      arr: The input array of numbers.
      x: The target sum to find.

  Returns:
      True if a pair is found, False otherwise.
  """
  # Initialize a hash table to store seen numbers.
  hash_table = {}
  for i in range(len(arr)):
    # Calculate the complement.
    complement = x - arr[i]

    # Check if the complement exists in the hash table.
    if complement in hash_table:
      return True
    else:
      # Add the current element to the hash table.
      hash_table[arr[i]] = 1
  
  # If we reach here, no pair is found.
  return False

# Example usage
arr = [1, -2, 1, 0, 5]
x = 0
if find_sum_pair(arr, x):
  print("Yes")
else:
  print("No")
