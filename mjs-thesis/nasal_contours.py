from standardize_chars import replace_coda, replace_onset

not_nasal = lambda s: '\u0303' not in s

def preoralized_coda(s):
    reps = {
        "m": "bm",
        "n": "dn",
        "ɲ": "ɟɲ",
        "ŋ": "gŋ"
    }
    return replace_coda(reps, s, not_nasal)
        
def postoralized_onset(s):
    reps = {
        "m": "mb",
        "n": "nd",
    }
    return replace_onset(reps, s, not_nasal)

def prenasalized_onset(s):
    reps = {
        "b": "mb",
        "d": "nd",
    }
    return replace_onset(reps, s, not_nasal)

def postnasalized_coda(s):
    reps = {
        "b": "bm",
        "d": "dn",
        "ɟ": "ɟɲ",
        "g": "gŋ"
    }
    return replace_coda(reps, s, not_nasal)



