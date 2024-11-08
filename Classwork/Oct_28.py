class Profile:
    username: str
    followers: list[str]
    following: list[str]

    def __init__(self, handle: str):
        self.username = handle
        self.followers = []
        self.following = []

        # method definitions

    def follow(self, username: str) -> None:
        self.following.append(username)

    def get_following(self) -> list[str]:
        return self.following

    my_prof: Profile = Profile("comp110fan")  # Calls __init__()
    print(my_prof.following)

    my_prof.follow("unc.latinosintech")
    print(my_prof.following)
