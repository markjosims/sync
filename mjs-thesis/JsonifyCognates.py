import pandas as pd
import json

cognates_file = 'epps_cognate_database.csv'
json_file = 'epps_cognate_database.json'

def main():
    cognates_df = pd.read_csv(cognates_file, keep_default_na=False)
    data = []

    for _, row in cognates_df.iterrows():
        this_entry = dict(row)
        for key, val in this_entry.items():
            if key in ('gloss_pt', 'gloss_en'):
                continue
            this_entry[key] = {"lexeme": val}
        data.append(this_entry)
    
    json_obj = {
        "changelog": [],
        "data": data
    }

    with open(json_file, 'w', encoding='utf8') as outfile:
        json.dump(json_obj, outfile, indent=2, ensure_ascii=False)


    


if __name__ == "__main__":
    main()