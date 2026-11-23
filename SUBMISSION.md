# 作業繳交內容（上傳 GitHub 後填上兩個連結）

## 1. Wiki 主題與介紹
RAG 技術入門：讓 AI 學會查資料再回答。以 LLM Wiki 整理五篇學術論文來源卡，建立互聯的概念筆記，介紹 Embedding、Chunking、Top-k、檢索與生成，以及 RAG 限制。

## 2. Wiki 成果
`wiki/index.md`（6 個互聯概念頁）與 `raw/S01.md`～`raw/S05.md`（5 篇可信來源卡）、`wiki/log.md`（逐篇 ingest 紀錄）。
Wiki 連結：`https://github.com/<帳號>/<Repository>/blob/main/wiki/index.md`（請替換）

## 3. 教學 HTML 簡報連結
`https://<帳號>.github.io/<Repository>/`（發布後替換）

## 4. Loop / Graph 說明
選題 → 取得五篇來源卡 → **來源核對 Gate A（失敗回資料取得）** → Ingest 到概念頁並更新索引／log → Query Wiki → 教學大綱 → **主張與引用 Gate B（失敗回查詢／補充）** → 產生 HTML → **靜態檢查 Gate C（失敗回修改）** → 發布。

## 5. 一次實際執行／檢查紀錄
見 `checks/report.md`，可執行 `python checks/validate.py` 驗證五篇來源卡、六個概念頁、十頁投影片與檔案路徑。

## 6. 反思
本次主要問題風險發生在「概念整理與引用核對」：可能混淆 Faiss 與完整向量資料庫，或把 RAG 的效益說成能消除幻覺。因此把內容查核從投影片生成後前移到 Wiki 概念整合完成後（Gate B），並保留產出後的網站結構檢查（Gate C）。這是單次流程觀察，無多輪錯誤次數統計。
