julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
(name, surname, birth_year, movie, movie_years, profession, birth_place) = julia

print(name, birth_year, movie, movie_years, profession, birth_place)


print(julia[2])
print(julia[2:6])

print(len(julia))

for field in julia:
    print(field)

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)
