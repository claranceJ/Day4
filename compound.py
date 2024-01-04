elements = {
  "helium": {
    "weight": 4.0026,
    "group": "noble gases",
    "symbol": "He"
  },
  "Hydrogen":{
    "weight": 1.0078,
    "group": "alkali metals",
    "symbol": "H"
  },
  "Lithium":{
    "weight": 6.94,
    "group": "alkali metals",
    "symbol": "Li"
  }
}

print(elements["helium"]["weight"])
print(elements.get("Oxygen", "There\'s no Oxygen in the dictionary"))