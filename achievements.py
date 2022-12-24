import csv
from plyer import notification
achievements_file = 'achievements.csv'

# this will be copied in the for loop to create new dict for each new line from the csv file
new_dict = {'condition-kanji': 'None', 'name': 'None', 'status': 'None'}
new_list = []
count_rows = 1

# name of columns in the csv file
header1 = 'condition-kanji'
header2 = 'name'
header3 = 'status'


def get_achievement(answer_from_menu):
    global count_rows
    true_false_check = ''
    # open file, read data from it, create one new dict for each line and append them to the list
    with open(achievements_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            count_rows += 1
            new_dict_copy = new_dict.copy()
            for i in range(1, count_rows):
                new_dict_copy['condition-kanji'] = row['condition-kanji']
                new_dict_copy['name'] = row['name']
                new_dict_copy['status'] = row['status']
            new_list.append(new_dict_copy)
    # iterate over the list to check values and get the achievement(or tell it's already achieved)
    for i in new_list:
        for k, p in i.items():
            if p in answer_from_menu and i['status'] != 'True':
                i['status'] = 'True'
                notification.notify(title='Congratulations, achievement unlocked!', message=f"Achievement - {i['name']} unlocked with {answer_from_menu}", timeout=5)
                true_false_check = True
            else:
                break
    # write updated info into the same file. to make sure same achievement won't be achieved twice
    if true_false_check == True:
        with open(achievements_file, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([header1, header2, header3])
            for data in new_list:
                writer.writerows([[data['condition-kanji'], data['name'], data['status']]])
    true_false_check = ''
    new_list.clear()

def score_related_achievements(current_score):
    with open('achievements with digits.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['digit']) == int(current_score):
                notification.notify(title='Congratulations, achievement unlocked!',
                                    message=f"Achievement - {row['name']}, correct answers was given - {current_score}",
                                    timeout=5)
