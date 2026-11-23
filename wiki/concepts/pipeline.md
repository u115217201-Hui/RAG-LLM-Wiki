# RAG 端到端流程

來源卡：[S01](../../raw/S01.md)、[S02](../../raw/S02.md)、[S03](../../raw/S03.md)、[S04](../../raw/S04.md)

**資料準備（離線）**：取得可信來源 → 清理 → Chunking → Embedding → 向量索引（或其他搜尋索引）。

**問答（線上）**：使用者提問 → 問題向量化 → 取得 Top-k 文件 → 檢查相關性與來源 → 組成提示 → LLM 生成 → 附引用與必要的不確定性說明。

兩條流程應分開理解：資料準備不一定每次提問都重做。

## 相關概念

[RAG 概念](rag.md)、[Embedding 與語意向量](embedding.md)、[Chunking、Top-k 與檢索](retrieval.md)、[限制與評估](limits.md)、[LLM Wiki 與一般 RAG 的差別](wiki-vs-rag.md)
