# •Write a program which downloads file from the Internet
# •If you try and download a very large file then how do you monitor the progress?
# •Research on urllib.urlretrieve() to solve this problem

import urllib.request
from urllib.error import URLError, HTTPError 
import os

# Lai palaistu šo programmu, NAV jāaktivizē virtuālā vide

# 1 - url failam, ko lejupielādēšu:
url = "https://www.booking.com/searchresults.html?"
# url = "https://www.data.gov/"
# url = "https://data.worldbank.org/indicator/..."
# url = "https://www2.census.gov/programs-surveys/acs/summary_file/" 

# 2 - fails, kur tiks saglabāti dati no lejupielādējamā faila
downloadedInformation = "downloaded_file_a)b)c).txt"

# 6 - funkcija, kas uzrauga lejupielādēšanas progresu
def monitorTheProgress(numberOfBlocks, blockSize, totalSize): 
    downloaded = numberOfBlocks * blockSize
    if totalSize > 0: 
        downloadedPercent = (downloaded /totalSize)  * 100  # cik procenti ir lejupielādējušies
        print("\nDownloading: {:.2f}% ({}/{} bytes)".format(downloadedPercent, downloaded, totalSize), end="")
    else: # ja atbildē nav kopējo satura lielums ("Content-Length"), kas nevienmēr ir, tad pēc noklusējuma totalSize vērtība ir -1
        print("\nDownloading: {} bytes".format(downloaded), end="") # atgriež, cik baiti ir lejupielādēti
    
# 3 - funkcija, kas izvada lejupielādējamā faila izmēru un lejupielādē failu
def downloadFile(url, downlInformation):
    # 4 - tiek veikts pieprasījums un atvērta saite
    try:
        res = urllib.request.urlopen(url)
        # if res.getcode() == 200: # ja status ir 200 (ir izdevies pierpasījums) bet tā kā ir tr-except, tad šo nevajag

        # 5 -  pirmkārt, tiek veikta faila lejupielāde ar urlretrieve failā downlInformation = ("downloaded_file_a)b)c).txt"), 
        # un, otrkārt, ar reporthook tiek uzraudzīts lejupielādes progress
        urllib.request.urlretrieve(url, downlInformation, reporthook=monitorTheProgress)
        print("\nFile downloaded successfully!")

        # ja nebūtu try-except, tas šos vajadzētu:
        # elif res.getcode == 404: # ja ir neizdevies pieprasījums; faila lejupielāde netiek veikta
        #     print("404 Not Found. File does not exist.")
        # else:
        #     print("Unexpected Status Code: {}.".format(res.getcode))

    except Exception as e:
        print("Error: {}".format(e))

downloadFile(url, downloadedInformation)