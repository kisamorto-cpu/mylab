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

