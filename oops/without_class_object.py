#analytics/analysis  of  players
#If an entity has multiple attributes,then it is better to use dictionary
virat={
     "firstName":"virat",
     "lastName":"kholi",
     "scores":[]
}
virat["scores"].append(30)
virat["scores"].append(40)
virat["scores"].append(0)


dhoni={
    "firstName":"MS",
    "lastName":"dhoni",
    "scores":[]

}

dhoni["scores"].append(30)
dhoni["scores"].append(50)
dhoni["scores"].append(50)

def get_average(player):
    return sum(player["scores"])/len(player["scores"])

print("Kholis average in last three games: ",get_average(virat))
print("dhonis average in last three games: ",get_average(dhoni))