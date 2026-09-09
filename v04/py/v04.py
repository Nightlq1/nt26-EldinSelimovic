#A function that builds the configuration for a single VLAN.
def vlan_config(number, name):
    rader=[]
    rader.append(f"vlan {number}")
    rader.append(f" name {name}")
    return rader


#Nordvik's networks. Replace them with your own.
vlans = {
    10: "Kontor",
    20: "Hotell",
    30: "Drift",
    99: "Management",    
}

#Run the function once for each VLAN and print the result.
for number in vlans:
    for rad in vlan_config(number, vlans[number]):
        print(rad)