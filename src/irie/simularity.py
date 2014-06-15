'''
Created on 10. juni 2014

@author: Kim-Georg Aase
'''

from numpy import dot
from numpy.linalg import norm


def cosine_sim( q, d ):
    dp = float( dot( q, d ) )
    np = float( ( norm( q ) ) * ( norm( d ) ) )
    if( np == 0 ):
        np = 1
    return float( dp / np )


