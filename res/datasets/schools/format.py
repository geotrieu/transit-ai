import csv
import re
# uses csv and regex, maybe converting to a dict is better or something? not sure

with open("TDCSB_schools.csv","r") as f:
    with open("ARCGIS_format_TDCSB_schools.csv","w",newline='') as w:
        nf = csv.writer(w, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        d = csv.DictReader(f)
        for row in d:
            result = re.search('\((.*)\)', row["geometry"])
            print(result.group(1))
            nf.writerow([result.group(1).split(", ")[1],result.group(1).split(", ")[0]])