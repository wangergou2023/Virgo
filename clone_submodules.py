import os
import re

# 打开并读取.gitmodules文件的内容
with open(".gitmodules", "r") as file:
    gitmodules_content = file.read()

def extract_submodules_info(gitmodules_content):
    # 使用正则表达式从.gitmodules内容中提取子模块的路径和URL
    pattern = r'\[submodule "(.*?)"\]\n\tpath = (.*?)\n\turl = (.*?)\n'
    return re.findall(pattern, gitmodules_content)

def display_submodules(submodules):
    # 显示所有可用的子模块
    print("Available submodules:")
    for idx, (name, path, url) in enumerate(submodules, 1):
        print(f"{idx}. {name} (Path: {path}, URL: {url})")

def clone_selected_submodules(submodules, selected_indices):
    # 根据用户选择的索引克隆选定的子模块
    for idx in selected_indices:
        name, path, url = submodules[idx-1]
        print(f"Cloning {name} into {path}...")
        os.system(f"git clone {url} {path}")

def main():
    try:
        print("Starting script...")
        # 从.gitmodules文件内容中提取子模块信息
        submodules = extract_submodules_info(gitmodules_content)
        # 显示所有子模块
        display_submodules(submodules)

        # 提示用户输入要克隆的子模块的编号
        selection = input("Enter the numbers of the submodules you want to clone (comma separated) or 'all' for all submodules: ")

        # 如果用户选择了"all"，则选择所有子模块，否则选择指定的子模块
        if selection == 'all':
            selected_indices = list(range(1, len(submodules) + 1))
        else:
            selected_indices = list(map(int, selection.split(',')))
        # 克隆选定的子模块
        clone_selected_submodules(submodules, selected_indices)

    except Exception as e:
        # 如果在执行过程中出现错误，打印错误信息
        print(f"An error occurred: {e}")

# 运行脚本
main()
