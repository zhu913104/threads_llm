import json


def load_thread_text():
    def read_jsonlines(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # 逐行讀取並解析 JSON
                data = json.loads(line)
                yield data

    # 指定文件路徑
    file_path = "./content.jsonl"
    a = ""
    # 讀取並處理 JSONLines 文件中的每個 JSON 對象
    for data in read_jsonlines(file_path):
        if data["media_type"] == "TEXT_POST":
            if len(data["text"]) > 50:
                text = data["text"]
                a = a + text + "\\n\\n"

    return a


def save_str_to_text_file(string, file_path):
    """
    將字符串存儲到指定的文本文件中。

    :param string: 要存儲的字符串
    :param file_path: 存儲文本文件的路徑
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(string)
        print(f"字符串已成功存儲到 {file_path}")
    except Exception as e:
        print(f"存儲字符串時發生錯誤: {e}")


# 示例用法
file_path = "./content.txt"
save_str_to_text_file(load_thread_text(), file_path)
