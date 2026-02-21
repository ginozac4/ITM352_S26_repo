celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd", "Keanu Reeves", "Angelina Jolie")
ages = (36, 28, 26, 61, 50)

celebs_list = []
ages_list = []

for celeb in celebs:
    celebs_list.append(celeb)

ages_list = [age for age in ages]

celebs_dict = {"Celebrities": celebs_list, "Ages": ages_list}

print(celebs_dict)