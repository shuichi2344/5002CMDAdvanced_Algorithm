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

# Create a new user
user1 = Person(
    name="Shirlyn",
    gender="Female",
    biography="Love coding & coffee!",
    privacy=PrivacySetting.PRIVATE)

# Print user info
print(user1)

# Update biography and privacy
user1.update_bio("Exploring mobile app development!")
user1.set_privacy(PrivacySetting.PUBLIC)

# Print updated info
print("\nUpdated Profile:")
print(user1)
