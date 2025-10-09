a = input().split(" ")

list = []
for i in a:
    first = a[0]
    last = a[-1]
    medium = a[1]

dict = {
    "JAN": "01", "FEB": "02", "MAR": "03", 
    "APR": "04", "MAÍ": "05", "JÚN": "06", 
    "JÚL": "07", "ÁGÚ": "08", "SEP": "09", 
    "OKT": "10", "NÓV": "11", "DES": "12"
}

month = dict[medium]

print(f"20{last}-{month}-{first}")