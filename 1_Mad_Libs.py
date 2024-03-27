print("\nThis Madlibs is inspired by Mad Lib Theater with Benedict Cumberbatch on The Tonight Show Starring Jimmy Fallon.")

male_name = input("\nMale name: ")
fav_teacher = input("Name of your favorite teacher(Add Ms or Mr): ")
exclamation = input("Exclamation: ")
number = input("Number: ")
plural_obj = input("Plural object: ")
store_name = input("Store name: ")
body_part = input("Body part: ")
silly_word = input("Silly word: ")
holiday_name = input("Name of a holiday: ")
movie = input("Movie title: ")
verb_ing = input("Verb ends with -ing: ")
distance = input("Amount of distance(Add m, cm, mm, etc.): ")
country = input("A country: ")
animal = input("Animal: ")
famous_quote = input("Famous movie quote: ")
body_part_2 = input("Another body part: ")
children_song = input("Children song: ")
adj = input("Adjective: ")

mad_libs = f"\n\nBenedict: Hello, I'm detective {male_name}. And you are? \
\nJimmy: {fav_teacher}. \
\nBenedict: You're here today under the suspicion of a Second-degree robbery. \
\nJimmy: {exclamation}! \
\nBenedict: That's right. {number} {plural_obj} was stolen from {store_name}. And the crime scene has your {body_part} written all over it. \
\nJimmy: That is {silly_word}! \
\nBenedict: Where were you on the night of {holiday_name}? \
\nJimmy: We were watching {movie}. \
\nBenedict: Then why the security camera footage show you {verb_ing} just {distance} away from the crime scene? \
\nBenedict: Alright. Alright. I'm full with playing games. Where are you from? \
\nJimmy: {country}. \
\nBenedict: Yeah. Just as I suspected. \
\nDo you know one of the best part about being a detective is that I get to lock up criminals like you and go home to my children and my pet {animal}. \
\nAnd say {famous_quote}! \
\nJimmy: Fine, I did this. I committed the robbery. But I only did this because i needed the money to buy myself {body_part_2} implant. \
\nBenedict: I knew it all along. I knew it all along! And everytime I saw a crime, I'd like to sing my favorite song {children_song}. \
\nJimmy: You have a {adj} voice. I LOVE YOU. \
\n\nEND SCENE\n"

print(mad_libs)