import requests
import json
import os




search = "i didn't know"





r = requests.get("https://www.youtube.com/results?search_query=" + search)

t = r.text

t = t.split('var ytInitialData = ')[1].split("window.ytcsi.tick('pdr', null, '');")[0].split('</script>')[0][:-1]

j = json.loads(t)

x = open('file.txt', 'w')
x.write(t)
x.flush()
x.close()

nCanz = len(j['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'])


for i in range(21):
    
    if nCanz < 10:
        try:
            primaCanzone = j['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][1]['itemSectionRenderer']['contents'][i]['videoRenderer']['title']['runs'][0]['text']
            linkVideo = 'https://www.youtube.com/watch?v='+j['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][1]['itemSectionRenderer']['contents'][i]['videoRenderer']['videoId']
        except KeyError:
            continue
    else:
        try:
            primaCanzone = j['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][i]['videoRenderer']['title']['runs'][0]['text']
            linkVideo = 'https://www.youtube.com/watch?v='+j['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][i]['videoRenderer']['videoId']
        except KeyError:
            continue

    print(primaCanzone + '        Link --> ' + linkVideo)

    
    

    


