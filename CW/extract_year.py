import re
def extract_date(url):
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
url1= "https://www.rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date(url1))
