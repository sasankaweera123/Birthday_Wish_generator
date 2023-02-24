import data
import random
from csv import writer
import enchant

data = data.Data('wish.csv')


def generate_gender_specific_random(n, gender):
    random_row = []
    random_value = []

    # Get the generated random row
    for i in range(0, n):
        random_value.append(random.randint(0, data.get_row_count()-1))
        random_row.append(data.get_row(random_value[i]))
        # check the gender of the random row
        if str(random_row[i].Gender) == gender:
            print(random_row[i].Wish)
        if str(random_row[i].Gender) == "B":
            print(random_row[i].Wish)


def generate_random_wish(n):
    random_row = []
    random_value = []

    # Get the generated random row
    for i in range(0, n):
        random_value.append(random.randint(0, data.get_row_count()-1))
        random_row.append(data.get_row(random_value[i]))
        print(random_row[i].Wish)


def add_wish(wish,gender):

    if not search_wish(wish):

        if check_words_in_wish(wish):

            values = [data.get_row_count()+1, wish, gender]

            with open('wish.csv', 'a') as f:
                csv_writer = writer(f)
                csv_writer.writerow(values)
                f.close()
        else:
            print("Invalid wish")
    else:
        print("Wish already exists")


def get_wish():
    value = random.randint(0, data.get_row_count()-1)
    return data.get_row(value).Wish


def check_words_in_wish(wish):
    c = True
    d = enchant.Dict("en_US")
    words = wish.split()
    for word in words:
        if not d.check(word):
            c = False
            break
    return c


def search_wish(wish):
    if data.search_data("Wish", wish) is not None:
        return True


def main():

    generate_gender_specific_random(3, "M")
    # add_wish("Sending you my prayers and wishes on your special day. Happy birthday.", "B")


if __name__ == "__main__":
    main()
