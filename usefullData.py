import random
import string


# import os
# import requests
# import json
# params = dict()
# headers = dict()
# url = "https://randommer.io/api/Phone/Generate"
# # url = "https://randommer.io/api/Name"
#
# # params["nameType"]="fullname"
#
# params["CountryCode"]="ma"
#
# params["Quantity"]=100
# headers["X-Api-Key"]=os.environ['X_API_KEY']
#
# x = requests.get(url,params=params,headers=headers)
# if not str(x.status_code).startswith("2"):
#     print(x.content)
#     print(x.status_code)
#     exit(1)
# print(x)
# L = json.loads(x.content.decode('UTF-8'))
# print(L,type(L),sep='\n')
def generate_random_list_of_strings(alphabet=string.ascii_letters, number_of_characters=-1, number_of_items=1):
    """generates a list of random strings :
    :param :
        alphabet: alphabet to base on when generating the strings list
            default: ascii letters
        number of characters: number of characters for the generated strings
            default: random number between 1 and 39
        number of items: length of returned list
            default: 1
    """
    if number_of_characters < -1:
        print("number of characters is not a positive integer")
        return generate_random_list_of_strings(alphabet, -1, number_of_items)
    if number_of_items < 1:
        print("number of items is not a positive integer")
        return generate_random_list_of_strings(alphabet, number_of_characters, 1)
    L = []
    for i in range(number_of_items):
        L.append(
            ''.join(random.choice(string.ascii_letters) for _ in
                    range(number_of_characters / 2 if number_of_characters != -1 else random.randint(1, 20))) + ' ' +
            ''.join(random.choice(string.ascii_letters) for _ in
                    range(number_of_characters / 2 if number_of_characters != -1 else random.randint(1, 20)))
        )
    # for i in L:

    return L


"""already generated random names list && random phone numbers list"""
random_names = ['Adnan Desimone', 'Jamiya Barbee', 'Lennox Mckinley', 'Siana Shiver', 'Marie Mcdermott',
                'Landry Mccollum', 'Zaniyah Dugan', 'Nicodemus Norvell', 'Lou Partlow', 'Khari Omeara', 'Deion Seeley',
                'Nilah Wickham', 'Darron Comfort', 'Emir Montero', 'Kaitlyn Hodges', 'Cori Vail', 'Lesley Crutchfield',
                'Lelani Desalvo', 'Soliana Monge', 'Grahm Dufrene', 'Justice Hanna', 'Daniyal Matt', 'Franky Ricciardi',
                'Eddy Farrow', 'Geremiah Marvel', 'Asiel Tarrant', 'Jorge Goodwin', 'Anden Alder', 'Blake Gould',
                'Emorie Marlowe', 'Bladen Cofield', 'Ramses Desantis', 'Briza Metts', 'Ani Olguin', 'Rileigh Tavares',
                'Kristel Merz', 'Kayana Villalba', 'Sol Fries', 'Branson Otto', 'Caylin Deck', 'Quin Rubalcava',
                'Louisa Quiroz', 'Blimy Mcglothlin', 'Bowman Child', 'Calvin Powers', 'Reyli Karns', 'Callie Chang',
                'Maliha Gabel', 'Shaun Castle', 'Nawal Judkins', 'Edison Helton', 'Jessiah Samson', 'Kelani Cunha',
                'Koby Blaylock', 'Luka Livesay', 'Milani Rouse', 'Aster Lammers', 'Ori Pabon', 'Becker Carlyle',
                'Wilton Ullman', 'Niah Upshaw', 'Kynlee Gregg', 'Treysen Kujawa', 'Spencer Michaels', 'Carlin Crew',
                'Yohanna Propst', 'Nicolette Benavidez', 'Jaceyon Mallard', 'Abdallah Batiste', 'Moshe Starr',
                'Tayden Landrum', 'Linken Melgoza', 'Maddalena Reidy', 'Twyla Pasillas', 'Meadow Weston', 'Jamier Bost',
                'Kamiah Palermo', 'Mister Llanes', 'Zya Fore', 'Carolina Benton', 'Jediah Markowski', 'Lilyann Hamby',
                'Ahmir Dennison', 'Kamille Grubbs', 'Elif Bentz', 'Jafet Woodbury', 'Aariv Zamarripa', 'Raymond Solis',
                'Cordelia Brand', 'Amaan Dewberry', 'Aydin Epps', 'Conley Tijerina', 'Taim Gastelum', 'Carmello Beeson',
                'Gunner Carrillo', 'Kota Maroney', 'Nevaeh Moreno', 'Vaughn Omalley', 'Aarush Hogue', 'Achilles Sauer'
                ]

random_phone_numbers = ['+212 767-082922', '+212 681-608093', '+212 711-072420', '+212 767-088651', '+212 702-261267',
                        '+212 681-353435', '+212 702-795855', '+212 689-190680', '+212 687-641017', '+212 711-979642',
                        '+212 627-943241', '+212 684-452182', '+212 709-980088', '+212 701-705859', '+212 677-888741',
                        '+212 771-382902', '+212 689-185652', '+212 644-791447', '+212 699-505744', '+212 687-814828',
                        '+212 681-314813', '+212 712-233134', '+212 681-439839', '+212 696-510872', '+212 681-796529',
                        '+212 684-739701', '+212 619-155297', '+212 777-605583', '+212 649-395777', '+212 775-429218',
                        '+212 689-599170', '+212 708-342463', '+212 696-679443', '+212 707-736316', '+212 682-313557',
                        '+212 681-081112', '+212 689-638519', '+212 678-248324', '+212 688-992384', '+212 680-274993',
                        '+212 702-836153', '+212 681-091303', '+212 704-322354', '+212 672-040192', '+212 710-203285',
                        '+212 684-132535', '+212 688-153126', '+212 711-322795', '+212 688-319034', '+212 681-407095',
                        '+212 641-436061', '+212 687-407522', '+212 712-915597', '+212 762-232812', '+212 712-801003',
                        '+212 687-873868', '+212 775-608824', '+212 682-065708', '+212 711-080538', '+212 702-425408',
                        '+212 771-286368', '+212 652-244301', '+212 761-479521', '+212 659-133892', '+212 710-189626',
                        '+212 761-075816', '+212 681-876810', '+212 684-308216', '+212 701-969823', '+212 687-259440',
                        '+212 682-307070', '+212 774-728140', '+212 710-070686', '+212 767-858485', '+212 762-518025',
                        '+212 704-859911', '+212 693-911139', '+212 712-543058', '+212 615-519885', '+212 630-579981',
                        '+212 681-765909', '+212 767-148216', '+212 648-577914', '+212 770-492820', '+212 681-571327',
                        '+212 700-417083', '+212 682-369356', '+212 656-918571', '+212 689-316658', '+212 761-758467',
                        '+212 712-285179', '+212 767-807670', '+212 711-124781', '+212 681-153665', '+212 711-655675',
                        '+212 681-802047', '+212 689-753071', '+212 689-057828', '+212 711-872553', '+212 702-656390']
