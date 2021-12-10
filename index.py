import requests

from fillChoices import *
from getEntriesIds import *
from logger import logging


def fill(url: str, filled_url: str, possibilities: list, number_of_times=1, index_of_name=-1, index_of_phone=-1):
    post_url = generate_post_request_url(url)
    entries = get_entries_ids(filled_url)
    if index_of_name < -1 or index_of_phone < -1 or index_of_name >= len(entries) or index_of_phone >= len(entries):
        logging.error("index of name or index of phone is out of range")
        return
    if index_of_name != -1 and index_of_name == index_of_phone:
        logging.error(f"index of name == index of phone (value = {index_of_name})")
        return
    counter = -1
    for x in entries:
        counter += 1
        fill_choices(x,
                     possibilities[counter],  # generate_random_list_of_strings(number_of_items=random.randint(1, 5))
                     entries[index_of_name] if index_of_name != -1 else "",
                     entries[index_of_phone] if index_of_phone != -1 else ""
                     )
    for i in range(number_of_times):
        logging.debug(f"{get_random_choices()}")
        response = requests.post(post_url, get_random_choices())
        if response.status_code == 200:
            logging.debug(f"{response.status_code}")
        else:
            logging.warning(f"{response.status_code}")


def get_list_of_lists_of_possibilities(*possibilities_lists):
    return [i for i in possibilities_lists]


def scan():
    url = input("enter the link of the form : ")
    filled_url = input("enter the prefilled link of the form : ")
    number_of_entries = len(get_entries_ids(filled_url))
    logging.debug(f"number of entries : {number_of_entries}")
    poss_list = []
    for i in range(number_of_entries):
        print("--------------------------------")
        n = int(input(f"enter the number of possibilities you will be entering for this entry {i + 1} : "))
        print("----possibilities : ------------")
        temp_list = []
        for j in range(n):
            temp_var = input(f"enter the {j + 1}th possibility : ")
            temp_list.append(temp_var)
        poss_list.append(temp_list)
    d = dict()
    d["url"] = url
    d["filled_url"] = filled_url
    d["possibilities"] = poss_list
    number_of_times = int(input("-----------------\nenter the number of times you wish the form to be filled : "))
    d["number_of_times"] = number_of_times
    return d


def main():
    url = "https://docs.google.com/forms/d/e/1FAIpQLSctF47eV05W4YgwMU6mRvPts1gS-ZjbPjHc3loV1HuPN5Vnsg/viewform?usp=sf_link"
    filled_url = "https://docs.google.com/forms/d/e/1FAIpQLSctF47eV05W4YgwMU6mRvPts1gS-ZjbPjHc3loV1HuPN5Vnsg/viewform?usp=pp_url&entry.1217452621=test+temp&entry.768380383=test&entry.2093537409=test"
    # cours_possibilities = ["react", "node", "js", "python", "java", "selenium"]
    # prof_possibilities = ["hamlaoui", "hachimi", "elfkihi", "elasri", "ettalbi", "tabii"]
    # fill(url, filled_url,
    #      possibilities=get_list_of_lists_of_possibilities(random_names, cours_possibilities, prof_possibilities),
    #      number_of_times=200)
    d = scan()
    fill(d["url"], d["filled_url"], possibilities=d["possibilities"], number_of_times=d["number_of_times"])


if __name__ == '__main__':
    main()
