from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokeman Name", ["Picachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align="l"

print(table)