# RAG 概念

來源卡：[S01](../../raw/S01.md)、[S04](../../raw/S04.md)

RAG（Retrieval-Augmented Generation）是先取得與問題相關的外部資料，再將選出的內容放進語言模型上下文以協助回答的架構。Lewis 等人的工作將檢索與生成結合；現代系統常採文件分塊、嵌入、檢索、提示組裝與生成的實務流程，但不是唯一實作。

**注意**：RAG 不是即時上網的同義詞，也不保證消除幻覺。

## 相關概念

[Embedding 與語意向量](embedding.md)、[Chunking、Top-k 與檢索](retrieval.md)、[RAG 端到端流程](pipeline.md)、[限制與評估](limits.md)、[LLM Wiki 與一般 RAG 的差別](wiki-vs-rag.md)
