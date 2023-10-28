map = [[0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0],
       [1, 1, 0, 1, 0],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0]]

combos = [[0], [1], [2],
          [0, 1], [0, 2], [1, 2], [1, 0], [2, 0], [2, 1],
          [0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

steps = ((1, 0), (0, 1), (-1, 0), (0, -1))
nodes = [[[0, 0], [0, 1], [0, 2]]]
finish = [[3, 0], [0, 4], [4, 2]]


def create_graph(map, combos, steps, nodes, finish):
    for pos in nodes:
        print('pos', pos)
        for combo in combos:
            agent = combo[0]
            for step in steps:
                node = []
                for i in range(len(pos)):
                    if i == agent:
                        if -1 < (pos[i][0] + step[0]) < 5 and -1 < (pos[i][1] + step[1]) < 5 and \
                                map[pos[i][0] + step[0]][pos[i][1] + step[1]] == 0 and \
                                [pos[i][0] + step[0], pos[i][1] + step[1]] not in pos:
                            node.append([pos[i][0] + step[0], pos[i][1] + step[1]])
                        else:
                            break
                    else:
                        node.append(pos[i])
                if len(combo) > 1:
                    agent2 = combo[1]
                    for step2 in steps:
                        node2 = []
                        for j in range(len(node)):
                            if j == agent2:
                                if -1 < (node[j][0] + step2[0]) < 5 and -1 < (node[j][1] + step2[1]) < 5 and \
                                        map[node[j][0] + step2[0]][node[j][1] + step2[1]] == 0 and \
                                        [node[j][0] + step2[0], node[j][1] + step2[1]] not in node:
                                    node2.append([node[j][0] + step2[0], node[j][1] + step2[1]])
                                else:
                                    break
                            else:
                                node2.append(node[j])
                        if len(combo) == 3:
                            agent3 = combo[2]
                            for step3 in steps:
                                node3 = []
                                for k in range(len(node2)):
                                    if k == agent3:
                                        if -1 < (node2[k][0] + step3[0]) < 5 and -1 < (node2[k][1] + step3[1]) < 5 and \
                                                map[node2[k][0] + step3[0]][node2[k][1] + step3[1]] == 0 and \
                                                [node2[k][0] + step3[0], node2[k][1] + step3[1]] not in node2:
                                            node3.append([node2[k][0] + step3[0], node2[k][1] + step3[1]])
                                        else:
                                            break
                                    else:
                                        node3.append(node2[k])
                                if len(node3) == 3 and node3 not in nodes:
                                    nodes.append(node3)
                                    if node3 == finish:
                                        return 0
                        else:
                            if len(node2) == 3 and node2 not in nodes:
                                nodes.append(node2)
                                if node2 == finish:
                                    return 0
                else:
                    if len(node) == 3 and node not in nodes:
                        nodes.append(node)
                        if node == finish:
                            return 0


create_graph(map, combos, steps, nodes, finish)
print("finish")
