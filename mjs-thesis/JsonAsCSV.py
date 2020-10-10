import pandas as pd
import json

json_file = "epps_cognate_database.json"
csv_file = "epps_cognate_database.csv"

def main():
    with open(json_file, 'r', encoding='utf8') as j_f:
        json_obj = json.load(j_f)

    df = pd.DataFrame(columns=[
        "gloss_pt", "gloss_en",
        "mbj_rc_m05", "mbj_rc_eppsob", "mbj_rn_m05",
        "daw_m05", "daw_eppsob", "daw_eppsob_pht",
        "hup_m05", "hup_ramepps", "hup_ramepps_pht",
        "yhp_m05", "yhp_silva", "yhp_silva_pht"
    ])

    for entry in json_obj['data']:
        row = {}
        for key, val in entry.items():
            if key in ('gloss_pt', 'gloss_en'):
                row[key] = val
            elif key in ('note', 'daw_orth_epps'):
                pass
            else:
                row[key] = val['lexeme']
                row[key+'_pht'] = val['pht']
        df.loc[len(df)] = row

    df.to_csv(csv_file, encoding='utf8', index=False)

    
    

if __name__ == "__main__":
    main()