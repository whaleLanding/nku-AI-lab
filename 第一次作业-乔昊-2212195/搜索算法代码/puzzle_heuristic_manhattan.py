import time
import psutil
import paint

# 计算曼哈顿距离启发式函数
def manhattan_distance(state, goal_state):
    # 初始化曼哈顿距离
    distance = 0
    # 初始化格子宽度
    size = int(len(state) ** 0.5)
    # 计算各个格子距目标位置的曼哈顿距离
    for i in range(len(state)):
        if state[i]!= 0:
            goal_pos = goal_state.index(state[i])
            current_row, current_col = i // size, i % size
            goal_row, goal_col = goal_pos // size, goal_pos % size
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

# 移动状态函数
def move(state, move_index):
    blank_index = state.index(0)
    new_state = state.copy()
    new_state[blank_index], new_state[move_index] = new_state[move_index], new_state[blank_index]
    return new_state

# 启发式搜索（使用曼哈顿距离启发式）
def heuristic_search_manhattan(initial_state, goal_state, max_steps):
    start_time = time.time()
    start_memory = psutil.Process().memory_info().rss / 1024
    # 创建画布
    root,canvas = paint.create_canvas("启发式曼哈顿距离算法")
    # 打印最终状态
    paint.draw_images(goal_state,"目标状态",canvas,0,root)

    visited = set()
    priority_queue = [(manhattan_distance(initial_state, goal_state), initial_state, [])]
    nodes_searched = 0

    while priority_queue and nodes_searched <= max_steps:
        _, current_state, path = priority_queue.pop(0)
        nodes_searched += 1

        if current_state == goal_state:
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / 1024
            print(f"曼哈顿距离启发式搜索：")
            print(f"搜索节点数：{nodes_searched}")
            print(f"搜索时间：{end_time - start_time} 秒")
            print(f"内存占用：{end_memory - start_memory} KB")
            paint.draw_images(goal_state,"搜索成功",canvas,paint.height/2,root)
            root.destroy()
            return path

        if tuple(current_state) not in visited:
            visited.add(tuple(current_state))
            size = int(len(current_state) ** 0.5)
            blank_index = current_state.index(0)

            if blank_index % size > 0:
                priority_queue.append((manhattan_distance(move(current_state, blank_index - 1), goal_state),
                                       move(current_state, blank_index - 1), path + [current_state]))
            if blank_index % size < size - 1:
                priority_queue.append((manhattan_distance(move(current_state, blank_index + 1), goal_state),
                                       move(current_state, blank_index + 1), path + [current_state]))
            if blank_index >= size:
                priority_queue.append((manhattan_distance(move(current_state, blank_index - size), goal_state),
                                       move(current_state, blank_index - size), path + [current_state]))
            if blank_index < len(current_state) - size:
                priority_queue.append((manhattan_distance(move(current_state, blank_index + size), goal_state),
                                       move(current_state, blank_index + size), path + [current_state]))
            # 将曼哈顿距离最小的状态放置队列首部
            priority_queue.sort(key=lambda x: x[0])
          
        paint.draw_images(current_state,"检索曼哈顿距离最小状态",canvas,paint.height/2,root)
    
    # 结束时间,内存计数变量
    end_time = time.time()
    end_memory = psutil.Process().memory_info().rss / 1024
    print(f"曼哈顿距离启发式搜索：")
    print("本次搜索已达最大步数,搜索失败")
    print(f"搜索节点数：{nodes_searched}")
    print(f"搜索时间：{end_time - start_time} 秒")
    print(f"内存占用：{end_memory - start_memory} KB")
    root.destroy()
    root.mainloop()
    return path