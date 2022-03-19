MONTHS = {"Januari" : "31",
            "Februari" : "28 of 29",
            "Maart" : "31",
            "April" : "31",
            "Mei" : "31",
            "Juni" : "31",
            "Juli" : "31",
            "Augustus" : "31",
            "September" : "31",
            "Oktober" : "31",
            "November" : "31",
            "December" : "31"}
maand = input("Geef de maand : ")
try:
    print(MONTHS[maand])
except:
    print("Fout")
