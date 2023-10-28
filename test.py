# карта всей хуйни, где 1 это препятствие
map = [[0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0],
       [1, 1, 0, 1, 0],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0]]

# все возможные варианты комбинации агентов
combos = [[0], [1], [2],
          [0, 1], [0, 2], [1, 2], [1, 0], [2, 0], [2, 1],
          [0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

# все возможные движения для агента
steps = ((1, 0), (0, 1), (-1, 0), (0, -1))

# список всех нод, куда уже добавлена стартовая нода
nodes = [[[0, 0], [0, 1], [0, 2]]]

# конечная нода
finish = [[3, 0], [0, 4], [4, 2]]


def create_graph(map, combos, steps, nodes, finish):
    for pos in nodes: # перебираем все ноды, каждая нода - конф. всех агентов
        print('pos', pos)
        for combo in combos: # перебираем все комбинации движений
            agent = combo[0] # выбираем первым агентом первого робота из комбинации
            for step in steps: # перебираем все движения
                node = [] # создаём новую ноду
                for i in range(len(pos)): # проходим по всем элементам родительской ноды
                    if i == agent: # если элемент соответствует выбранному агенту
                        # если итоговое полож. агента попадает в свободную ячейку карты и не находится в род. ноде
                        # добавляем к ноде элемент
                        if -1 < (pos[i][0] + step[0]) < 5 and -1 < (pos[i][1] + step[1]) < 5 and \
                                map[pos[i][0] + step[0]][pos[i][1] + step[1]] == 0 and \
                                [pos[i][0] + step[0], pos[i][1] + step[1]] not in pos:
                            node.append([pos[i][0] + step[0], pos[i][1] + step[1]])
                        else: # в противном случае прерываем цикл и выбираем другое движение
                            break
                    else: # если агент не двигается оставляем координаты без изменений
                        node.append(pos[i])
                if len(combo) > 1: # если двигаются несколько роботов, продолжаем
                    agent2 = combo[1] # выбираем вторым агентом второго робота
                    for step2 in steps: # перебираем все движения для него
                        node2 = [] # создаём новую ноду
                        for j in range(len(node)): # так же проходимся по всем элементам прошлой ноды и при
                            # необходимости меняем их
                            if j == agent2:
                                if -1 < (node[j][0] + step2[0]) < 5 and -1 < (node[j][1] + step2[1]) < 5 and \
                                        map[node[j][0] + step2[0]][node[j][1] + step2[1]] == 0 and \
                                        [node[j][0] + step2[0], node[j][1] + step2[1]] not in node:
                                    node2.append([node[j][0] + step2[0], node[j][1] + step2[1]])
                                else:
                                    break
                            else:
                                node2.append(node[j])
                        if len(combo) == 3: # если у нас двигаются все агенты, продолжаем по той же логике
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
                                if len(node3) == 3 and node3 not in nodes: # если ноды ещё нет в графе, добавляем её
                                    nodes.append(node3)
                                    if node3 == finish: # если нода конечная - стопаем прогу
                                        return 0
                        else:
                            if len(node2) == 3 and node2 not in nodes: # если ноды ещё нет в графе, добавляем её
                                nodes.append(node2)
                                if node2 == finish: # если нода конечная - стопаем прогу
                                    return 0
                else:
                    if len(node) == 3 and node not in nodes: # если ноды ещё нет в графе, добавляем её
                        nodes.append(node)
                        if node == finish: # если нода конечная - стопаем прогу
                            return 0


create_graph(map, combos, steps, nodes, finish) # вызываем функцию, где map - карта, combos - все возможные
# комбинации агентов, steps - все возможные движения, nodes - список нод со стартовой нодой, finish - конечная нода
print("finish") # вы великолепны!
