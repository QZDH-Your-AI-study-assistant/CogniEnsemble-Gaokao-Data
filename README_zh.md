# CogniEnsemble-Gaokao-Data:高考真题推理数据集
CogniEnsemble-Gaokao-Data 是启智导航项目自主收集的数据集，旨在推动AI教育快速发展，助力AI应用的开发和AI教师模型的构建。团队构建此数据集的初衷是能够为团队使用模型的微调提供数据支持，希望大家自拿自取。

## 数据集简介
CogniEnsemble-Gaokao-Data数据集涵盖了2010-2022年中国高考的诸多真题以及它的大模型答案。数据集包括675条题目答案对，主要涵盖数学和物理两大理科性质较强的科目。

## 数据集结构
数据集包含一个名为`Gaokao_R.json`的文件，其中包含以下字段：

- `"question"`: 题目的markdown形式描述。
- `"answer"`: 大模型给出的答案。
- `"corr-ans"`: 题目的标准官方答案。
- `"question_id"`:题目的id标识符。

## 数据集处理过程
1. 题目采集：从[Gaokao_Bench](https://github.com/OpenLMLab/GAOKAO-Bench)数据集中获取2010-2022年高考真题。
2. 答案生成：使用[Deepseek-R1](https://github.com/deepseek-ai/DeepSeek-R1)大模型对每个题目进行回答，并获取其生成的答案。
3. 答案校验：将Deepseek-R1生成的答案与官方标准答案进行比对和简单人工清洗，标准如下：
    - 答案不一致的被清洗删除
    - 答案一致的保留
    - 答案一致但格式不正确的进行格式化处理

数据收集和预处理的程序具体已在文件`./src`中展示。

我们也有[huggingface地址](https://huggingface.co/datasets/Interstellar174/Gaokao-LLM-data)
