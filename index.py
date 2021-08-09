import random

from getEntriesIds import *
from fillChoices import *
from logger import logging
import requests


def fill(url: str, filled_url: str, number_of_times: int, index_of_name=-1, index_of_phone=-1):
    post_url = generate_post_request_url(url)
    entries = get_entries_ids(filled_url)
    if index_of_name < -1 or index_of_phone < -1 or index_of_name >= len(entries) or index_of_phone >= len(entries):
        logging.error("index of name or index of phone is out of range")
        return
    if index_of_name != -1 and index_of_name == index_of_phone:
        logging.error(f"index of name == index of phone (value = {index_of_name})")
        return

    if index_of_name != -1:
        specify_name_entry(entries[index_of_name])
    if index_of_phone != -1:
        specify_phone_number_id(entries[index_of_phone])

    for x in entries:
        fill_choices(x, generate_random_list_of_strings(number_of_items=random.randint(1, 5)))
        # response = requests.post(post_url, get_random_choices())
        # print(response.status_code)

    logging.debug(f"{L}")
    logging.debug(f"{get_random_choices()}")
    logging.debug(f"name id index {index_of_name} phone index {index_of_phone}")
    logging.debug(f"name id : {get_name_id()} phone id : {get_phone_id()}")


################################
_url = "https://docs.google.com/forms/d/e/1FAIpQLSctF47eV05W4YgwMU6mRvPts1gS-ZjbPjHc3loV1HuPN5Vnsg/viewform"
_filled_url = "https://docs.google.com/forms/d/e/1FAIpQLSctF47eV05W4YgwMU6mRvPts1gS-ZjbPjHc3loV1HuPN5Vnsg/viewform?usp" \
              "=pp_url&entry.1217452621=hello&entry.768380383=obaydah&entry.2093537409=*bouifadene "

fill(_url, _filled_url, 1, 2, 2)
