import random

FILEPATH = 'files/team-members.txt'


def get_all_members(filepath=FILEPATH):
    """
    Read a text file and return the list of all
    team members noted in team-members.txt
    """
    with open(filepath, 'r') as local_file:
        local_members = local_file.readlines()
    return local_members


def select_next_person(people_list):
    """
    :param people_list: list of team members
    :return: random selected person
    """
    next_person = random.choice(people_list)
    return next_person


if __name__ == "__main__":
    print("Hello from main!")

    members = get_all_members()
    print(members)
    print(select_next_person(members))
