combos = [[0], [1], [2],
          [0, 1], [0, 2], [1, 2],
          [0, 1, 2]]
steps = ((1, 0), (0, 1), (-1, 0), (0, -1))
nodes = [[[0, 0], [1, 1], [2, 2]]]
for pos in nodes:
    print('pos', pos)
    for combo in combos:
        print('combo', combo)
        node = []
        for agent in combo:
            for step in steps:
                for i in range(3):
                    if i == agent:
                        node.append([pos[i][0] + step[0], pos[i][1] + step[1]])
                    else:
                        node.append(pos[i])



        agent = combo[0]
        for step in steps:
            node = []
            for i in range(len(pos)):
                if i == agent:
                    node.append([pos[i][0] + step[0], pos[i][1] + step[1]])
                else:
                    node.append(pos[i])
            if len(combo) > 1:
                agent2 = combo[1]
                for step2 in steps:
                    node2 = []
                    for j in range(len(node)):
                        if j == agent2:
                            node2.append([node[j][0] + step2[0], node[j][1] + step2[1]])
                        else:
                            node2.append(node[j])
                    if len(combo) == 3:
                        agent3 = combo[2]
                        for step3 in steps:
                            node3 = []
                            for k in range(len(node2)):
                                if k == agent3:
                                    node3.append([node2[k][0] + step3[0], node2[k][1] + step3[1]])
                                else:
                                    node3.append(node2[k])
                            print("node3", node3)
                            nodes.append(node3)
                    else:
                        print("node2", node2)
                        nodes.append(node2)
            else:
                print("node", node)
                nodes.append(node)
print("finish")