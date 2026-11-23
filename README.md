# RAG LLM Wiki + HTML 教學簡報

## 作業成果
- **主題**：RAG 技術入門：讓 AI 學會查資料再回答。對象：初學者，深度：入門＋技術原理。
- **Wiki**：`wiki/index.md`（6 個互聯概念頁）；來源：`raw/S01.md`～`raw/S05.md`（五篇學術來源的可追溯摘記卡）。
- **教學 HTML**：`index.html`（十頁可翻頁簡報）；`workflow.html`（Loop/Graph 與反思）。
- **規則**：`AGENTS.md`（Ingest、Query、Lint）。
- **實際紀錄**：`wiki/log.md`、`checks/report.md`、`checks/validate.py`。

## 使用說明
在瀏覽器直接開啟 `index.html`，或將**整個資料夾內容**放到 GitHub Repository 根目錄，啟用 GitHub Pages：Settings → Pages → Deploy from a branch → main → /(root)。左右鍵或畫面按鈕換頁。

## 注意與範圍
這是符合 Karpathy LLM Wiki 概念的**輕量、檔案式演示**，不是現成 Wiki SaaS、沒有向量 DB、也沒有進行 LLM API 自動批次呼叫。Ingest 在本次意指五篇論文的**來源卡／摘要摘記**整理、來源交叉連結和 Wiki 生成，並非全文納入系統。若老師要求論文全文 ingest，需依原文存取權另行匯入全文。不要聲稱已在 GitHub 上發布，直到實際上傳。

## 參考
- Wiki 方法：<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- 其他五份學術來源：見 `wiki/index.md`。
