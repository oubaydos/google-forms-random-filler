import requests

from fillChoices import *
from getEntriesIds import *
from logger import logging


def fill(url: str, filled_url: str, number_of_times=1, index_of_name=-1, index_of_phone=-1):
    post_url = generate_post_request_url(url)
    entries = get_entries_ids(filled_url)
    if index_of_name < -1 or index_of_phone < -1 or index_of_name >= len(entries) or index_of_phone >= len(entries):
        logging.error("index of name or index of phone is out of range")
        return
    if index_of_name != -1 and index_of_name == index_of_phone:
        logging.error(f"index of name == index of phone (value = {index_of_name})")
        return
    for x in entries:
        fill_choices(x,
                     generate_random_list_of_strings(number_of_items=random.randint(1, 5)),
                     entries[index_of_name] if index_of_name != -1 else "",
                     entries[index_of_phone] if index_of_phone != -1 else ""
                     )
    for i in range(number_of_times):
        logging.debug(f"{get_random_choices()}")
        response = requests.post(post_url, get_random_choices())
        if response.status_code == 200:
            logging.debug(f"{response.status_code}")
        else :
            logging.warning(f"{response.status_code}")


################################

