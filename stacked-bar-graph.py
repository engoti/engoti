#Mod

import matplotlib.pyplot as engel

#VAR

labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')

index = (1, 2, 3, 4, 5)

web_usage = [20, 2, 5, 10, 14]

data_science_usage = [15, 8, 5, 15, 2]

games_usage = [10, 1, 5, 5, 4]


engel.bar(index, web_usage, tick_label=labels, label='web')

engel.bar(index, data_science_usage, tick_label=labels,
          label='data science', bottom=web_usage)

web_and_games_usage = [web_usage[i] + data_science_usage[i]
                       for i in range(0, len(web_usage))]

engel.bar(index, games_usage, tick_label=labels,
          label='games', bottom=web_and_games_usage)

engel.ylabel('Usage')
engel.xlabel('Programming Languages')
engel.legend()

engel.show()