import os


def generate_tree(path, level=0):
    """
    递归遍历文件夹，生成文件夹结构
    """
    tree = ""
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            tree += "  " * level + f"├── {item}/\n"
            tree += generate_tree(item_path, level + 1)
        else:
            tree += "  " * level + f"├── {item}\n"
    return tree


def save_to_readme(folders, output_file="README.md"):
    tree_structure = "# 项目文件夹结构\n\n"

    for folder in folders:
        tree_structure += f"## {folder} 文件夹结构\n\n```\n"
        if os.path.isdir(folder):
            tree_structure += generate_tree(folder)
        else:
            tree_structure += f"{folder} 不存在\n"
        tree_structure += "```\n\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(tree_structure)


# 获取当前目录下特定两个文件夹的结构
folders = ["Listing运营", "亚马逊广告运营","DeepBI其它优势"]
save_to_readme(folders)
