echo "# Module-2-Lesson-4-Assignment-Python-Loop-Statements" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/swlancas7/Module-2-Lesson-4-Assignment-Python-Loop-Statements.git
git push -u origin main

## Module 2 Lesson 4: Range Riddle

mood = ['Loopy', 'Sad', 'Melancholy', 'Happy', 'Frustrated', 'Angry']
day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for mood in day:
    print("My mood is now "[mood])

import random
mood = ['Loopy', 'Sad', 'Melancholy', 'Happy', 'Frustrated', 'Angry']
print (mood)


# Module 2 Lesson 4: Double Scoops With Nested Loops
mood = ['Loopy', 'Sad', 'Melancholy', 'Happy', 'Frustrated', 'Angry']
time_of_day = ['Morning', 'Afternoon', 'Evening']
day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


while True:
    for mood in time_of_day in day:
        print("My mood is now "{mood})

import random
mood = ['Loopy', 'Sad', 'Melancholy', 'Happy', 'Frustrated', 'Angry']
    print (mood)
