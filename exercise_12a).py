# •Write a program which downloads file from the Internet

import requests # strādā kad activate virt.env.

# Lai palaistu šo programmu, ir jāaktivizē virtuālā vide: source venv/bin/activate

# 1 - url failam, ko lejupielādēšu:
url = 'https://www.data.gov/'

# 2 - fails, kur tiks saglabāti dati no lejupielādējamā faila
downloadedInformation = "downloaded_file_a).txt"

# 3 - uz norādīto url tiek nosūtīts pieprasījums "GET", kurš atgirež rezultātu
response = requests.get(url)

# 4 - funkcija, kas veic faila lejupielādi
def downloadFile(res, downlInformation):
    if res.status_code == 200: # ja status ir 200 (ir izdevies pierpasījums)
        file = open(downlInformation, "wb") # wb - atveru failu rakstīšanai ar binārajiem datiem
        file.write(res.content) # failā tiek ieraktīts lejupieladējamais rezultāts
        # print(response.text) # izdrukā tekstu terminālī
        print("File downloaded successfully!")
    elif res.status_code == 404: # ja ir neizdevies pieprasījums; faila lejupielāde netiek veikta
        print("404 Not Found. The requested file does not exist.")
    else:
        print(f"Unexpected Status Code: {res.status_code}")

downloadFile(response, downloadedInformation)