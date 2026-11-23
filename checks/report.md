# 實際執行與檢查紀錄｜2026-11-23

## 建立與 ingest
- 先與使用者確定：RAG、入門加技術原理、GitHub + Markdown Wiki + HTML。
- 已建立五份論文來源卡 `raw/S01.md`～`S05.md`（含出版頁面 URL 與核對摘記，並非全文攝入）。
- 依序整合六個概念頁，更新 `wiki/index.md`、`wiki/log.md`，再從 Wiki 整理十頁教學內容。

## 第一次檢查發現的問題
- 技術內容的主要風險：把 Faiss 說成完整向量資料庫，以及把 RAG 說成能完全消除幻覺。修改方式：在 `wiki/concepts/retrieval.md` 與 `wiki/concepts/rag.md` 預先加上適用範圍與限制，簡報第 6、9 頁保留說明。
- 工具執行的實際錯誤：第一次 `checks/validate.py` 執行因生成時換行字串轉義失誤而 `SyntaxError: unterminated string literal`，已修改列印指令後重新執行。

## 第二次檢查結果
- **PASS**：來源卡 5 份、Wiki 概念頁 6 篇、投影片 10 頁、HTML 內部路徑存在、控制項 ID 存在。
- **PASS**：`node --check assets/slides.js`，JavaScript 語法檢查通過。
- **尚未執行**：真實瀏覽器操作與 GitHub Pages 部署；上傳後需人工逐頁點擊與確認。

## Graph 調整與反思
主要內容風險集中在 **Wiki 概念整理／主張核對**，因此將術語正確性與證據來源檢查提前到 Wiki 整合之後、HTML 生成之前（Gate B）。另外保留產物後的自動化結構驗證（Gate C），因為本次實際發生的檢查腳本語法錯誤不可能只靠來源核對發現。這是一回合工作紀錄，不聲稱有多次運行統計。
