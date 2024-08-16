import json
import os
from datetime import datetime

import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")


def extract_next(data):
    """
    檢查回傳資料中是否包含 ["paging"]["next"]，如果有則抽取出來。

    參數:
    data (dict): 回傳的資料字典

    回傳:
    str: 如果存在，則回傳 'next' 的值；否則回傳 None
    """
    try:
        result = data["paging"]["next"]
        return result
    except KeyError:
        return None


def build_params(access_token, **kwargs):
    # 將傳入的參數轉換成字典
    params = {key: value for key, value in kwargs.items()}
    # 確保加上 access_token
    params["access_token"] = access_token
    return params


# 取得今天的日期
today = datetime.today()

# 格式化日期為 yyyy-mm-dd
formatted_date = today.strftime("%Y-%m-%d")

params = build_params(
    access_token=ACCESS_TOKEN,
    fields="id,media_product_type,media_type,media_url,permalink,owner,username,text,timestamp,shortcode,thumbnail_url,children,is_quote_post",
    since="2023-07-06",  # 早於這個時間會噴 500
    until=formatted_date,
    # limit=100,
)

user_id = "me"
url = f"https://graph.threads.net/v1.0/{user_id}/threads"


def get_user_profile(url, file_path, params=None):
    if params:
        response = requests.get(url, params=params)
    else:
        response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open(file_path, "a", encoding="utf-8") as file:
            for item in data["data"]:
                if item["media_type"] == "TEXT_POST":  # 只抓有內文的貼文
                    print(item["timestamp"])
                json.dump(item, file, ensure_ascii=False)
                file.write("\n")  # 每筆資料換行
        next_url = extract_next(data)
        if next_url:
            get_user_profile(url=next_url, file_path=file_path)
    else:
        print(f"Error: {response.status_code}")


# 指定文件路徑
file_path = "./content.jsonl"

# 清空文件內容
open(file_path, "w").close()

# 開始遞迴抓取資料並寫入文件
get_user_profile(url, file_path, params)

print(f"Data collected and saved to {file_path}")
