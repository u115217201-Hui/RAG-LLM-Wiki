# Chunking、Top-k 與檢索

來源卡：[S03](../../raw/S03.md)、[S04](../../raw/S04.md)

**Chunking** 將長文件切分成便於檢索的小段；切太碎容易失去上下文，切太長則可能引入雜訊。**Top-k** 指依相似度取回前 k 筆候選，並不等於前 k 筆必然正確。

Faiss 能支援向量相似度搜尋；DPR 示範密集檢索方法。檢索後可考慮重排序，但並非本次實作的必備元件。

## 相關概念

[RAG 概念](rag.md)、[Embedding 與語意向量](embedding.md)、[RAG 端到端流程](pipeline.md)、[限制與評估](limits.md)、[LLM Wiki 與一般 RAG 的差別](wiki-vs-rag.md)
