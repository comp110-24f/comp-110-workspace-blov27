from Classwork.unit_tests.list_fns import get_first, get_and_remove_first, remove_first


def test_get_first() -> None:
    """checks to see if get_first works- it should return the first item in a list"""
    nba_players: list[str] = ["bird", "magic", "jordan", "james"]
    assert get_first(nba_players) == "bird"


# desired return value
def test_remove_first_value() -> None:
    """remove_first should return none"""
    nba_players: list[str] = ["bird", "magic", "jordan", "james"]
    assert remove_first(nba_players) == None


# desired behavior
def test_remove_first_behavior() -> None:
    """remove_first should remove the first element of the list"""
    nba_players: list[str] = ["bird", "magic", "jordan", "james"]
    remove_first(nba_players)
    assert nba_players == ["magic", "jordan", "james"]


def test_get_first_edge_case() -> None:
    """get first called on an empty list should return an empty string"""
    assert get_first([]) == ""
