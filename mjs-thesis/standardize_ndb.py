from standardize_chars import make_reps, basic_format, pipeline
from nasal_contours import preoralized_coda

# Nadëb Rç Epps & Obert
def fix_digraphs(s):
    reps = {
        "ts": "c",
        "ng": "ŋ",
        "nh": "ɲ"
    }
    return make_reps(reps, s)

def fix_umlauted_vowels(s):
    reps = {
        "ä": "ʌ",
        "ë": "ә",
        "ÿ": "?",
        "a\u0308": "ʌ",
        "e\u0308": "ә",
        "y\u0308": "?"
    }
    return make_reps(reps, s)

def fix_acute_vowels(s):
    reps = {
        "é": "ɛ",
        "ó": "ᴐ",
        "e\u0301": "ɛ",
        "o\u0301": "ᴐ"
    }
    return make_reps(reps, s)
    
def y_as_ibar(s):
    reps = {
        "y": "ɨ",
         "ỹ": "ɨ\u0303"
    }
    return make_reps(reps, s)

def digraph_as_long(s):
    oral_vowels = [
        "i", "y", "u",
        "e", "ÿ", "ë", "o",
        "é", "ä", "ó",
        "a"
    ]
    vowels = oral_vowels[:]
    vowels.extend(v+'\u0303' for v in oral_vowels)
    reps = {vowel+vowel: vowel+':' for vowel in vowels}
    return make_reps(reps, s)

def format_ndb_eppsob(s):
    return pipeline(s, [
        basic_format,
        digraph_as_long,
        fix_digraphs,
        fix_umlauted_vowels,
        fix_acute_vowels,
        y_as_ibar,
        preoralized_coda
    ])
    

# Nadëb Rç, Rn Martins
def remove_echo_vowel(s):
    reps = {
        "ɾә": "ɾ", 
        "ɾɵ": "ɾ"
    }
    return make_reps(reps, s)

def fix_j(s):
    reps = {
        "ʝ": "j"
    }
    return make_reps(reps, s)

def format_ndb_m05(s):
    return pipeline(s,[
        basic_format,
        remove_echo_vowel,
        fix_j
    ])