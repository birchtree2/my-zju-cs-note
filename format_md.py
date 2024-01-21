#处理markdown文件的各种格式问题
import os
import re

def add_newlines_to_mathjax(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r+',encoding='utf-8') as f:
                    content = f.read()

                    # 使用正则表达式匹配行间公式并替换
                    content = re.sub(r'\$\$(.*?)\$\$', r'\n\n$$\1$$\n\n', content, flags=re.DOTALL)

                    # 将修改后的内容写回文件
                    f.seek(0)
                    f.write(content)
                    f.truncate()

# 指定目录路径
directory_path = "./docs"

# 调用函数
add_newlines_to_mathjax(directory_path)
