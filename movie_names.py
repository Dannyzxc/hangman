def movie_names_func(chose_type):

    hollywood_movies = ['The Shawshank Redemption', 'The Godfather',  'The Dark Knight',  "Schindler's List", 'Pulp Fiction', 'The Lord of the Rings: The Return of the King', 'The Good, the Bad and the Ugly', 'The Lord of the Rings: The Fellowship of the Ring', 'The Lord of the Rings: The Two Towers', 'Forrest Gump', 'Inception', 'The Matrix', 'Goodfellas', "One Flew Over the Cuckoo's Nest", 'Seven Samurai', 'Se7en', 'City of God', 'The Silence of the Lambs', "It's a Wonderful Life", 'Life is Beautiful', 'The Usual Suspects', 'Spirited Away', 'Saving Private Ryan', 'American History X', 'Interstellar', 'The Green Mile', 'The Prestige', 'The Intouchables', 'Whiplash', 'The Lion King', 'The Pianist', 'Terminator', 'Back to the Future', 'Raiders of the Lost Ark', 'Psycho', 'Rear Window', 'Modern Times', 'City Lights', 'The Shining', 'Apocalypse Now', 'Alien', 'Memento','Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb', 'Sunset Boulevard', 'Grave of the Fireflies',  'The Great Dictator', 'Cinema Paradiso', 'The Lives of Others', 'Once Upon a Time in the West', 'Das Boot', 'A Clockwork Orange', 'The Dark Knight Rises', 'Paths of Glory', 'Spirited Away', 'The Treasure of the Sierra Madre', 'Eternal Sunshine of the Spotless Mind', 'Full Metal Jacket', 'Amadeus', 'Lawrence of Arabia', 'Taxi Driver', 'Double Indemnity', 'Casablanca', 'Some Like It Hot', 'North by Northwest', 'Rear Window', 'Vertigo', 'The Birds', 'Psychof', 'Notorious', 'Rope', 'Dial M for Murder', 'To Catch a Thief', 'The Man Who Knew Too Much', 'North by Northwest', 'The Trouble with Harry', 'Vertigo', 'Psycho', 'The Birds', 'Marnie', 'Torn Curtain', 'Frenzy', 'Family Plot', 'Rear Window', 'Vertigo', 'Psycho', 'The Birds', 'Marnie', 'Torn Curtain', 'Frenzy', 'Family Plot']

    marvel_movies = ["Iron Man",    "The Incredible Hulk",    "Iron Man 2",    "Thor",    "Captain America: The First Avenger",    "The Avengers",    "Iron Man 3",    "Thor: The Dark World",    "Captain America: The Winter Soldier",    "Guardians of the Galaxy",    "Avengers: Age of Ultron",    "Ant-Man",    "Captain America: Civil War",    "Doctor Strange",    "Guardians of the Galaxy Vol. 2",    "Spider-Man: Homecoming",    "Thor: Ragnarok",    "Black Panther",    "Avengers: Infinity War",    "Ant-Man and The Wasp",    "Captain Marvel",    "Avengers: Endgame",    "Spider-Man: Far From Home","Black Widow",    "Eternals",    "Shang-Chi and The Legend of the Ten Rings",    "Doctor Strange in the Multiverse of Madness",    "Thor: Love and Thunder",    "Blade",    "X-Men",    "X2: X-Men United",    "X-Men: The Last Stand",    "X-Men Origins: Wolverine",    "X-Men: First Class",    "The Wolverine",    "X-Men: Days of Future Past",    "Deadpool",    "X-Men: Apocalypse",    "Logan",    "Deadpool 2",    "Dark Phoenix",    "The New Mutants",    "Spider-Man: Into the Spider-Verse",    "Iron Fist",    "Luke Cage",    "Daredevil",    "Jessica Jones",   "The Defenders",        "The Punisher", ]

    bollywood_movies = ["Dil Chahta Hai","Rang De Basanti",
                        "PK",
                        "Zindagi Na Milegi Dobara",
                        "Kal Ho Naa Ho",
                        "Dilwale Dulhania Le Jayenge",
                        "Ae Dil Hai Mushkil",
                        "Devdas",
                        "Koi Mil Gaya",
                        "Mera Naam Joker",
                        "Sholay",
                        "Deewar",
                        "Anand",
                        "Mughal-e-Azam",
                        "Guide",
                        "Hum Aapke Hain Koun",
                        "Lagaan",
                        "Dil Se",
                        "Baghban",
                        "Sultan",
                        "PK",
                        "Dhoom 3",
                        "3 Idiots",
                        "Mera Naam Joker",
                        "Swaroop",
                        "Talaash",
                        "Kabhi Kabhie",
                        "Chandni",
                        "Trishul",
                        "Dil To Pagal Hai",
                        "Mela",
                        "Baazigar",
                        "Main Hoon Na",
                        "Koi Mil Gaya",
                        "Kal Ho Naa Ho",
                        "Veer-Zaara",
                        "Bunty Aur Babli",
                        "Rang De Basanti",
                        "Dil Chahta Hai",
                        "Salaam Namaste",
                        "Jab We Met",
                        "Love Aaj Kal",
                        "Yeh Jawaani Hai Deewani",
                        "2 States",
                        "Kapoor & Sons",
                        "Udta Punjab",
                        "Dear Zindagi",
                        "Badlapur",
                        "Tamasha",
                        "PK",
                        "Queen",
                        "Haider",
                        "Bajrangi Bhaijaan",
                        "Sultan",
                        "Dangal",
                        "PK",
                        "Secret Superstar",
                        "Padmaavat",
                        "Pad Man",
                        "Andhadhun",
                        "Stree",
                        "Dream Girl",
                        "Bala",
                        "Good Newwz",
                        "Angrezi Medium",
                        "Ludo",
                        "Panga",
                        "Tanhaji: The Unsung Warrior",
                        "Chhapaak",
                        "Thappad",
                        "Gulabo Sitabo",
                        "Shakuntala Devi",
                        "Sooryavanshi",
                        "83",
                        "Brahmastra",
                        "Coolie No. 1",
                        "Bell Bottom",
                        "Laxmmi Bomb",
                        "Sadak 2",
                        "The Big Bull",
                        "Shakuntala Devi",
                        "Ludo",
                        "Bhoot Part One: The Haunted Ship",
                        "Gunjan Saxena: The Kargil Girl"
                        ]

    if chose_type == '1':
        data = hollywood_movies
    elif chose_type == '2':
        data = marvel_movies

    elif chose_type == '3':
        data = bollywood_movies
    else:
        print('invalid input, try again')
        print(''' 
        this is a hangman game, in this you need to guess the names of movies 
        so select the type of movies you want play with 
        enter input
        1 - hollywood hits
        2 - marvel hits
        3 - bollywood hits
                ''')
        chose_type = str(input('enter the data: '))

        movie_names_func(chose_type)

    return data
