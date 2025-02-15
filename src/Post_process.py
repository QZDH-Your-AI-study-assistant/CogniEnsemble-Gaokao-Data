import json
import os
import re

files = os.listdir('path_to_your_dataset')

### 1. 添加“corr-ans”字段，提取正确答案

for file in files:
    # 读取A.json文件
    with open('path_to_your_dataset', 'r', encoding='utf-8') as file_a:
        dataset_a = json.load(file_a)

    # 读取B.json文件
    dir = 'path_to_your_dataset' + file
    with open(dir, 'r', encoding='utf-8') as file_b:
        dataset_b = json.load(file_b)

    # 构建一个问题到答案的映射
    question_answer_map = {item['question']: item['answer'] for item in dataset_b['example']}

    # 遍历数据集A
    for item in dataset_a:
        question = item['question']
        # 在映射中查找问题的标准答案
        correct_answer = question_answer_map.get(question, [])
        # 如果答案列表不为空，取第一个答案，否则为空字符串
        if correct_answer:
            item['corr-ans'] = correct_answer

    # 将更新后的数据集A保存到新文件
    with open('path_to_your_dataset', 'w', encoding='utf-8') as output_file:
        json.dump(dataset_a, output_file, ensure_ascii=False, indent=4)

### 2. 添加“LLM-ans”字段，并且加上编号(开始就没养成编号的习惯，真的太出生了)        

with open('path_to_your_dataset','r',encoding = 'utf-8') as file_a:
    data_ = json.load(file_a)

index = 1
# 处理每个元素
for item in data_:
    answer = item['answer']
    # 使用正则表达式查找 \boxed{XXX} 中的 XXX
    match = re.search(r'\\boxed\{(.*?)\}', answer)
    if match:
        # 如果找到，将匹配的内容作为 LLM-ans 的值
        item['LLM-ans'] = match.group(1)
    else:
        # 如果未找到，将 LLM-ans 的值设为 None
        item['LLM-ans'] = None
    item['answer'] = item['answer'].replace('<\\think>', '</think>')
    item['question_id'] = 'GK-'+str(index)
    index += 1

# 将处理后的数据写入新的JSON文件
with open('path_to_your_dataset', 'w', encoding='utf-8') as file:
    json.dump(data_, file, ensure_ascii=False, indent=4)
    
