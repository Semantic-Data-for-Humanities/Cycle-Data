

from SPARQLWrapper import SPARQLWrapper, SPARQLWrapper2, JSON, TURTLE, XML, RDFXML
import numpy as np
import pandas as pd



def query_to_table(spql_queried):
    
    """
    Function taking an endpoint associated with a SPARQL query
    with the return format set on JSON, and returning the results
    as a Pandas DataFrame.
    The function will directly transmit the query to the endpoint,
    receive and transform the results.
    
    :param spql_queried: A SPARQLWrapper.Wrapper.SPARQLWrapper object
        to which are already defined :
        - an endpoint with SPARQLWrapper()
        - a result format with variable.setReturnFormat(JSON)
        - a query to transmit with variable.setQuery()
    
    """
    
    preparing = {}

    try:
        spql_return = spql_queried.queryAndConvert()
        
        for ret in spql_return["results"]["bindings"]:
            for var in ret.keys():
                if var not in preparing.keys():
                    preparing[var] = []
                    
        for ret in spql_return["results"]["bindings"]:
            for var in preparing.keys():
                if var in ret.keys():
                    preparing[var].append(ret[var]['value'])
                else:
                    preparing[var].append('None')
        return pd.DataFrame(preparing)

    except Exception as e:
        print("The query has a problem. Here is the error:\n\t", e)