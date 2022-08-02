import requests


# function uses wikipedia api to get the wiki page of the celeb
def get_page(nameTo):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "prop": "revisions",
        "titles": nameTo,
        "rvprop": "content",
        "rvslots": "*",
        "formatversion": "2",
        "format": "json"
    }

    r = requests.get(url=url, params=params)
    jsonData = r.json()

    # using pageid to check if the celeb page was found
    if "pageid" not in jsonData["query"]['pages'][0].keys():
        print("This is no celeb! (or we just didn't found someone with that name)")   
    else:
        data = jsonData["query"]['pages'][0]["revisions"][0]["slots"]["main"]['content'].split('\n| ') # getting the content of the page as list
        if is_dead(data):
            print('He is dead and gone')
        else:
            print('Still alive and kicking')


# checking wiki page to check if the celeb is dead
def is_dead(dataToCheck):
    for line in dataToCheck:
        if 'death_date' in line: # checking if death_date exsit and not empty
            if len(line.split('= ')[1]) > 0:
                return True
    return False


def main():
    namey = input("Enter celeb full name to check if she/he/it still alive: ")
    if 'jackal' in namey.lower():
        print('The Jackal will live for ever!')
    else:
        checkName = False
        while checkName == False: # while loop to make sure the name is enterd correctly
            try:
                celebName = namey.split(' ')[0].capitalize() + ' ' + namey.split(' ')[1].capitalize()
                checkName = True
            except:
                namey = input("Please enter a valid first and last name separated with space: ")
        get_page(celebName)


if __name__ == "__main__":
    main()
