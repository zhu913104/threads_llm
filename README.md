# Threads_llm
因為我很愛發廢文，所以我透過OPENAI做了一個自己風格的故事產生器。
---

這是一組 Python 程式，用於從 Threads API 獲取貼文透過OpenAI生成和處理文章。這些程式包括以下三個部分：

1. `get_threads_post.py`：從 API 獲取貼文數據並保存到 JSONLines 文件中。
2. `gen_story.py`：使用 OpenAI API 根據已有內容生成和修改故事。
3. `etl_post.py`：從 JSONLines 文件中提取文本貼文並將其存儲到文本文件中。

## 使用要求

- Python 3.11
- `requests` 庫（用於 `get_threads_post.py`）
- `openai` 庫（用於 `gen_story.py`）

可以使用以下命令安裝所需的庫：

```bash
pip install -r requirements.txt
```

## `get_threads_post.py`
這個程式從指定的 API 獲取貼文數據並將其保存到 JSONLines 文件中。

使用方法
1. 設置 API 訪問令牌：確保環境變數 ACCESS_TOKEN 設置為有效的 API 訪問令牌。

    - 你可以參考 [Threads 官方文件](https://developers.facebook.com/docs/threads/overview) 了解如何獲取和設置訪問令牌。
2. 運行：

```bash
python get_threads_post.py
```
程式會從 API 獲取貼文數據，過濾出文本貼文，並將其以 JSONLines 格式追加到 content.jsonl 文件中。
## `gen_story.py`
這個程式使用 OpenAI API 根據你過往寫作的內容生成故事。程式包括兩個主要功能：生成新的文本和生成完整故事。

使用方法
1. 設置 OpenAI API token：

   - 確保環境變數 OPEN_AI_KEY 設置為有效的 OpenAI API token。
2. 編輯程式：

   - 修改 prompt，以符合你的需求。
3. 運行：

```bash
python gen_story.py
```
- 程式會讀取 content.txt 文件中的內容，生成新的文本，並基於這些內容生成完整的故事，然後打印出來。
  
> 特別注意，目前會多打幾次修正程式的prompt請注意花費
  
## `etl_post.py`
這個程式從 JSONLines 文件中提取文本貼文，將其合併並保存到文本文件中。

使用方法
1. 確保 JSONLines 文件存在：

- content.jsonl 文件應包含每行為 JSON 對象的貼文數據。
2. 運行：

```bash
python etl_post.py
```
> 程式會從 content.jsonl 文件中讀取文本貼文，將長度大於 50 個字符的文本合併(我某些文章太廢了 ==)，並將結果保存到 content.txt 文件中。
## 注意事項
確保所有程式中的文件路徑都正確設置。
確保 API 訪問令牌和 OpenAI API token正確設置並有效。
如果需要調整程式中的參數或功能，請根據具體需求修改程式。


## Reference
- https://cowton0517.medium.com/come-on-%E4%BD%BF%E7%94%A8-threads-api-%E4%BE%86%E8%87%AA%E5%8B%95%E7%99%BC%E6%96%87%E5%90%A7-792797a68437
- https://developers.facebook.com/docs/threads/overview



## todo
- [ ] 增加使用者可以傳入各種參數
- [ ] 使用click將程式包裝成指令
- [ ] 自動po到Threads