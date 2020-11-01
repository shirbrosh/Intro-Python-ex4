import hangman_helper

CHAR_A = 97
CHAR_Z = 122


def update_word_pattern(word, pattern, letter):
    """A function that receives a word, the current pattern and a letter and
    returns the updated pattern containing the letter in the suitable location
    according to the word """
    if letter not in word:
        return pattern
    else:
        new_pattern = ""
        for i in range(0, len(word)):
            if word[i] == letter:
                new_pattern = new_pattern + letter
            else:
                new_pattern = new_pattern + pattern[i]
        return new_pattern


def run_single_game(words_list):
    """A function that receives a list of words, randomly choosing one and runs
    the game 'hangman' on the chosen word:"""
    word = hangman_helper.get_random_word(words_list)
    pattern = "_" * len(word)
    wrong_guess_list = []
    msg = hangman_helper.DEFAULT_MSG
    num_errors = 0
    while num_errors < hangman_helper.MAX_ERRORS and pattern != word:
        # a loop that will run until the gamer had manged to discover the word
        # or had made too many mistakes
        hangman_helper.display_state(pattern, num_errors, wrong_guess_list,
                                     msg)
        input1 = hangman_helper.get_input()
        chosen_letter = input1[1]
        if input1[0] == hangman_helper.LETTER:
            # checks if the gamer entered a letter
            if len(chosen_letter) != 1 or not chosen_letter.islower():
                # checks if the chosen letter is valid
                msg = hangman_helper.NON_VALID_MSG
                continue
            elif chosen_letter in wrong_guess_list or chosen_letter in pattern:
                # checks if the chosen letter has already been used
                msg = hangman_helper.ALREADY_CHOSEN_MSG + chosen_letter
            elif chosen_letter in word:
                # checks if the chosen letter is in the word, which means we
                # want to put her in the pattern
                pattern = update_word_pattern(word, pattern, chosen_letter)
                msg = hangman_helper.DEFAULT_MSG
            else:
                # or else the chosen letter is wrong
                wrong_guess_list.append(chosen_letter)
                num_errors += 1
                msg = hangman_helper.DEFAULT_MSG
        elif input1[0] == hangman_helper.HINT:
            # checks if the gamer asked for a hint and gives a hint
            new_list_words = filter_words_list(words_list, pattern,
                                               wrong_guess_list)
            letter = choose_letter(new_list_words, pattern)
            msg = hangman_helper.HINT_MSG + letter
    if pattern == word:
        hangman_helper.display_state(pattern, num_errors, wrong_guess_list,
                                     hangman_helper.WIN_MSG, True)
    else:
        hangman_helper.display_state(pattern, num_errors, wrong_guess_list,
                                     hangman_helper.LOSS_MSG + word, True)


def main():
    """A function that generates the game 'hangman' using the function-
    run_single_game"""
    words_list = hangman_helper.load_words()
    run_single_game(words_list)
    input1 = hangman_helper.get_input()
    while input1[0] == hangman_helper.PLAY_AGAIN and input1[1]:
        run_single_game(words_list)
        input1 = hangman_helper.get_input()


def letters_in_pattern(word, pattern):
    """A function that receives a word and a pattern and returns True if the
    pattern is suitable to the word (if every letter in the pattern matches the
    location of the same letter in the word and False otherwise- this is a
    auxiliary function for filter_words_list"""
    already_in_pattern = {}
    letters_in_pattern_list = []
    for i in range(CHAR_A, CHAR_Z + 1):
        already_in_pattern[chr(i)] = 0
    for i in range(0, len(pattern)):
        if pattern[i] != "_":
            already_in_pattern[pattern[i]] = already_in_pattern[pattern[i]] + 1
            letters_in_pattern_list.append(pattern[i])
    for i in range(0, len(word)):
        if pattern[i] == word[i]:
            already_in_pattern[word[i]] = already_in_pattern[word[i]] - 1
        elif pattern[i] == "_" and word[i] in letters_in_pattern_list:
            already_in_pattern[word[i]] = already_in_pattern[word[i]] - 1
    for i in range(CHAR_A, CHAR_Z + 1):
        if already_in_pattern[chr(i)] != 0:
            return False
    return True


def same_wrong_letters(word, wrong_guess_list):
    """A function that receives a word and a list with wrong letters and
    returns True if nun of the letters in the list is in the word and False
    otherwise- this is a auxiliary function for filter_words_list"""
    for i in range(0, len(word)):
        for j in range(0, len(wrong_guess_list)):
            if word[i] == wrong_guess_list[j]:
                return False
    return True


def filter_words_list(words, pattern, wrong_guess_list):
    """A function that receives a list of words, a pattern and a wrong guess
    list and returns a new list containing only the words that can match the
    pattern. this function uses the functions- same_wrong_letters and
    optional_words."""
    optional_words = []
    for i in range(0, len(words)):
        if len(words[i]) == len(pattern) and \
                letters_in_pattern(words[i], pattern) and \
                same_wrong_letters(words[i], wrong_guess_list):
            optional_words.append(words[i])
    return optional_words


def choose_letter(words, pattern):
    """A function that receives a list of words and a pattern and returns the
    most frequent letter in the list that also does not appear in the
    pattern"""
    max_count = 0
    max_letter = ""
    for i in range(CHAR_A, CHAR_Z + 1):
        counter = 0
        for j in range(0, len(words)):
            for k in range(0, len(words[j])):
                if chr(i) == words[j][k]:
                    counter += 1
        if counter > max_count and chr(i) not in pattern:
            max_count = counter
            max_letter = chr(i)
    return max_letter


if __name__ == '__main__':
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()
