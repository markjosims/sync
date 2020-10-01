from standardize_chars import make_reps, basic_format, pipeline, replace_coda
from nasal_contours import prenasalized_onset, postnasalized_coda, preoralized_coda

def fix_mid_open(s):
    reps = {
        "e": "ɛ",
        "o": "ᴐ"
    }
    return make_reps(reps, s)

def fix_umlaut(s):
    reps = {
        "ë": "e",
        "ö": "o",
        "ä": "ә"
    }
    return make_reps(reps, s)

def glottal_stop_coda(s):
    reps = {
        "\u02bc": "ʔ"
    }
    condition = lambda s : len(s) < 2 or s[-2] not in 'pbtdcɟkg'
    return replace_coda(reps, s, condition)

def format_hup(s):
    return pipeline(s, [
        basic_format,
        fix_mid_open,
        fix_umlaut,
        prenasalized_onset,
        postnasalized_coda,
        glottal_stop_coda
    ])
    
def format_yhp(s):
    return pipeline(s, [
        basic_format,
        fix_mid_open,
        fix_umlaut,
        prenasalized_onset,
        preoralized_coda,
        glottal_stop_coda
    ])