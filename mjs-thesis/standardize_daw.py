from standardize_chars import basic_format, pipeline, make_reps
from nasal_contours import preoralized_coda, postoralized_onset

def format_vowels(s):
    reps = {
        "æ": "ɛ",
        "ʉ": "ɨ"
    }
    return make_reps(reps, s)

def format_daw(s):
    return pipeline(s, [
        basic_format,
        format_vowels,
        preoralized_coda,
        postoralized_onset
    ])