import json
from standardize_daw import format_daw
from standardize_hup_yhp import format_hup, format_yhp
from standardize_ndb import format_ndb_eppsob, format_ndb_m05
from standardize_chars import basic_format

cognates_file = 'epps_cognate_database.json'

def main():
    with open(cognates_file, 'r', encoding='utf8') as j_f:
        cognates = json.load(j_f)
    with open(cognates_file.replace('.json', 'BACKUP.json'), 'w', encoding='utf8') as j_f:
        json.dump(cognates, j_f, indent=2, ensure_ascii=False)

    for entry in cognates['data']:
        # nadëb
        entry['mbj_rc_eppsob']['pht'] = format_ndb_eppsob(entry['mbj_rc_eppsob']['lexeme'])
        entry['mbj_rc_m05']['pht'] = format_ndb_m05(entry['mbj_rc_m05']['lexeme'])
        entry['mbj_rn_m05']['pht'] = format_ndb_m05(entry['mbj_rn_m05']['lexeme'])

        # dâw
        entry['daw_eppsob']['pht'] = format_daw(entry['daw_eppsob']['lexeme'])
        entry['daw_m05']['pht'] = format_daw(entry['daw_m05']['lexeme'])

        # hup
        entry['hup_ramepps']['pht'] = format_hup(entry['hup_ramepps']['lexeme'])
        entry['hup_m05']['pht'] = basic_format(entry['hup_m05']['lexeme'])

        # yuhup
        entry['yhp_silva']['pht'] = format_yhp(entry['yhp_silva']['lexeme'])
        entry['yhp_m05']['pht'] = basic_format(entry['yhp_m05']['lexeme'])

    with open(cognates_file, 'w', encoding='utf8') as j_f:
        json.dump(cognates, j_f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()