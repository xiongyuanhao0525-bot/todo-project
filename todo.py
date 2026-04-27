import json

# 读取文件
tasks = []

try:
    with open("tasks.json", "r", encoding="utf-8") as f:
        tasks = json.load(f)
except (FileNotFoundError,json.JSONDecodeError):
    tasks=[]


while True:
    print("\n==== TODO LIST ====")
    print("\n1. 所有任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 标记任务")
    print("5. 输出已完成任务")
    print("6. 删掉完成的任务")    
    print("10. 退出")


    choice = input("请选择: ")

    if choice == "1":
        for i, t in enumerate(tasks):
            status="[x]" if t.get("done",False) else "[ ]"
            print(f"{status} {i + 1}. {t['task']}")
        

    elif choice == "2":
        task = input("输入任务内容: ")
        tasks.append({
            "task":task,
            "done":False
        })
    elif choice == "3":
        num = int(input("输入要删除的任务编号: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
    elif choice=='4':
        num=int(input("请输入要切换状态的任务编号："))
        if 0<num<=len(tasks):
            tasks[num-1]["done"]=not tasks[num-1]["done"]
    elif choice=='5':
        for i,t in enumerate(tasks):
            if t.get("done",False):
                print(f"{i+1}. [x] {t['task']}")
    elif choice=='6':
        tasks=[t for t in tasks if not t.get("done",False)]


    elif choice=="10":
        break


# 👉 退出前保存文件
with open("tasks.json", "w", encoding="utf-8") as f:
    json.dump(tasks,f,ensure_ascii=False,indent=2)