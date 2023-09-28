from haystack import Pipeline
from haystack.nodes import MarkdownConverter, PreProcessor, EmbeddingRetriever
from milvus_haystack import MilvusDocumentStore
import os

document_store = MilvusDocumentStore(recreate_index=True, return_embedding=True, similarity="cosine")

markdown_converter = MarkdownConverter(remove_numeric_tables=True, valid_languages=["en"])

preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=False,
    split_by="word",
    split_length=100,
    split_respect_sentence_boundary=True,
)
retriever = EmbeddingRetriever(document_store=document_store, embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1")

doc_dir = "../data/tiddlers"
files_to_index = [doc_dir + "/" +f for f in os.listdir(doc_dir)]

indexing_pipeline = Pipeline()
indexing_pipeline.add_node(component=markdown_converter, name="markdown", inputs=['File'])
indexing_pipeline.add_node(component=preprocessor, name="preprocessor", inputs=['markdown'])
indexing_pipeline.add_node(component=retriever, name="retriever", inputs=['preprocessor'])
indexing_pipeline.add_node(component=document_store, name="document_store", inputs=['retriever'])

indexing_pipeline.run(file_paths=files_to_index)
