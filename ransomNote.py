def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    :type ransom_note: str
    :type magazine: str
    :rtype: bool
    """
    # Solution1:
    return all(ransom_note.count(letter) <= magazine.count(letter) for letter in set(ransom_note))


def can_construct1(ransom_note: str, magazine: str) -> bool:
    """
    :type ransom_note: str
    :type magazine: str
    :rtype: bool
    """
    # Solution2:
    for note in ransom_note:
        if note not in magazine:
            return False
        magazine = magazine.replace(note, '', 1)
    return True


if __name__ == '__main__':
    print(can_construct("a", "b"))
    print(can_construct1("a", "b"))
    print(can_construct("aa", "ab"))
    print(can_construct1("aa", "ab"))
    print(can_construct("aa", "aab"))
    print(can_construct1("aa", "aab"))
