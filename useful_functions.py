

def query_to_table(spql_queried):
    
    preparing = {}

    try:
        spql_return = spql_queried.queryAndConvert()

        for ret in spql_return["results"]["bindings"]:
            for var in ret.keys():
                if var in preparing.keys():
                    preparing[var].append(ret[var]['value'])
                else:
                    preparing[var] = [ret[var]['value']]
        return pd.DataFrame(preparing)

    except Exception as e:
        print("The query has a problem. Here is the error:\n\t", e)