from getEntriesIds import get_entries_ids
from fillChoices import *
import string
import requests

# "https://docs.google.com/forms/d/e/1FAIpQLSctF47eV05W4YgwMU6mRvPts1gS-ZjbPjHc3loV1HuPN5Vnsg/viewform"
post_url = "https://docs.google.com/forms/d/e/1FAIpQLSctF47eV05W4YgwMU6mRvPts1gS-ZjbPjHc3loV1HuPN5Vnsg/formResponse"
filled_url = "https://docs.google.com/forms/d/e/1FAIpQLSctF47eV05W4YgwMU6mRvPts1gS-ZjbPjHc3loV1HuPN5Vnsg/viewform?usp" \
             "=pp_url&entry.1217452621=hello&entry.768380383=obaydah&entry.2093537409=bouifa "

entries = get_entries_ids(filled_url)

for x in entries:
    fill_choices(x, ''.join(random.choice(string.ascii_letters) for x in range(6)) + " " + ''.join(
        random.choice(string.ascii_letters) for x in range(6)))

x = requests.post(post_url, L)
print(x)
