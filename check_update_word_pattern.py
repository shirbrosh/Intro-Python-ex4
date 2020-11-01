from hangman import update_word_pattern


def test_for_update_word_pattern():
    """A function that tests the function update_word_pattern from hangman.py.
    It runs 4 extrema inputs and if all the outputs is as expected the test
    will print 'Function 'update_word_pattern' test success' and returns True,
    if the test failed it will print 'Function 'update_word_pattern' test fail'
    and returns False"""
    counter = 0
    new_pattern = update_word_pattern("anachronistic", "a_a__________", "c")
    if new_pattern == "a_ac________c":
        counter += 1
    new_pattern = update_word_pattern("panacea", "p_n_ce_", "a")
    if new_pattern == "panacea":
        counter += 1
    new_pattern = update_word_pattern("python", "__th__", "w")
    if new_pattern == "__th__":
        counter += 1
    new_pattern = update_word_pattern("avadakedavra", "_v___k______", "a")
    if new_pattern == "ava_ak__a__a":
        counter += 1
    if counter == 4:
        print("Function 'update_word_pattern' test success")
        return True
    else:
        print("Function 'update_word_pattern' test fail")
        return False


if __name__ == '__main__':
    test_for_update_word_pattern()
