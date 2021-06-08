opposites = {"up": "down", "right": "wrong", "true": "false"}
alias = opposites

print(alias is opposites)

acopy = opposites.copy()
acopy["right"] = "left"
print(opposites)
print(acopy)

alias["right"]  = "left"
print(opposites)

