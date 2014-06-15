'''
Created on 10. juni 2014

@author: Kim-Georg Aase
'''

import math
from scipy.stats.distributions import chi

from operator import mul
from fractions import Fraction


def nCk( n, k ): 
    return int( reduce( mul, ( Fraction( n - i, i + 1 ) for i in range( k ) ), 1 ) )



def two_nominal_variables_test_abcd( doc_index, func, p = 0.01 ):
    """
        TODO: link selected term doc??? What terms are important for each doc ???
        IMPORTANT: FINISH a,b,c,d calculation
    """
    selected_terms = set( [] )
    
    for doc in doc_index.docs:
        for term in doc_index.terms:
            a, b, c, d = 0, 0, 0, 0
            
            # TODO: calc a,b,c,d
            
            p = func( a, b, c, d, p )
            
            if not p:
                continue
            
            selected_terms.add( term )
            
    return selected_terms

###################################
#
#    Fisher's exact test
#

def fishers_simple( a, b, c, d ):
    n = a + b + c + d
    return float( ( nCk( a + b, a ) * nCk( c + d, c ) ) ) / float( nCk( n, a + c ) )

def fishers_simple_test( a, b, c, d , p = 0.01 ):
    f = fishers_simple( a, b, c, d )
    if f <= p:
        return True
    return False

def fishers( doc_index, p = 0.01 ):
    """
    """
    return two_nominal_variables_test_abcd( doc_index, fishers_simple_test, p )


###############################
#
#    Chi Squared
#

def chiSquare_simple( a, b, c, d ):
    thresh_expected = 5
    
    n = float( a + b + c + d )
    
    expected_a = n * ( ( ( a + c ) / n ) * ( ( a + b ) / n ) ) 
    expected_b = n * ( ( ( b + d ) / n ) * ( ( b + a ) / n ) ) 
    expected_c = n * ( ( ( c + a ) / n ) * ( ( c + d ) / n ) ) 
    expected_d = n * ( ( ( d + b ) / n ) * ( ( d + c ) / n ) ) 
    
    if min( expected_a, expected_b, expected_c, expected_d ) < thresh_expected:
        return 0
    
    # TODO: force float 
    chi = float( n * math.pow( ( a * d - b * c ), 2 ) ) \
        / float( ( a + c ) * ( a + b ) * ( b + d ) * ( d + c ) ) 
    
    return chi
          
          
def chiSquare_simple_test( a, b, c, d, p = 0.01 ):  
    p_table = {
             0.1:2.71,
             0.05:3.84,
             0.01:6.63,
             0.005:7.88,
             0.001:10.83,
             }
    if p not in p_table:
        raise Exception( 'P par is not valid', 'must be: 0.1, 0.05, 0.01, 0.005 or 0.001' )
    
    chi = chiSquare_simple( a, b, c, d )
    if chi == 0:
        return fishers_simple_test( a, b, c, d )
    
    if chi < p_table[p]:
        return False
    
    return True


def chiSquare( doc_index, p = 0.01 ):
    """
    """
    return two_nominal_variables_test_abcd( doc_index, chiSquare_simple_test, p )


###############################
#
#    Mutual Information
#

def mutual_information_simple( a, b, c, d ):
    n = float( a + b + c + d )
    x1 = ( a / n ) * math.log( ( n * a ) / float( ( a + b ) * ( a + c ) ), 2 )
    x2 = ( b / n ) * math.log( ( n * b ) / float( ( a + b ) * ( b + d ) ), 2 )
    x3 = ( c / n ) * math.log( ( n * c ) / float( ( a + c ) * ( c + d ) ), 2 )
    x4 = ( d / n ) * math.log( ( n * d ) / float( ( b + d ) * ( c + d ) ), 2 )
    return x1 + x2 + x3 + x4

def mutual_information_simple_test( a, b, c, d, p = 0.01 ):
    f = mutual_information_simple( a, b, c, d )
    # TODO: FIX test thresh
    if f <= p:
        return True
    return False

def mutual_information( doc_index, p = 0.01 ):
    """
    """
    return two_nominal_variables_test_abcd( doc_index, mutual_information_simple_test, p )


if __name__ == '__main__':
    print "FISHER"
    print fishers_simple( 1, 9, 11, 3 )
    print "SHOULD BE: 0.001346076"
    print "ChiSquare"
    print chiSquare_simple( 36, 14, 30, 25 )
    print "SHOULD BE: 3.418"
    print "Mutual Information"
    print mutual_information( 49, 27652, 141, 774106 )
    print "SHOULD BE: 0.0001105"
    pass
