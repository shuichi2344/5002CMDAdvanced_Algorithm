from typing import Dict, Set
from Graph_Q3 import Person, PrivacySetting  # Import Person and PrivacySetting from Q3 module

# Class to represent a social network graph
class SocialGraph:
    def __init__(self):
        # Dictionary mapping usernames to Person objects
        self.users: Dict[str, Person] = {}
        # Dictionary mapping each user to the set of users they follow
        self.following: Dict[str, Set[str]] = {}
        # Dictionary mapping each user to the set of users who follow them
        self.followers: Dict[str, Set[str]] = {}

    # Add a new user to the social graph
    def add_user(self, person: Person):
        username = person.name
        if username not in self.users:
            self.users[username] = person
            self.following[username] = set()  # Initialize empty following set
            self.followers[username] = set()  # Initialize empty followers set

    # Create a "follow" relationship between users
    def follow(self, follower_name: str, followed_name: str):
        if follower_name == followed_name:
            return  # Prevent users from following themselves
        if follower_name in self.users and followed_name in self.users:
            self.following[follower_name].add(followed_name)
            self.followers[followed_name].add(follower_name)
        else:
            print(f"One or both users '{follower_name}', '{followed_name}' do not exist.")

    # Remove a "follow" relationship between users
    def unfollow(self, follower_name: str, followed_name: str):
        if follower_name in self.following and followed_name in self.following[follower_name]:
            self.following[follower_name].remove(followed_name)
            self.followers[followed_name].remove(follower_name)

    # Return the set of users a given user is following
    def get_following(self, username: str):
        return self.following.get(username, set())

    # Return the set of followers for a given user
    def get_followers(self, username: str):
        return self.followers.get(username, set())

    # Return the Person object for a given username
    def get_user(self, username: str) -> Person:
        return self.users.get(username)

    # Print the entire social network in a readable format
    def display_network(self):
        for username in sorted(self.users):
            user = self.users[username]
            print(user)  # Print Person object (assumes __str__ method is defined)
            print(f"  Following → {', '.join(sorted(self.following[username])) or 'None'}")
            print(f"  Followers ← {', '.join(sorted(self.followers[username])) or 'None'}\n")
            print()


# Example usage
if __name__ == "__main__":
    # List of Person objects representing user profiles
    people_profiles = [
        Person("Shirlyn", "Female", "14 forever", PrivacySetting.PUBLIC),
        Person("Mika", "Male", "Exploring new places", PrivacySetting.PRIVATE),
        Person("Emily", "Female", "Digital artist & cat mom", PrivacySetting.PUBLIC),
        Person("Aiman", "Male", "Space enthusiast. Saturn is my favorite planet.", PrivacySetting.PUBLIC),
        Person("Mei Lin", "Female", "Weekend hiker. Nature keeps me grounded", PrivacySetting.PRIVATE),
    ]

    # Create a new instance of SocialGraph
    social_graph = SocialGraph()

    # Add all users to the graph
    for person in people_profiles:
        social_graph.add_user(person)

    # Define following relationships between users
    social_graph.follow("Shirlyn", "Emily")
    social_graph.follow("Shirlyn", "Mika")
    social_graph.follow("Mika", "Shirlyn")
    social_graph.follow("Emily", "Mika")
    social_graph.follow("Aiman", "Mei Lin")
    social_graph.follow("Mei Lin", "Aiman")

    # Print the social network
    social_graph.display_network()
