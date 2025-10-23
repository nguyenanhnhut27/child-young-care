import os
from typing import Dict, List, Optional
import PyPDF2
import docx
from io import BytesIO

class DocumentProcessor:
    """
    Processes uploaded documents and extracts text for the AI agent to use.
    Supports PDF, DOCX, TXT, and MD files.
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize document processor.
        
        Args:
            chunk_size: Size of text chunks for processing
            chunk_overlap: Overlap between chunks to maintain context
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.processed_documents = []
    
    def process_file(self, uploaded_file) -> Dict:
        """
        Process an uploaded file and extract text.
        
        Args:
            uploaded_file: Streamlit UploadedFile object
        
        Returns:
            Dictionary with processing results
        """
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        try:
            if file_extension == 'pdf':
                text = self._extract_from_pdf(uploaded_file)
            elif file_extension == 'docx':
                text = self._extract_from_docx(uploaded_file)
            elif file_extension in ['txt', 'md']:
                text = self._extract_from_text(uploaded_file)
            else:
                return {
                    "success": False,
                    "error": f"Unsupported file type: {file_extension}"
                }
            
            # Split into chunks
            chunks = self._split_into_chunks(text)
            
            # Store processed document
            doc_info = {
                "filename": uploaded_file.name,
                "file_type": file_extension,
                "text": text,
                "chunks": len(chunks),
                "chunk_list": chunks
            }
            
            self.processed_documents.append(doc_info)
            
            return {
                "success": True,
                "filename": uploaded_file.name,
                "chunks": len(chunks),
                "preview": text[:500] + "..." if len(text) > 500 else text
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _extract_from_pdf(self, uploaded_file) -> str:
        """Extract text from PDF file"""
        pdf_reader = PyPDF2.PdfReader(BytesIO(uploaded_file.read()))
        text = ""
        
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        return text
    
    def _extract_from_docx(self, uploaded_file) -> str:
        """Extract text from DOCX file"""
        doc = docx.Document(BytesIO(uploaded_file.read()))
        text = ""
        
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        
        return text
    
    def _extract_from_text(self, uploaded_file) -> str:
        """Extract text from TXT or MD file"""
        return uploaded_file.read().decode('utf-8')
    
    def _split_into_chunks(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks for better context preservation.
        
        Args:
            text: Full text to split
        
        Returns:
            List of text chunks
        """
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start += self.chunk_size - self.chunk_overlap
        
        return chunks
    
    def search_documents(self, query: str, top_k: int = 3) -> List[Dict]:
        """
        Search through processed documents for relevant content.
        
        Args:
            query: Search query
            top_k: Number of top results to return
        
        Returns:
            List of relevant document chunks
        """
        results = []
        query_lower = query.lower()
        
        for doc in self.processed_documents:
            for i, chunk in enumerate(doc['chunk_list']):
                # Simple keyword matching (can be enhanced with embeddings)
                relevance_score = sum(
                    1 for word in query_lower.split() 
                    if word in chunk.lower()
                )
                
                if relevance_score > 0:
                    results.append({
                        "filename": doc['filename'],
                        "chunk_index": i,
                        "content": chunk,
                        "relevance": relevance_score
                    })
        
        # Sort by relevance and return top k
        results.sort(key=lambda x: x['relevance'], reverse=True)
        return results[:top_k]
    
    def get_all_documents(self) -> List[Dict]:
        """Get information about all processed documents"""
        return [
            {
                "filename": doc['filename'],
                "file_type": doc['file_type'],
                "chunks": doc['chunks'],
                "preview": doc['text'][:200] + "..."
            }
            for doc in self.processed_documents
        ]
    
    def get_document_by_name(self, filename: str) -> Optional[Dict]:
        """Get a specific document by filename"""
        for doc in self.processed_documents:
            if doc['filename'] == filename:
                return doc
        return None
    
    def clear_documents(self):
        """Clear all processed documents"""
        self.processed_documents = []


class RAGSystem:
    """
    Retrieval-Augmented Generation system for document-based queries.
    Combines document retrieval with AI generation.
    """
    
    def __init__(self, document_processor: DocumentProcessor, agent):
        """
        Initialize RAG system.
        
        Args:
            document_processor: DocumentProcessor instance
            agent: MentalHealthAgent instance
        """
        self.doc_processor = document_processor
        self.agent = agent
    
    def query_with_context(self, query: str, top_k: int = 3) -> str:
        """
        Query the AI agent with relevant document context.
        
        Args:
            query: User query
            top_k: Number of relevant document chunks to include
        
        Returns:
            AI response with document context
        """
        # Retrieve relevant documents
        relevant_docs = self.doc_processor.search_documents(query, top_k)
        
        # Build context from documents
        context = "Relevant information from uploaded documents:\n\n"
        for i, doc in enumerate(relevant_docs, 1):
            context += f"[Source {i}: {doc['filename']}]\n{doc['content']}\n\n"
        
        # Combine context with query
        full_query = f"{context}\nUser Question: {query}\n\nPlease answer the question using the provided context from the documents when relevant, and supplement with your knowledge of child and adolescent mental health."
        
        # Get AI response
        return self.agent.query(full_query)