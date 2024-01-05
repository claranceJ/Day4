#Compound Datastructure
elements = {
    "helium": {
        "weight": [4.0026, 32],
        "group": "noble gases",
        "symbol": "He"
    },
    "Hydrogen": {
        "weight": 1.0078,
        "group": "alkali metals",
        "symbol": "H"
    },
    "Lithium": {
        "weight": 6.94,
        "group": "alkali metals",
        "symbol": "Li"
    }
}

# printing the elements value and checking if it exists
print(elements["helium"]["weight"])
print(elements.get("Oxygen", "There\'s no Oxygen in the dictionary"))

#Adding Elements in a dictionary
Oxygen = {"weight": 15.999, "group": "halogens", "symbol": "O"}
elements["Oxygen"] = Oxygen

print("elements: ", elements)

#OR

elements["Sodium"] = {"weight": 23.0, "group": "alkali metals", "symbol": "Na"}

print("updated list: ", elements)

#Appending Elements in a dictionary
elements["helium"]["weight"].append(21)
print(elements["helium"]["weight"])
