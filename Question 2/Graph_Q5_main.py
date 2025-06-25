from Graph_Q5_app import Sparkles  # Import the main Sparkles app class


# Function to display the main menu
def print_menu():
    print("""
    **************************************
    Welcome to Sparkles, Your New Social Media App:
    **************************************
    1. View names of all profiles
    2. View details for any profile
    3. View followers of any profile
    4. View followed accounts of any profile
    5. Add a new user profile
    6. Follow a user
    7. Unfollow a user
    8. Quit
    **************************************
    """)


# Helper function to allow user to select a profile for any action
def select_profile(app, action):
    people = app.get_all_profiles()  # Get all user profiles
    if not people:
        print("No profiles available.")
        return None

    # Display all profile names with an index
    for i, person in enumerate(people, 1):
        print(f"{i}.) {person.get_name()}")

    # Ask user to select a profile by number
    try:
        idx = int(input(f"Select whose profile to {action} (1 - {len(people)}): ")) - 1
        if 0 <= idx < len(people):
            return people[idx]
        else:
            print("Invalid number selected.")
    except ValueError:
        print("Invalid input. Please enter a number")
    return None


# Main driver function of the app
def main():
    app = Sparkles()  # Create an instance of the app

    # Create sample user profiles
    app.add_new_profile("Alice", "Female", "Loves hiking and photography.", "public")
    app.add_new_profile("Bob", "Male", "Software developer and gamer.", "private")
    app.add_new_profile("Charlie", "Male", "Foodie and cat dad.", "public")
    app.add_new_profile("Diana", "Female", "Tech enthusiast. Coffee addict.", "public")
    app.add_new_profile("Eve", "Female", "Cybersecurity nerd. Always alert.", "private")

    # Map usernames to user objects for easier access
    users = {user.get_name(): user for user in app.get_all_profiles()}

    # Set up sample follow relationships
    app.add_follow(users["Alice"], users["Charlie"])
    app.add_follow(users["Alice"], users["Diana"])
    app.add_follow(users["Bob"], users["Alice"])
    app.add_follow(users["Diana"], users["Bob"])
    app.add_follow(users["Eve"], users["Alice"])
    app.add_follow(users["Charlie"], users["Eve"])

    # Main loop for user interaction
    while True:
        print_menu()
        choice = input("Enter your choice (1 - 8): ").strip()

        # Validate input to ensure it's a number from 1 to 8
        while choice not in [str(i) for i in range(1, 9)]:
            print("Invalid input. Please enter a number between 1 and 8.")
            choice = input("Enter your choice (1 - 8): ").strip()
        print("**************************************")

        # Option 1: Show all profile names
        if choice == '1':
            print("View All Profile Names:")
            print("=================================")
            profiles = app.get_all_profiles()
            if not profiles:
                print("No profiles created yet.")
            else:
                for i, person in enumerate(profiles, 1):
                    print(f"{i}.) {person.get_name()}")

        # Option 2: View full profile details (if public)
        elif choice == '2':
            person = select_profile(app, "view")
            if person:
                app.display_profile(person)

        # Option 3: View followers of a profile
        elif choice == '3':
            person = select_profile(app, "view followers")
            if person:
                print(f"\nFollowers of {person.get_name()}:")
                print("=================================")
                followers = app.get_followers(person)
                if not followers:
                    print("No followers found.")
                else:
                    for f in followers:
                        print(f"- {f.get_name()}")

        # Option 4: View who a person is following
        elif choice == '4':
            person = select_profile(app, "view followings")
            if person:
                print(f"\nAccounts followed by {person.get_name()}:")
                print("=================================")
                followings = app.list_following(person)
                if not followings:
                    print("Not following anyone.")
                else:
                    for f in followings:
                        print(f"- {f.get_name()}")

        # Option 5: Add a new profile via user input
        elif choice == '5':
            name = input("Enter name: ")
            gender = input("Enter gender (male/female): ").strip().lower()
            while gender not in ['male', 'female']:
                print("Invalid gender. Please enter 'male' or 'female'")
                gender = input("Enter gender (male/female): ").strip().lower()
            bio = input("Enter biography: ")
            privacy = input("Enter privacy (public/private): ").strip().lower()
            while privacy not in ['public', 'private']:
                print("Invalid privacy option. Please enter 'public' or 'private'.")
                privacy = input("Enter privacy (public/private): ").strip().lower()
            app.add_new_profile(name, gender, bio, privacy)
            print("Profile added successfully.")

        # Option 6: Follow another user
        elif choice == '6':
            follower = select_profile(app, "follow from")
            if follower:
                all_profiles = app.get_all_profiles()
                already_following = set(app.list_following(follower))
                # Filter out self and users already followed
                not_following = [p for p in all_profiles if p != follower and p not in already_following]

                if not not_following:
                    print(f"{follower.get_name()} is already following everyone else.")
                else:
                    print(f"\nSelect a user for {follower.get_name()} to follow:")
                    for i, person in enumerate(not_following, 1):
                        print(f"{i}.) {person.get_name()}")
                    try:
                        idx = int(input(f"Enter choice (1 - {len(not_following)}): ")) - 1
                        if 0 <= idx < len(not_following):
                            followed_user = not_following[idx]
                            app.add_follow(follower, followed_user)
                            print(f"{follower.get_name()} now follows {followed_user.get_name()}.")
                        else:
                            print("Invalid number selected.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

        # Option 7: Unfollow someone
        elif choice == '7':
            unfollower = select_profile(app, "unfollow from")
            if unfollower:
                following = list(app.list_following(unfollower))
                if not following:
                    print(f"{unfollower.get_name()} is not following anyone.")
                else:
                    print(f"\nSelect who to unfollow from {unfollower.get_name()}'s followings:")
                    for i, person in enumerate(following, 1):
                        print(f"{i}.) {person.get_name()}")
                    try:
                        idx = int(input(f"Enter choice (1 - {len(following)}): ")) - 1
                        if 0 <= idx < len(following):
                            unfollowed_user = following[idx]
                            app.remove_follow(unfollower, unfollowed_user)
                            print(f"{unfollower.get_name()} has unfollowed {unfollowed_user.get_name()}.")
                        else:
                            print("Invalid number selected.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

        # Option 8: Quit the application
        elif choice == '8':
            print("Exiting Sparkles. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


# Run the app when this file is executed
if __name__ == '__main__':
    main()