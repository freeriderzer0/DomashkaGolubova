a = [0, 0]
b = [1, 1]
c = [2, 2]
comb = [[a], [b], [c],
        [a, b], [a, c], [b, c],
        [a, b, c]]
steps = ((1, 0), (0, 1), (-1, 0), (0, -1))
nodes = [[[0, 0],[1, 1],[2, 2]]]
while a!=(3, 3) and b!=(3, 3) and c!=(3, 3):
    for co in comb:
        print("comb:", co)
        for agent in co:
            print("agent", agent)
            for s in steps:
                agent[0] += s[0]
                agent[1] += s[1]
                print(a,b,c)
            diff = [x for x in co if x not in [agent]]
            for agent2 in diff:
                print("agent2", agent2)
                for s in steps:
                    agent2[0] += s[0]
                    agent2[1] += s[1]
                    print(a, b, c)
                diff2 = [x for x in diff if x not in [agent2]]
                for agent3 in diff2:
                    print("agent3", agent3)
                    for s in steps:
                        agent3[0] += s[0]
                        agent3[1] += s[1]
                        print(a, b, c)
