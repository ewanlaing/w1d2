stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
stops.append("Edinburgh Waverley")
stops.insert(0, "Glasgow Queen St")
stops.insert(4, "Polmont")
print(stops.index("Linlithgow"))
stops.remove("Livingston")
stops.pop(2)
print(len(stops))
stops.sort()
stops.reverse()

for stop in stops:
    print(stop)