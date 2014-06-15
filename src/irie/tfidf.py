'''
Created on 10. juni 2014

@author: Kim-Georg Aase
'''
from math import log

#####################################
#
#    TF: Term Frequency
#
def tf_raw( word, doc, doc_index ):
    return doc_index.doc_word_count( word )

def tf( word, doc, doc_index ):
    return float( doc_index.doc_word_count( word ) ) / doc_index.doc_len( doc )

def tf_boolean( word, doc, doc_index ):
    if doc_index.doc_word_exist( word ):
        return 1
    else:
        return 0

def tf_augmented( word, doc, doc_index ):
    return 0.5 + ( ( 0.5 * doc_index.doc_word_count( word ) ) / 
                   ( float( doc_index.doc_max_word_count( doc ) ) ) )


#####################################
#
#    IDF: Inverse Document Frequency
#
def idf( word, doc_index ):
    try:
        return log( doc_index.doc_count() / doc_index.docs_containing_word_count( word ) )
    except:
        return log( doc_index.doc_count() )



##############################################
#
#    TF-IDF
#

def tfidf_base( func, word, doc, doc_index ):
    """
        A base function, used to chose tf func
    """
    return func( word, doc, doc_index ) * idf( word, doc_index )


def tfidf( word, doc, doc_index ):
    return tfidf_base( tf, word, doc, doc_index )

def tfidf_raw( word, doc, doc_index ):
    return tfidf_base( tf_raw, word, doc, doc_index )

def tfidf_boolean( word, doc, doc_index ):
    return tfidf_base( tf_boolean, word, doc, doc_index )

def tfidf_augmented( word, doc, doc_index ):
    return tfidf_base( tf_augmented, word, doc, doc_index )
