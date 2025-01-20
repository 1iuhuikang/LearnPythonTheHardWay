def start_game():
    print("欢迎来到冒险世界！")
    print("你站在一个神秘的森林入口，面前有两条路，左边是一条幽深的小路，右边是一条宽阔的大道。你会选择哪一条？")
    choice = input("输入 'left' 或 'right': ")
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("无效的选择，请输入 'left' 或 'right'。")
        start_game()


def left_path():
    print("你沿着幽深的小路前行，发现了一个神秘的洞穴。洞穴里闪烁着诡异的光芒，你要进入洞穴吗？")
    choice = input("输入 'enter' 或 'go back': ")
    if choice == "enter":
        cave()
    elif choice == "go back":
        start_game()
    else:
        print("无效的选择，请输入 'enter' 或 'go back'。")
        left_path()


def right_path():
    print("你踏上宽阔的大道，看到了一个古老的城堡。你想尝试进入城堡吗？")
    choice = input("输入 'enter' 或 'go back': ")
    if choice == "enter":
        castle()
    elif choice == "go back":
        start_game()
    else:
        print("无效的选择，请输入 'enter' 或 'go back'。")
        right_path()


def cave():
    print("进入洞穴后，你发现了一个宝箱，但它被一个魔法锁锁住了。你可以尝试破解魔法锁，或者寻找其他出路。")
    choice = input("输入 'crack' 或 'search': ")
    if choice == "crack":
        print("你试图破解魔法锁，但不小心触发了陷阱，你损失了一些生命值！")
        # 这里可以添加生命值管理机制
        start_game()
    elif choice == "search":
        print("你在洞穴的角落里找到了一把神秘的钥匙，它可能能打开宝箱。")
        print("现在你可以用钥匙打开宝箱，或者继续寻找其他线索。")
        choice = input("输入 'open' 或 'continue': ")
        if choice == "open":
            print("你打开了宝箱，获得了一件强大的武器！")
            # 这里可以添加物品收集机制
            start_game()
        elif choice == "continue":
            print("你继续寻找线索，发现了一条通往地下河的通道。")
            underground_river()
        else:
            print("无效的选择，请输入 'open' 或 'continue'。")
            cave()
    else:
        print("无效的选择，请输入 'crack' 或 'search'。")
        cave()


def castle():
    print("当你接近城堡时，你听到了可怕的咆哮声。你是要勇敢地进入城堡，还是转身逃跑？")
    choice = input("输入 'enter' 或 'run': ")
    if choice == "enter":
        print("你进入城堡，发现了一个凶猛的巨龙！你可以选择战斗或试图与它交谈。")
        choice = input("输入 'fight' 或 'talk': ")
        if choice == "fight":
            print("你与巨龙展开了激烈的战斗，结果会如何呢？")
            # 这里可以添加战斗机制
            start_game()
        elif choice == "talk":
            print("你试图与巨龙交谈，巨龙似乎对你的勇气表示赞赏，它给了你一个神秘的任务。")
            print("你会接受巨龙的任务，还是拒绝它？")
            choice = input("输入 'accept' 或 'refuse': ")
            if choice == "accept":
                print("你接受了任务，踏上了新的冒险之旅。")
                # 这里可以添加任务机制
                start_game()
            elif choice == "refuse":
                print("巨龙对你的拒绝感到愤怒，你不得不逃离城堡。")
                start_game()
            else:
                print("无效的选择，请输入 'accept' 或 'refuse'。")
                castle()
        else:
            print("无效的选择，请输入 'fight' 或 'talk'。")
            castle()
    elif choice == "run":
        print("你转身逃跑，却不小心迷失了方向。")
        print("你会继续寻找出路，还是等待救援？")
        choice = input("输入 'search' 或 'wait': ")
        if choice == "search":
            print("你开始寻找出路，发现了一个神秘的路标。")
            # 这里可以添加解谜机制
            start_game()
        elif choice == "wait":
            print("你决定等待救援，但时间流逝，你开始感到饥饿。")
            # 这里可以添加饥饿度机制
            start_game()
        else:
            print("无效的选择，请输入 'search' 或 'wait'。")
            castle()
    else:
        print("无效的选择，请输入 'enter' 或 'run'。")
        castle()


def underground_river():
    print("你沿着地下河前行，河水冰冷刺骨。你看到河对岸有一个发光的物体，你会尝试过河吗？")
    choice = input("输入 'cross' 或 'go back': ")
    if choice == "cross":
        print("你试图过河，但水流湍急，你差点被冲走。你是继续前进，还是返回洞穴？")
        choice = input("输入 'continue' 或 'return': ")
        if choice == "continue":
            print("你成功到达对岸，发现了一个神秘的传送门。")
            # 这里可以添加传送门机制
            start_game()
        elif choice == "return":
            cave()
        else:
            print("无效的选择，请输入 'continue' 或 'return'。")
            underground_river()
    elif choice == "go back":
        cave()
    else:
        print("无效的选择，请输入 'cross' 或 'go back'。")
        underground_river()


start_game()