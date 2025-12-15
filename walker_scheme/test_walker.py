from walker import Walker

test = Walker([("a", 0), ("b", 1)])

def test():
    rand = test.get_random()
    assert rand == 1

