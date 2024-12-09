import time
import random
import psutil
import paint

# 生成随机移动的函数
def generate_random_move(state):
    size = int(len(state) ** 0.5)
    blank_index = state.index(0)
    moves = []
    if blank_index % size > 0:
        moves.append(blank_index - 1)
    if blank_index % size < size - 1:
        moves.append(blank_index + 1)
    if blank_index >= size:
        moves.append(blank_index - size)
    if blank_index < len(state) - size:
        moves.append(blank_index + size)
    
    # 随机刷新当前状态
    random.shuffle(moves)
    return moves[0]

# 移动状态函数
def move(state, move_index):
    blank_index = state.index(0)
    new_state = state.copy()
    new_state[blank_index], new_state[move_index] = new_state[move_index], new_state[blank_index]
    return new_state

# 随机决策选择搜索
def random_search(initial_state, goal_state, max_steps):
    # 启动时间,内存计数变量
    start_time = time.time()
    start_memory = psutil.Process().memory_info().rss / 1024
    # 初始化当前状态,路径和已搜索结点数
    current_state = initial_state
    path = []
    nodes_searched = 0
    visited = set()
    # 创建画布
    root,canvas = paint.create_canvas("随即决策搜索")
    # 打印最终状态
    paint.draw_images(goal_state,"目标状态",canvas,0,root)
    # 遍历至匹配成功或达到最大步数
    for _ in range(max_steps+1):
        nodes_searched += 1
        if current_state == goal_state:
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / 1024
            print(f"随机决策选择搜索：")
            print(f"搜索节点数：{nodes_searched}")
            print(f"搜索时间：{end_time - start_time} 秒")
            print(f"内存占用：{end_memory - start_memory} KB")
            paint.draw_images(goal_state,"搜索成功",canvas,paint.height/2,root)
            root.destroy()
            return path
        
        visited.add(tuple(current_state))
        path.append(current_state)
        paint.draw_images(current_state,"正在随即检索",canvas,paint.height/2,root)
        # 随机移动白格
        move_index = generate_random_move(current_state)
        # 更新当前状态
        current_state = move(current_state, move_index)
        while tuple(current_state) in visited:
            move_index = generate_random_move(current_state)
            # 更新当前状态
            current_state = move(current_state, move_index)
    # 结束时间,内存计数变量
    end_time = time.time()
    end_memory = psutil.Process().memory_info().rss / 1024
    # 打印本次搜索的信息
    print(f"随机决策选择搜索：")
    print("本次搜索已达最大步数,搜索失败")
    print(f"搜索节点数：{nodes_searched}")
    print(f"搜索时间：{end_time - start_time} 秒")
    print(f"内存占用：{end_memory - start_memory} KB")
    root.destroy()
    root.mainloop()
    return path