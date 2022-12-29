import os , random

for i in range(365):
    d = f'{str(i)} Days Ago'
    rand = random.randrange(1, 12)
    with open('data.txt','a') as file:
        file.write(d+'\n')
    os.system('git add data.txt')
    os.system(f'git commit --date=" 2021-{rand}-{d}" -m 1')
os.system('git push -u origin main')