# 深度搜索优先算法
import puzzle_dfs
# 宽度优先算法
import puzzle_bfs
# 启发式搜索曼哈顿算法
import puzzle_heuristic_manhattan
# 启发式搜索错位子算法
import puzzle_heuristic_misplaced
# 随机移动算法
import puzzle_random
# 导入绘图
import paint

def puzzle_question(initial_state, goal_state,input_steps):
    # 深度优先搜索
    path_dfs = puzzle_dfs.dfs(initial_state, goal_state,input_steps)
    # 宽度优先搜索
    path_bfs = puzzle_bfs.bfs(initial_state, goal_state,input_steps)
    # 曼哈顿距离启发式搜索
    path_heuristic_manhattan = puzzle_heuristic_manhattan.heuristic_search_manhattan(initial_state, goal_state,input_steps)
    # 错位棋子数启发式搜索
    path_heuristic_misplaced = puzzle_heuristic_misplaced.heuristic_search_misplaced(initial_state, goal_state,input_steps)
    # 随机决策选择搜索
    path_random = puzzle_random.random_search(initial_state, goal_state,input_steps)
    
    #记录最长搜索链
    longest_search_chain = max(len(path_dfs), len(path_bfs), len(path_heuristic_manhattan),
                                len(path_heuristic_misplaced), len(path_random))
    print(f"最长搜索链长度：{longest_search_chain}")

if __name__ == "__main__":
    # 动态演示
    input_dc = input("是否需要动画演示:是[1]否[默认]")
    if input_dc == "1":
        paint.flag = True
        # 演示时间
        input_dc_t = input("输入动画演示间隔时间(默认0.2):")
        if input_dc_t:
            paint.show_time = float(input_dc_t)
    # 接收输入的字符串
    input_str = input("请输入[0-9]或[0-16]的整数:")
    # 设置最大步数
    input_steps = input("请输入最大步长(默认100):")
    if input_steps:
        input_steps = int(input_steps)
    else:
        input_steps = 100

    while True:
        # 以空格为分界符,得到输入字符数组
        input_arr = input_str.split()
        # 构建初始状态数组
        initial_state = []
        # 循环遍历字符数组,转字符为整型添加至状态数组
        for num in input_arr:
            initial_state.append(int(num))

        if len(initial_state) !=9 and len(initial_state) != 16:
            input_str = input("请输入合法的9个或16个整数:")
            continue
        else:
            if len(initial_state)==9:
                goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
                print("以下是8数码问题的求解:")
            else:
                goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
                print("以下是15数码问题的求解:")
            puzzle_question(initial_state,goal_state,input_steps)
            break