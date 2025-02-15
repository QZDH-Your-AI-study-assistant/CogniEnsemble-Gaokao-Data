from qianfan import Qianfan
import os
import json
import warnings
import time

warnings.filterwarnings("ignore")

directory = 'path_to_your_dataset'
files = os.listdir(directory)

Queries = []
total_len = 0

with open('path_to_your_dataset','r',encoding='utf-8') as file_:
    ques_ex = json.load(file_)
    ques_ex_list = [item['question'] for item in ques_ex]
    total_len = len(ques_ex_list)

for file in files:
    file_path = os.path.join(directory, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        questions = [item['question'] for item in data['example']]
        for question in questions:
            if question not in ques_ex_list:
                Queries.append(question)
                
length = len(Queries)
remain_len = 747 - length
                
print('-----------------------------------------')
print(f'Up to now, {remain_len} questions are solved')
                
client = Qianfan(
    api_key="Your qianfan apikey" 
)

result_file = 'path_to_your_dataset.json'

def save_result(result, file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        existing_data.extend(result)
    else:
        existing_data = result
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

total_questions = len(Queries)
for i in range(0, total_questions):
    question = Queries[i]
    success = False
    while not success:
        print(f'Question {remain_len + i+1}/{remain_len + total_questions} is answering...')
        try:
            completion = client.chat.completions.create(
                model="deepseek-r1",
                messages=[
                    {'role': 'system', 'content': '你是一个中小学理科老师，你擅长解决中国高考数学，物理题，请你解答这道题，详细思考并解答。'},
                    {'role': 'user', 'content': question}
                ]
            )
            answer = completion.choices[0]
            answer_str = f'<think>{answer.message.reasoning_content}</think>{answer.message.content}'
            QA = [{'question': question, 'answer': answer_str}]
            save_result(QA, result_file)
            print('------------------------------------------------------------------')
            print(f'Question {remain_len + i+1}/{remain_len + total_questions} is answered')
            print('------------------------------------------------------------------')
            success = True  # 标记为成功，退出 while 循环
        except Exception as e:
            print(f">>>>>>>>Error occurred while processing question,retrying.....")
            # 这里可以添加一些延迟，避免频繁重试导致问题加剧
            time.sleep(10)  # 等待 10 秒后重试