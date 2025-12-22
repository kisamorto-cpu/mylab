def is_fully_connected(V, R, P):
    """
    Определяет, является ли сеть полносвязной.
    
    Args:
        V (int): Количество вершин
        R (int): Количество рёбер
        P (list): Список кортежей (i, j) - связи между вершинами
    
    Returns:
        bool: True если сеть полносвязная, иначе False
    """
    # В полносвязном графе должно быть V*(V-1)/2 рёбер
    max_edges = V * (V - 1) // 2
    
    if R != max_edges:
        return False
    
    # Проверяем, что все возможные пары вершин соединены
    # Создаём множество всех пар (упорядоченных для избежания дубликатов)
    existing_pairs = set()
    
    for i, j in P:
        # Сортируем вершины для избежания дубликатов (1,2) и (2,1)
        if i < j:
            existing_pairs.add((i, j))
        else:
            existing_pairs.add((j, i))
    
    # Проверяем, что все возможные пары присутствуют
    for i in range(1, V + 1):
        for j in range(i + 1, V + 1):
            if (i, j) not in existing_pairs:
                return False
    
    return True


def determine_topology(V, R, P):
    """
    Определяет тип топологии сети для неполносвязных сетей.

    Args:
        V (int): Количество вершин
        R (int): Количество рёбер
        P (list): Список кортежей (i, j) - связи между вершинами

    Returns:
        str: "шина", "кольцо", "звезда" или "неизвестная топология"
    """
    # Сначала проверяем, не является ли сеть полносвязной
    if is_fully_connected(V, R, P):
        return "полносвязная"

    # Строим список смежности для графа
    adjacency = {i: [] for i in range(1, V + 1)}

    for i, j in P:
        adjacency[i].append(j)
        adjacency[j].append(i)

    # Вычисляем степени вершин
    degrees = [len(adjacency[i]) for i in range(1, V + 1)]
    max_degree = max(degrees)
    min_degree = min(degrees)

    # Проверка на звезду:
    # Звезда: одна вершина имеет степень V-1, остальные имеют степень 1
    # Рёбер должно быть V-1
    if R == V - 1:
        if max_degree == V - 1 and degrees.count(1) == V - 1:
            return "звезда"

    # Проверка на кольцо:
    # Кольцо: все вершины имеют степень 2, рёбер V
    if R == V:
        if all(degree == 2 for degree in degrees):
            return "кольцо"

    # Проверка на шину:
    # Шина: 2 вершины имеют степень 1 (концы), остальные имеют степень 2
    # Рёбер должно быть V-1
    if R == V - 1:
        # Считаем количество вершин каждой степени
        degree_count = {1: 0, 2: 0}
        for degree in degrees:
            if degree == 1:
                degree_count[1] += 1
            elif degree == 2:
                degree_count[2] += 1

        # Для шины должно быть 2 вершины степени 1 и V-2 вершин степени 2
        if degree_count[1] == 2 and degree_count[2] == V - 2:
            return "шина"

    # Если ни один из типов не подошёл
    return "неизвестная топология"