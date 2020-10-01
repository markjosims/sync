import pandas as pd
from collections import defaultdict
import json

in_file = "epps_cognate_database.csv"
out_file = "unique_chars.json"

def main():
    df = pd.read_csv(in_file, keep_default_na=False)
    
    unique_chars = defaultdict(set)
    
    for _, row in df.iterrows():
        for col, data in row.items():
            if not data or type(data) is not str:
                continue
            for char in data:
                unique_chars[col].add(char)
                
    for k, v in unique_chars.copy().items():
        unique_chars[k] = [f"{char} : {char.encode('unicode-escape').decode('utf8')}" for char in v]
        
    del unique_chars['gloss_pt']
    del unique_chars['gloss_en']
        
    with open(out_file, 'w', encoding='utf8') as f:
        json.dump(unique_chars, f, indent=2, ensure_ascii=False)

# general methods  
def pipeline(val, functions):
    for f in functions:
        val = f(val)
    return val

def basic_format(s):
    return pipeline(s, [
            remove_punct,
            back_as_central,
            implosives_as_glottalized,
            merge_apostrophes,
            merge_r
        ])

def remove_punct(s):
    punct = [
        "\u031a", "-", ";", "[", "]", "(", ")"
    ]
    return make_reps({p: "" for p in punct}, s)

def back_as_central(s):
    reps = {
        "ɤ": "ә",
        "ɯ": "ɨ"
    }
    return make_reps(reps, s)
    
def implosives_as_glottalized(s):
    reps = {
        "ɓ": "b\u02bc",
        "ɗ": "d\u02bc"
    }
    return make_reps(reps, s)

def merge_apostrophes(s):
    reps = {
        "'": "\u02bc",
        "\u02b9": "\u02bc"
    }
    return make_reps(reps, s)

def merge_r(s):
    reps = {
        "r": "ɾ"
    }
    return make_reps(reps, s)
    
def make_reps(reps, s):
    for k, v in reps.items():
        s = s.replace(k, v)
    return s

def replace_onset(reps, s, condition = lambda s : True):
    if len(s.split()) == 1 and condition(s):
        if s[0] in reps:
            s = s.replace(s[0], reps[s[0]], 1)
        return s
    elif not condition(s):
        return s
    return " ".join(replace_onset(reps, sub, condition) for sub in s.split())

def replace_coda(reps, s, condition = lambda s : True):
    if len(s.split()) == 1 and condition(s):
        if s[-1] in reps:
            s = s[::-1].replace(s[-1], reps[s[-1]][::-1], 1)[::-1]
        return s
    elif not condition(s):
        return s
    return " ".join(replace_coda(reps, sub, condition) for sub in s.split())

if __name__ == "__main__":
    main()