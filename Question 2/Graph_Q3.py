from enum import Enum
from typing import Optional


# Enum for privacy settings
class PrivacySetting(Enum):
    PUBLIC = "Public"
    PRIVATE = "Private"


# Person class to represent a social media user
class Person:
    def __init__(self,
                 name: str,
                 gender: Optional[str] = None,
                 biography: Optional[str] = "",
                 privacy: PrivacySetting = PrivacySetting.PUBLIC):
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy

    def update_bio(self, new_bio: str):
        """Update the user's biography."""
        self.biography = new_bio

    def set_privacy(self, new_privacy: PrivacySetting):
        """Update the user's privacy setting."""
        self.privacy = new_privacy

    def __str__(self):
        """String representation of the person."""
        return (
            f"Name: {self.name}\n"
            f"Gender: {self.gender or 'Not specified'}\n"
            f"Biography: {self.biography or 'No bio'}\n"
            f"Privacy: {self.privacy.value}"
        )


# Create a list to store up to 10 Person objects
people_profiles = []

# Create 5 Person profiles
people_profiles.append(Person(
    name="Shirlyn",
    gender="Female",
    biography="14 forever",
    privacy=PrivacySetting.PUBLIC
))

people_profiles.append(Person(
    name="Mika",
    gender="Male",
    biography="Exploring new places",
    privacy=PrivacySetting.PRIVATE
))

people_profiles.append(Person(
    name="Emily",
    gender="Female",
    biography="Digital artist & cat mom",
    privacy=PrivacySetting.PUBLIC
))

people_profiles.append(Person(
    name="Aiman",
    gender="Male",
    biography="Space enthusiast. Saturn is my favorite planet.",
    privacy=PrivacySetting.PUBLIC
))

people_profiles.append(Person(
    name="Mei Lin",
    gender="Female",
    biography="Weekend hiker. Nature keeps me grounded",
    privacy=PrivacySetting.PRIVATE
))

# Add this guard to only run if this file is executed directly
if __name__ == "__main__":
    print("=== Social Media Profiles ===")
    for person in people_profiles:
        print(person)
        print("-" * 30)
