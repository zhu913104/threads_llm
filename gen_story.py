import os

import openai

# 設置 OpenAI API 金鑰
openai.api_key = os.environ.get("OPNE_AI_KEY")


def generate_text_with_style(content, prompt):
    # 使用 OpenAI Chat API 發送請求
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # 确保模型名称正确
        messages=[
            {
                "role": "system",
                "content": "你是一位專業的文章作者，現在你是我請來的幽靈寫手。",
            },
            {
                "role": "user",
                "content": ("以下是我寫的文章內容:\n" f"{content}" f"{prompt}"),
            },
        ],
        # max_tokens=500,  # 可以根據需要調整生成的文本長度
        temperature=0.8,  # 控制生成文本的創造性
    )

    # 處理回應
    annotated_text = response["choices"][0]["message"]["content"]
    return annotated_text


def read_str_from_text_file(file_path):
    """
    從指定的文本文件中讀取字符串。

    :param file_path: 要讀取的文本文件的路徑
    :return: 文件中的字符串內容
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"讀取字符串時發生錯誤: {e}")
        return None


# 示例用法
file_path = "./content.txt"
content = read_str_from_text_file(file_path)
processed_content = content.replace("\\n\\n", "\n\n")

# 生成新的文本
prompt = (
    "請模仿我的行文風格與排版方式杜撰一篇搞笑的故事有關於我的在交友軟體遇到的奇怪女生"
)
generated_text = generate_text_with_style(processed_content, prompt)

print(generated_text)
print("---開始第一次校稿---")


def generate_complete_story(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 或其他你需要的模型
        messages=[
            {
                "role": "system",
                "content": "你是一位專業的故事講述者，能夠創作完整而連貫的故事。",
            },
            {
                "role": "user",
                "content": "請根據以下提示以及我過往寫過的文章將故事給重新改寫確保這是一個完整的故事。確保故事有開頭、中間和結尾，並且情節完整好笑，且字數精簡。\n\n"
                f"故事開始：{prompt}",
            },
        ],
        # max_tokens=500,  # 增加 tokens 上限以容納完整故事
        temperature=0.8,  # 控制生成文本的創造性
    )

    return response.choices[0].message["content"]


# 生成故事
complete_story = generate_complete_story(generated_text)

print(complete_story)
print("---開始第二次校稿---")

# 生成故事
complete_story = generate_complete_story(generated_text)

print(complete_story)
