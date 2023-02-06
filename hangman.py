# hangman

from find_multi_occure_str import find_mul
import random
from movie_names import movie_names_func

class hangmn:
    def hang(self):
        print(''' 
        this is a hangman game, in this you need to guess the names of movies 
        so select the type of movies you want play with 
        enter
        1 - hollywood hits
        2 - marvel hits
        3 - bollywood hits
                ''')
        chose_type = str(input('enter the data: '))
        
        user_input = movie_names_func(chose_type)
        
        print('''
              here is your puzzle, All the best\n\n
              ''')

            
        chose_rand = random.choice(user_input)

        chose_random = chose_rand.lower()
        # chose_random = 'Thor: Ragnarok'
        # print(chose_random)

        for char in ['.', '@', ':', '-', '', '', '', ',']:
            if char in chose_random:
                chose_random = chose_random.replace(char, "")

        length_of_movie = len(chose_random)

        data_all = '_' * length_of_movie

        new_string = data_all
        if ' ' in chose_random:
            mul_data1 = find_mul(chose_random, ' ').get_list()

            for space in range(0, len(mul_data1)):
                item_in_space = mul_data1[space]
                new_string = new_string[0:item_in_space] + \
                    ' ' + new_string[item_in_space + 1:]

        else:
            new_string = data_all

        random_hint = random.choice(chose_random)

        output_str_hint = find_mul(chose_random, random_hint).get_list()
        # print(output_str)

        for m in range(len(output_str_hint)):
            n = output_str_hint[m]
            new_string = new_string[0:n] + random_hint + new_string[n+1:]

        print(new_string)
        print('\n')

        n = 1
        while n < 8:

            guess_digit = input(
                'Guess a letter to fill in the blanks : ').lower()

            if guess_digit == '':
                continue

            if guess_digit == chose_random:
                print('\nyou won \n')
                break

            guess_word = guess_digit[0]

            if guess_word in chose_random:
                print('\ngood one\n')

                output_str = find_mul(chose_random, guess_word).get_list()
                # print(output_str)

                for k in range(len(output_str)):
                    l = output_str[k]
                    new_string = new_string[0:l] + \
                        guess_word + new_string[l+1:]

                print('\n', new_string, '\n')

            else:
                print(f'\nwrong, you have {8-n} lives left\n')
                n = n+1

            if '_' not in new_string:
                print('\nyou won\n')
                break

            if n == 8 and '_' in new_string:
                print(f'\n you loose , the answer is {chose_random}\n')


obj = hangmn()
now_show = obj.hang()
