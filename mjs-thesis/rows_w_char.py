in_file = 'epps_cognate_database.csv'
q = u'\u030c'

def main():
    with open(in_file, 'r') as f:
        lines = f.readlines()
    
    to_display = [line for line in lines if q in line]
    for line in to_display:
        print(line)
    print(len(to_display))
    
if __name__ == "__main__":
    main()