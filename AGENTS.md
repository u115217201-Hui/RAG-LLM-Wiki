# AGENTS.md — RAG LLM Wiki Agent Contract

## 目的與層次
依 Andrej Karpathy llm-wiki 方法建立三層：`raw/` 不變來源層、`wiki/` LLM 可維護概念頁、`AGENTS.md` 執行規格。輸出 `index.html` 教學簡報。

## Ingest
1. 先與使用者確認主題、深度與來源（先討論後生成）。
2. 在 `raw/` 加入 Sxx.md 來源卡，記錄作者、標題、年份、可追溯 URL、摘記範圍。不得暗示只讀摘要等於閱讀全文。
3. 檢查來源可信度、區分研究觀察與一般性結論、找出至少一個可教學的概念。
4. 更新一個以上 `wiki/concepts/` 概念頁，雙向連結、寫來源編號。
5. 更新 `wiki/index.md`，append `wiki/log.md`；不覆寫舊 log。

## Query → Slides
1. 一律先讀 `wiki/index.md`，依問題選概念頁。
2. 每張簡報列出對應來源代碼 Sxx；不可新增沒有 Wiki 支持的精確數據。
3. 以初學者為對象：問題、類比、技術名詞、流程、範例、限制、總結。
4. 使用單一 `index.html`、`assets/style.css`、`assets/slides.js`，可用鍵盤左右方向鍵與按鈕翻頁。
5. 避免聲稱執行過模型檢索、向量庫訓練或完整文獻 ingest；本範例為離線來源卡／Wiki 的輕量實作。

## Lint / Feedback loop
- **Gate A（來源進入 Wiki 前）**：核對來源 URL、主張與層次，不足則返回 source-review。
- **Gate B（生成投影片前）**：每一教學主張能映射 Wiki 頁及來源卡；不符合就返回 query/synthesis。
- **Gate C（產出後）**：檢查 HTML/JS/CSS、十頁完整性、可讀性、引用與連結；失敗回到相應節點。
- 每次至少保留一份可重現的檢查紀錄於 `checks/`。

## 禁止事項
不捏造實驗數據，不將概念性說明說成實測結果，不刪改 raw 來源卡原意，不把 LLM Wiki 與向量資料庫視為同一件事。
