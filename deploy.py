# TODO: 1. 忽略resources文件夹
#       2. 图片复制到assets
#       3. intro
#       4. gpt latex替换
# 指定目录路径
md_dir = "./docs/"
html_dir = "./site/"
# 指定替换字典表
replace_dict = {
    '\\oiint': '\\oint',
    '\\infin': '\infty',
    '\\exist': '\\exists'
    # '\\iint': '\\int\\int',
}
import os
import re
import subprocess
from bs4 import BeautifulSoup

def upd_md(directory, replace_dict):
    frontmatter = "---\ncomments: true\n---\n"  # frontmatter to add for comment enable
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Add frontmatter if not exist
                    if not content.startswith(frontmatter):
                        content = frontmatter + content

                    # Add new line before $$ if not exist
                    content = re.sub(r'(?<!\n)\$\$', r'\n\n$$', content)

                    # Replace only whole words
                    # for old, new in replace_dict.items():
                        # Replace the whole words, not partial ones
                        # old = re.escape(old)
                        # content = re.sub(r'\b' + old + r'\b', new, content)

                with open(file_path, 'w', encoding='utf-8') as f:
                    # 将修改后的内容写回文件
                    f.write(content)



def calculate_relative_path(image_path, html_dir):
    image_dir = os.path.dirname(image_path)
    relative_path = os.path.relpath(image_dir, html_dir)
    num_levels = len(relative_path.split(os.sep))
    return num_levels

def modify_image_paths(html_dir):
    for root, dirs, files in os.walk(html_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding='utf-8') as f:
                    soup = BeautifulSoup(f, "html.parser")
                    # 处理 img 标签的 src 属性
                    for img in soup.find_all("img"):
                        src = img["src"]
                        if src.startswith(".."):
                            #计算当前文件位置和根目录的偏差
                            num_levels = calculate_relative_path(file_path, html_dir)
                            cleaned_src = src.lstrip('../')  #去掉前面的../
                            modified_src = os.path.join(*([".."] * num_levels), cleaned_src) #加上正确的../个数
                            modified_src = modified_src.replace('_resources', 'assets/images')
                            # print(file_path,cleaned_src,html_dir,num_levels,modified_src)
                            img["src"] = modified_src
                with open(file_path, "w", encoding='utf-8') as f:
                    f.write(str(soup))





if __name__ == "__main__":
    #处理markdown文件
    upd_md(md_dir, replace_dict)
    #调用mkdocs
    subprocess.run(["mkdocs", "build"])
    # 处理 HTML 文件
    modify_image_paths(html_dir)
    subprocess.run(["powershell.exe","cp",".\\_resources\\*","-r",".\\site\\assets\\images"])
    # 推送到 Git 仓库
    # subprocess.run(["powershell.exe","cd","./site"])
    # subprocess.run(["git", "log"])
    # subprocess.run(["git", "commit", "-m", "Update site"])
    # subprocess.run(["git", "push"])