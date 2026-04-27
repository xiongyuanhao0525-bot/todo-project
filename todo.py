tasks = []

while True:
    print("\n==== TODO LIST ====")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

    print("\n1. 添加任务")
    print("2. 删除任务")
    print("3. 退出")

    choice = input("请选择: ")

    if choice == "1":
        task = input("输入任务内容: ")
        tasks.append(task)

    elif choice == "2":
        num = int(input("输入要删除的任务编号: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)

    elif choice == "3":
        break