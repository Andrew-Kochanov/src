from walker import Walker


def test():
    test = Walker([("a", 0), ("b", 1)])
    rand = test.get_random()
    assert rand == 1

