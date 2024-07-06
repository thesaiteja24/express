def water_jug_dfs(jug1_capacity, jug2_capacity, target):
  """
  Solves the water jug problem using Depth-First Search (DFS).

  Args:
      jug1_capacity: Capacity of the first jug.
      jug2_capacity: Capacity of the second jug.
      target: Target amount of water to reach.

  Returns:
      A list of states representing the steps to reach the target, 
      or None if not possible.
  """
  visited = set()  # Set to store visited states

  def dfs(jug1, jug2):
    state = (jug1, jug2)
    if state in visited:
      return

    visited.add(state)

    if jug1 == target:
      return [state]

    # Fill jug1
    result = dfs(jug1_capacity, jug2)
    if result:
      result.append(state)
      return result

    # Fill jug2
    result = dfs(jug1, jug2_capacity)
    if result:
      result.append(state)
      return result

    # Empty jug1
    result = dfs(0, jug2)
    if result:
      result.append(state)
      return result

    # Empty jug2
    result = dfs(jug1, 0)
    if result:
      result.append(state)
      return result

    # Transfer water between jugs
    # Transfer from jug1 to jug2 (up to jug2's capacity)
    amount_to_transfer = min(jug1, jug2_capacity - jug2)
    result = dfs(jug1 - amount_to_transfer, jug2 + amount_to_transfer)
    if result:
      result.append(state)
      return result

    # Transfer from jug2 to jug1 (up to jug1's capacity)
    amount_to_transfer = min(jug2, jug1_capacity - jug1)
    result = dfs(jug1 + amount_to_transfer, jug2 - amount_to_transfer)
    if result:
      result.append(state)
      return result

    return None

  # Start DFS from initial state (0 water in both jugs)
  result = dfs(0, 0)
  if result:
    # Reverse the list to get the steps in the correct order
    return result[::-1]
  else:
    return None

# Example usage
jug1_capacity = int(input("Enter capacity for jug 1:"))
jug2_capacity = int(input("Enter capacity for jug 2:"))
target = int(input("Enter goal:"))

solution = water_jug_dfs(jug1_capacity, jug2_capacity, target)

if solution:
  print("Steps to reach", target, "liters of water:")
  for state in solution:
    print(state)
else:
  print("It is not possible to reach", target, "liters of water with these jug capacities.")
