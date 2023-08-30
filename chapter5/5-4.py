
# import datetime
# day1 = datetime.date(2021, 12, 14)
# day2 = datetime.date(2023, 4, 5)

# print(day1)
# print(day2)
# print(day2 - day1)

# diff = day2 - day1
# print(diff.days)
# print(diff)
# a1 = day2 - day1
# print(a1.days)
# print((day2 - day1).days)
# print(day1.isoweekday())

from faker import Faker
fake = Faker('ko-KR')
print(fake.name())
print(fake.address())