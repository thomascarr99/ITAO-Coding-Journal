class FamilyMember:
    def __init__(self, name, relationship, height):
        self.name = name
        self.relationship = relationship
        self.height = height

familymember1 = FamilyMember("Natalie", "mother", 68)

print("My {} is named {} and is {} inches tall.").format(familymember1.relationship, familymember1.name, familymember1.height)

familymember2 = FamilyMember("Tim", "father", 70)
familymember3 = FamilyMember("Connor", "brother", 72)
familymember4 = FamilyMember("Darby", "sister", 68)