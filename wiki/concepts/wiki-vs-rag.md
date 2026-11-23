# LLM Wiki 與一般 RAG 的差別

來源卡：[S01](../../raw/S01.md)

一般 RAG 常在每次提問時從原始文件中檢索片段。LLM Wiki 則讓 LLM 在資料加入時，把理解與交叉連結寫入**持久 Markdown 概念頁**，之後以 Wiki 索引查詢。這是知識管理架構上的差別，兩者可以互補。

本頁關於 LLM Wiki 的方法設計來自 Andrej Karpathy 的 llm-wiki Gist（方法來源，不計入五篇 RAG 技術論文）。

## 相關概念

[RAG 概念](rag.md)、[Embedding 與語意向量](embedding.md)、[Chunking、Top-k 與檢索](retrieval.md)、[RAG 端到端流程](pipeline.md)、[限制與評估](limits.md)
