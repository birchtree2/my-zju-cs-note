import os
import re
import subprocess
from bs4 import BeautifulSoup
def replace_latex_commands(md_text, replace_dict):
    # 构建正则表达式模式，匹配 LaTeX 命令
    pattern = r'(?:\$[^\$]*|\\\()[^\$\\\()]*' + '|'.join(re.escape(command) for command in replace_dict.keys()) + r'[^\$\\\()]*(?:\$\$|\))'
    
    # 使用 re.sub() 函数替换命令
    replaced_text = re.sub(pattern, lambda match: replace_dict[match.group()], md_text)
    
    return replaced_text

def upd_md(directory, replace_dict):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # 使用正则表达式匹配行间公式并替换
                    content = re.sub(r'\$\$(.*?)\$\$', r'\n\n$$\1$$\n\n', content, flags=re.DOTALL)

                    # 批量替换 LaTeX 命令
                    content = replace_latex_commands(content, replace_dict)

                with open(file_path, 'w', encoding='utf-8') as f:
                    # 将修改后的内容写回文件
                    f.write(content)

# 指定目录路径
md_dir = "./docs/23-24秋冬学期/大学物理(乙)II/静电场2_"
html_dir = "./site/23-24秋冬学期/大学物理(乙)II/静电场2_"
# 指定替换字典表
replace_dict = {
    '\\oiint': '\\oint'
    # '\\iint': '\\int\\int',
}

if __name__ == "__main__":
    #处理markdown文件
    upd_md(md_dir, replace_dict)
    #调用mkdocs
    subprocess.run(["mkdocs", "build"])
    # 处理 HTML 文件
    
    for filename in os.listdir(html_dir):
        if filename.endswith(".html"):
            file_path = os.path.join(html_dir, filename)
            with open(file_path, "r",encoding='utf-8') as f:
                soup = BeautifulSoup(f, "html.parser")
                # 处理 img 标签的 src 属性
                for img in soup.find_all("img"):
                    src = img["src"]
                    if src.startswith(".."):
                        img["src"] = "../" + src
            with open(file_path, "w",encoding='utf-8') as f:
                f.write(str(soup))

    # 推送到 Git 仓库
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Update site"])
    subprocess.run(["git", "push"])