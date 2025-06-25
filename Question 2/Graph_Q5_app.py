from Graph_Q5_UDGraph import UDGraph  # Import the undirected graph class
from Graph_Q5_person import Person    # Import the Person class


# Sparkles class represents the core social network platform
class Sparkles:
    def __init__(self):
        self.my_graph = UDGraph()  # Create a graph to manage follow relationships
        self.users = []            # List to store all user profiles

    # Add a new user profile to the network
    def add_new_profile(self, name, gender, biography, privacy):
        person = Person(name, gender, biography, privacy)  # Create a new Person object
        self.users.append(person)                          # Add to the users list
        self.my_graph.add_vertex(person)                   # Add the user as a vertex in the graph

    # Create a follow relationship (edge) between two users
    def add_follow(self, follower, followed_user):
        self.my_graph.add_edge(follower, followed_user)

    # Remove a follow relationship (edge) between two users
    def remove_follow(self, follower, followed_user):
        self.my_graph.remove_edge(follower, followed_user)

    # Return the list of all user profiles
    def get_all_profiles(self):
        return self.users

    # Display a user's profile details based on privacy setting
    def display_profile(self, person):
        print("\n===== View Details for Any Profile: =====")
        print(f"Name: {person.get_name()}")
        if person.is_public():  # Only show full details if profile is public
            print(f"Gender: {person.get_gender()}")
            print(f"Biography: {person.get_biography()}")
            print(f"Privacy: {person.get_privacy()}")
        else:
            print("This is a private profile.")  # Hide details if profile is private

    # Return the list of users who follow the given person
    def get_followers(self, person):
        return self.my_graph.list_incoming_adjacent(person)

    # Return the list of users that the given person is following
    def list_following(self, person):
        return self.my_graph.list_outgoing_adjacent(person)
