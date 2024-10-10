class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner = ""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        # Owner.owner_pets.append(Pet())
        Pet.all.append(self)
        
        if owner:
            owner.owner_pets.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value in Pet.PET_TYPES:
            self._pet_type = value
        else:
            raise Exception
        

            

class Owner:
    
    
    def __init__(self, name):
        self.name = name
        self.owner_pets = []
    
    def pets(self):
        return self.owner_pets
    
    def add_pet(self, pet):
        if pet in Pet.all:
            pet.owner = self
            self.owner_pets.append(pet)
        else:
            raise Exception
            
            
    def get_sorted_pets(self):
        return sorted(self.owner_pets, key=lambda pet: pet.name)
            