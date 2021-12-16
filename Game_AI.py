import heapq

def Manhattan(state, sol):

    total = 0
    coord = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    count = 0
    for first, second in zip(state, sol):
        if first == 0:
            count += 1
            continue
        else:
            if first == second:
                count += 1
                continue
            else:
                counter = 0
                for j in sol:
                    if j == first:
                        break
                    counter += 1
                total += abs((coord[counter][0]) - (coord[count])[0]) + abs((coord[counter][1]) - (coord[count])[1])
                count += 1

    return total

def print_succ(state):

    succ_list = get_succ(state)
    sol = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    for j in succ_list:
        heur = Manhattan(j, sol)
        print(j, " h=", heur, sep='')
    return

def get_succ(state):

    index_0 = 0
    for i in state:
        if i == 0:
            break
        index_0 += 1
    row1, row2, row3 = [state[0], state[1], state[2]], [state[3], state[4], state[5]], [state[6], state[7], state[8]]
    states = []
    if index_0 == 0:
        row1 = [state[1], state[0], state[2]]
        states.append(list(row1+row2+row3))
        row1 = [state[3], state[1], state[2]]
        row2 = [state[0], state[4], state[5]]
        states.append(list(row1+row2+row3))
        return sorted(states)
    if index_0 == 6:
        row3 = [state[7], state[6], state[8]]
        states.append(list(row1+row2+row3))
        row3 = [state[3], state[7], state[8]]
        row2 = [state[6], state[4], state[5]]
        states.append(list(row1+row2+row3))
        return sorted(states)
    if index_0 == 2:
        row1 = [state[0], state[2], state[1]]
        states.append(list(row1+row2+row3))
        row1 = [state[0], state[1], state[5]]
        row2 = [state[3], state[4], state[2]]
        states.append(list(row1+row2+row3))
        return states
    if index_0 == 8:
        row3 = [state[6], state[8], state[7]]
        states.append(list(row1+row2+row3))
        row3 = [state[6], state[7], state[5]]
        row2 = [state[3], state[4], state[8]]
        states.append(list(row1+row2+row3))
        return sorted(states)
    if index_0 == 1:
        row1 = [state[1], state[0], state[2]]
        states.append(list(row1+row2+row3))
        row1 = [state[0], state[2], state[1]]
        states.append(list(row1 + row2 + row3))
        row1 = [state[0], state[4], state[2]]
        row2 = [state[3], state[1], state[5]]
        states.append(list(row1+row2+row3))
        return sorted(states)
    if index_0 == 7:
        row3 = [state[7], state[6], state[8]]
        states.append(list(row1+row2+row3))
        row3 = [state[6], state[8], state[7]]
        states.append(list(row1+row2+row3))
        row2 = [state[3], state[7], state[5]]
        row3 = [state[6], state[4], state[8]]
        states.append(list(row1+row2+row3))
        return sorted(states)
    if index_0 == 3:
        row2 = [state[4], state[3], state[5]]
        states.append(list(row1+row2+row3))
        row1 = [state[3], state[1], state[2]]
        row2 = [state[0], state[4], state[5]]
        states.append(list(row1+row2+row3))
        row1 = [state[0], state[1], state[2]]
        row2 = [state[6], state[4], state[5]]
        row3 = [state[3], state[7], state[8]]
        states.append(list(row1+row2+row3))
        return sorted(states)
    if index_0 == 5:
        row2 = [state[3], state[5], state[4]]
        states.append(list(row1+row2+row3))
        row1 = [state[0], state[1], state[5]]
        row2 = [state[3], state[4], state[2]]
        states.append(list(row1+row2+row3))
        row1 = [state[0], state[1], state[2]]
        row2 = [state[3], state[4], state[8]]
        row3 = [state[6], state[7], state[5]]
        states.append(list(row1+row2+row3))
        return sorted(states)
    if index_0 == 4:
        row2 = [state[4], state[3], state[5]]
        states.append(list(row1+row2+row3))
        row2 = [state[3], state[5], state[4]]
        states.append(list(row1+row2+row3))
        row1 = [state[0], state[4], state[2]]
        row2 = [state[3], state[1], state[5]]
        states.append(list(row1+row2+row3))
        row1 = [state[0], state[1], state[2]]
        row2 = [state[3], state[7], state[5]]
        row3 = [state[6], state[4], state[8]]
        states.append(list(row1+row2+row3))
        return sorted(states)

def solve(state):

    sol = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    path_list = []
    visited = []
    pq = []
    heapq.heappush(pq, (0+Manhattan(state, sol), state, (0, Manhattan(state,sol), len(visited)-1)))
    while len(pq) != 0:
        curr_state = heapq.heappop(pq)
        visited.append(curr_state)
        if curr_state[1] == sol: #if solution, return
            index = curr_state[2][2]
            while index != -1:
                parent = visited[index]
                path_list.append(parent)
                index = parent[2][2]
            count = 0
            for each in path_list[::-1]:
                print(each[1], " h=", Manhattan(each[1], sol), " moves: ", count, sep='')
                count += 1
            print(sol, " h=", 0, " moves: ", count, sep='')
            return
        states = get_succ(curr_state[1]) #get successors
        for s in states: #loop through possible next states
            is_visited = False
            if len(visited) == 0:
                is_visited = True
            for v in visited: #if visited, skip
                if s == v[1]:
                    is_visited = True
                    break
            if not is_visited:
                heapq.heappush(pq, ((curr_state[2][0]+1)+Manhattan(s, sol), s, ((curr_state[2][0]+1), Manhattan(s,sol), len(visited)-1)))

if __name__ == '__main__':

    print_succ([1,2,3,4,5,0,6,7,8])
    print("\n")
    print_succ([8,7,6,5,4,3,2,1,0])
    print("\n")
    state = [4,3,8,5,1,6,7,2,0]
    solve(state)
    print("\n")
    state = [1,2,3,4,5,6,7,0,8]
    solve(state)

