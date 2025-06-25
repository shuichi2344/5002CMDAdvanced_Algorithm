class Person:
    def __init__(self, name, gender, biography, privacy):
        # Initialize a new user profile with basic info
        self.name = name                      # User's name
        self.gender = gender                  # User's gender
        self.biography = biography            # User's biography or description
        self.privacy = privacy.lower()        # Privacy setting: 'public' or 'private'

    # Getter method to retrieve the user's name
    def get_name(self):
        return self.name

    # Getter method to retrieve the user's gender
    def get_gender(self):
        return self.gender

    # Getter method to retrieve the user's biography
    def get_biography(self):
        return self.biography

    # Getter method to retrieve the user's privacy setting
    def get_privacy(self):
        return self.privacy

    # Returns True if the profile is public, False if private
    def is_public(self):
        return self.privacy == "public"
