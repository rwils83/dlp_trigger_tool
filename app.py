import random
import string
class DLPPerson:
    def __init__(self):
        self.cc_number = self._generate_cc_number()
        self.social = self._generate_social()
        self.name = self._generate_name()
        self.telephone = self._generate_telephone()
        self.maiden = self._generate_maiden()
    @staticmethod
    def _generate_cc_number():
        return f'{random.randint(1111,9999)}-{random.randint(1111,9999)}-{random.randint(1111,9999)}-{random.randint(1111,9999)}'
    @staticmethod
    def _generate_social():
        return f'{random.randint(111,999)}-{random.randint(11,99)}-{random.randint(1111,9999)}'
    @staticmethod
    def _generate_name():
        letters = string.ascii_lowercase
        first_name = ''.join(random.choice(letters) for i in range(8)).capitalize()
        last_name = ''.join(random.choice(letters) for i in range(10)).capitalize()
        middle_initial = ''.join(random.choice(letters) for i in range(1)).capitalize()
        return f'{first_name} {middle_initial}. {last_name}'
    @staticmethod
    def _generate_telephone():
        area_code = random.randint(111, 999)
        first_three = random.randint(111, 999)
        last_four = random.randint(1111, 9999)
        return f'({area_code}) {first_three}-{last_four}'
    @staticmethod
    def _generate_maiden():
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10))
        return name.capitalize()
    def __str__(self):
        return f'{self.name},{self.cc_number},{self.social},{self.maiden},{self.telephone}'
people = []
for i in range(1000):
    people.append(DLPPerson())
for person in people:
    with open('names.csv', 'a+') as f:
        f.write(str(person)+'\r')