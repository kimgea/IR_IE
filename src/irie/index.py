'''
Created on 10. juni 2014

@author: Kim-Georg Aase
'''



class BaseDocIndex( object ):
    """
        Base class used to access document info by various methods.
        This class must be used when creating custom document collections (inverted index,...)
        
        TODO:
            Remove index in name???
    
        Methods to add:
            doc_word_count
            doc_len
            doc_word_exist
            doc_max_word_count
            doc_count
            
            doc_vector(doc)
            
            terms
            docs - list of doc names/id
            
            add_doc
            remove_doc
            update_doc
    """
    def __init__( self ):
        pass
