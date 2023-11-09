def water_jug_dfs(jug1_capacity, jug2_capacity, target_capacity):
    def dfs(jug1, jug2, path):
        if jug1 == target_capacity or jug2 == target_capacity:
            print("Solution Found : ", path)
            return
 
        # Fill jug1
        if jug1 < jug1_capacity:
            new_jug1 = jug1_capacity
            new_jug2 = jug2
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                dfs(new_jug1, new_jug2, path+f"Fill Jug1\n")
 
        # Fill jug2
        if jug2 < jug2_capacity:
            new_jug1 = jug1
            new_jug2 = jug2_capacity
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                dfs(new_jug1, new_jug2, path+f"Fill Jug2\n")
 
        # Pour water from jug1 to jug2
        if jug1 > 0 and jug2 < jug2_capacity:
            pour_amount = min(jug1, jug2_capacity-jug2)
            new_jug1 = jug1 - pour_amount
            new_jug2 = jug2+pour_amount
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                dfs(new_jug1, new_jug2, path+f"Pour Jug1 into Jug2\n")
 
        # Pour water from jug2 to jug1
        if jug2 > 0 and jug1 < jug1_capacity:
            pour_amount = min(jug2, jug1_capacity-jug1)
            new_jug1 = jug1 + pour_amount
            new_jug2 = jug2 - pour_amount
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                dfs(new_jug1, new_jug2, path+f"Pour Jug2 into Jug1\n")
 
        # Empty jug1
        if jug1 > 0:
            new_jug1 = 0
            new_jug2 = jug2
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                dfs(new_jug1, new_jug2, path+f"Empty jug1\n")
 
        # Empty jug2
        if jug2 > 0:
            new_jug1 = jug1
            new_jug2 = 0
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                dfs(new_jug1, new_jug2, path+f"Empty jug2\n")
 
    visited = set()
    dfs(0, 0, "")
 
if __name__ == '__main__':
    jug1_capacity = 4
    jug2_capacity = 3
    target_capacity = 2
    
    water_jug_dfs(jug1_capacity, jug2_capacity, target_capacity)
 