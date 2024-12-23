import json
import os
from datetime import datetime
import readchar

FILE_NAME = "reading_records.json"

# 自动加载书籍记录
def load_records():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# 自动保存书籍记录
def save_records(records):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4, ensure_ascii=False)

# 显示书籍记录
def view_records(records, filter_status=None):
    filtered = records if filter_status is None else [r for r in records if r['status'] == filter_status]
    if not filtered:
        print("\n当前没有符合条件的书籍记录。\n")
    else:
        print("\n书籍记录：")
        for idx, record in enumerate(filtered, start=1):
            start_time = record.get('start_time', '未记录')
            finish_time = record.get('finish_time', '未完成')
            english_title = record.get('english_title', '无英文名')
            print(f"{idx}.  中文名: {record['title']}")
            print(f"    英文名: {english_title}")
            print(f"    作者: {record['author']}, 状态: {record['status']}")
            print(f"    开始时间: {start_time}, 完成时间: {finish_time}\n")

# 添加书籍记录
def add_record(records):
    title = input("请输入书的中文名: ").strip()
    english_title = input("请输入书的英文名（如果没有可留空）: ").strip()
    author = input("请输入作者: ").strip()
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    records.append({
        "title": title,
        "english_title": english_title if english_title else "无英文名",
        "author": author,
        "status": "未读",
        "start_time": start_time,
        "finish_time": None
    })
    print(f"已添加书籍: {title}，开始阅读时间: {start_time}\n")

# 更新书籍状态
def update_status(records):
    view_records(records)
    try:
        index = int(input("请输入要修改状态的书籍序号: ")) - 1
        if 0 <= index < len(records):
            new_status = input("请输入新的状态（未读/正在阅读/已读）: ").strip()
            records[index]['status'] = new_status
            if new_status == "已读":
                records[index]['finish_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"已完成阅读: {records[index]['title']}，完成时间: {records[index]['finish_time']}\n")
            else:
                records[index]['finish_time'] = None
                print(f"状态已更新为: {new_status}\n")
        else:
            print("无效的序号！\n")
    except ValueError:
        print("请输入有效的数字！\n")

# 搜索书籍记录
def search_records(records):
    keyword = input("请输入书名或作者关键词: ").strip()
    results = [r for r in records if keyword.lower() in r['title'].lower() or
               keyword.lower() in r.get('english_title', '').lower() or
               keyword.lower() in r['author'].lower()]
    if results:
        print("\n搜索结果：")
        for idx, record in enumerate(results, start=1):
            start_time = record.get('start_time', '未记录')
            finish_time = record.get('finish_time', '未完成')
            english_title = record.get('english_title', '无英文名')
            print(f"{idx}. 中文名: {record['title']}")
            print(f"    英文名: {english_title}")
            print(f"    作者: {record['author']}, 状态: {record['status']}")
            print(f"    开始时间: {start_time}, 完成时间: {finish_time}\n")
    else:
        print("\n未找到匹配的书籍。\n")

# 主菜单选项
def main_menu():
    return [
        "查看所有书籍",
        "添加书籍记录",
        "更新书籍状态",
        "搜索书籍",
        "退出程序"
    ]

# 使用方向键导航菜单
def navigate_menu(menu):
    selected = 0
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("===== 读书记录管理系统 =====")
        for i, option in enumerate(menu):
            if i == selected:
                print(f"> {option}")  # 高亮当前选项
            else:
                print(f"  {option}")
        print("\n使用 ↑ 和 ↓ 选择，回车确认。\n")

        key = readchar.readkey()
        if key == readchar.key.UP:  # 上方向键
            selected = (selected - 1) % len(menu)
        elif key == readchar.key.DOWN:  # 下方向键
            selected = (selected + 1) % len(menu)
        elif key == readchar.key.ENTER:  # 回车键
            return selected

# 主程序
def main():
    records = load_records()
    menu = main_menu()

    while True:
        choice = navigate_menu(menu)

        if choice == 0:  # 查看所有书籍
            view_records(records)
        elif choice == 1:  # 添加书籍记录
            add_record(records)
        elif choice == 2:  # 更新书籍状态
            update_status(records)
        elif choice == 3:  # 搜索书籍
            search_records(records)
        elif choice == 4:  # 退出程序
            save_records(records)
            print("记录已保存，再见！")
            break

        input("\n按任意键返回菜单...")

if __name__ == "__main__":
    main()
