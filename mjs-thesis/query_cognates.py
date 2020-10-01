import pandas as pd
import json
import re

"""
Query params are of format:

global: {
  "predicate": "and", "or" or "none",
    -  determines if row has to fulfill regex on one column, all or none  
  "regex": string or null
    -  regex string to apply to all columns, will ignore and use columns if set to null
},
colname: {
    "exclude": boolean,
    "regex": "regex_str"
}

"""

df_file = "formatted_cognates.csv"
results_file = "query_results.csv"
predicates = {
    "or": any,
    "and": all,
    "none": lambda a: not any(a)
}


def main():  
    # load data file and create dataframe for results
    cognates = pd.read_csv(df_file, keep_default_na=False)
    results_df = pd.DataFrame(columns=cognates.columns)
    
    # load query
    with open("query.json", encoding='utf8') as json_file:
        query = json.load(json_file)
        
    exclude = get_excluded(query)

    global_settings = query['global']
    
    predicate = predicates[global_settings['predicate']]
    
    if global_settings['regex'] is None:
        query_columns(cognates, results_df, query, predicate, exclude)
        
    else:
        regex = global_settings['regex']
        filter_df(cognates, results_df, regex, predicate, exclude)
    
    results_df.to_csv(results_file, index=False)
        

def query_columns(cognates, results_df, query, predicate, exclude):
    patterns = {}
    for col, params in query.items():
        if col == 'global':
            continue
        patterns[col] = params['regex']
    return filter_df(cognates, results_df, patterns, predicate, exclude)
    
# regex can be either a single string or a list of strings
# for every column
def filter_df(cognates, results_df, regex, predicate, exclude):
    patterns = {}
    language_cols = [col for col in cognates.columns if 'gloss' not in col]
    
    if type(regex) is str:
        patterns.update({col: re.compile(regex) for col in language_cols})
    else:
        patterns.update({col: re.compile(regex[col]) for col in language_cols})
    for index, row in cognates.iterrows():
        if filter_row(row, patterns, predicate, exclude):
            results_df.loc[index] = row
    

def filter_row(row, patterns, predicate, exclude):
    hits = []
    for col, val in row.items():
        if 'gloss' in col:
            continue
        elif col in exclude:
            continue
        hits.append(bool(
            patterns[col].search(val)
        ))
    return predicate(hits)

def get_excluded(query):
    exclude = []
    for column, params in query.items():
        if column == 'global':
            continue
        if params['exclude']:
            exclude.append(column)
    return exclude

if __name__ == "__main__":
    main()