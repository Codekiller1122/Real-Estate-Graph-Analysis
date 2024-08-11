import networkx as nx
import matplotlib.pyplot as plt

# Define nodes and edges
nodes = ["Biz1", "Biz2", "Biz3", "Biz4", "Biz5", "Biz6", "Biz7", "Biz8", "Biz9", "Biz10",
         "Biz11", "Biz12", "Biz13", "Biz14", "Biz15", "Biz16", "Biz17", "Biz18", "Biz19", "Biz20",
         "Biz21", "Biz22", "Biz23", "Biz24", "Biz25", "Biz26", "Biz27", "Biz28", "Biz29", "Biz30",
         "Biz31", "Biz32", "Biz33", "Biz34", "Biz35", "Biz36", "Biz37", "Biz38", "Biz39", "Biz40",
         "Biz41", "Biz42", "Biz43", "Biz44", "Biz45", "Biz46", "Biz47", "Biz48", "Biz49", "Biz50",
         "Biz51"]

edges = [
    ("Biz1", "Biz3"), ("Biz1", "Biz18"), ("Biz1", "Biz22"), ("Biz1", "Biz27"), ("Biz1", "Biz29"), 
    ("Biz1", "Biz32"), ("Biz1", "Biz37"), ("Biz3", "Biz37"), ("Biz3", "Biz23"), ("Biz3", "Biz33"),
    ("Biz3", "Biz41"), ("Biz4", "Biz23"), ("Biz4", "Biz3"), ("Biz4", "Biz33"), ("Biz4", "Biz37"),
    ("Biz4", "Biz41"), ("Biz4", "Biz5"), ("Biz4", "Biz6"), ("Biz4", "Biz8"), ("Biz4", "Biz17"),
    ("Biz4", "Biz37"), ("Biz4", "Biz38"), ("Biz4", "Biz41"), ("Biz4", "Biz46"), ("Biz4", "Biz47"),
    ("Biz4", "Biz49"), ("Biz5", "Biz6"), ("Biz5", "Biz8"), ("Biz5", "Biz17"), ("Biz5", "Biz38"),
    ("Biz5", "Biz39"), ("Biz5", "Biz41"), ("Biz5", "Biz46"), ("Biz5", "Biz47"), ("Biz6", "Biz8"),
    ("Biz6", "Biz17"), ("Biz6", "Biz37"), ("Biz6", "Biz38"), ("Biz6", "Biz41"), ("Biz6", "Biz47"),
    ("Biz6", "Biz48"), ("Biz7", "Biz8"), ("Biz7", "Biz12"), ("Biz7", "Biz18"), ("Biz7", "Biz19"),
    ("Biz7", "Biz22"), ("Biz7", "Biz26"), ("Biz7", "Biz27"), ("Biz7", "Biz29"), ("Biz7", "Biz32"),
    ("Biz7", "Biz34"), ("Biz7", "Biz42"), ("Biz7", "Biz44"), ("Biz7", "Biz47"), ("Biz8", "Biz17"),
    ("Biz8", "Biz27"), ("Biz8", "Biz28"), ("Biz8", "Biz36"), ("Biz8", "Biz37"), ("Biz8", "Biz46"),
    ("Biz8", "Biz47"), ("Biz9", "Biz12"), ("Biz9", "Biz18"), ("Biz9", "Biz19"), ("Biz9", "Biz26"),
    ("Biz9", "Biz27"), ("Biz9", "Biz29"), ("Biz9", "Biz31"), ("Biz9", "Biz34"), ("Biz9", "Biz37"),
    ("Biz10", "Biz13"), ("Biz10", "Biz14"), ("Biz10", "Biz15"), ("Biz10", "Biz16"), ("Biz10", "Biz17"),
    ("Biz10", "Biz20"), ("Biz10", "Biz21"), ("Biz10", "Biz28"), ("Biz10", "Biz33"), ("Biz10", "Biz35"),
    ("Biz10", "Biz36"), ("Biz10", "Biz40"), ("Biz10", "Biz43"), ("Biz10", "Biz48"), ("Biz10", "Biz50"),
    ("Biz10", "Biz51"), ("Biz11", "Biz13"), ("Biz11", "Biz14"), ("Biz11", "Biz1"), ("Biz11", "Biz16"),
    ("Biz11", "Biz17"), ("Biz11", "Biz20"), ("Biz11", "Biz21"), ("Biz11", "Biz28"), ("Biz11", "Biz35"),
    ("Biz11", "Biz36"), ("Biz11", "Biz40"), ("Biz11", "Biz43"), ("Biz11", "Biz50"), ("Biz11", "Biz51"),
    ("Biz12", "Biz26"), ("Biz12", "Biz31"), ("Biz12", "Biz34"), ("Biz12", "Biz47"), ("Biz13", "Biz14"),
    ("Biz13", "Biz15"), ("Biz13", "Biz1"), ("Biz13", "Biz16"), ("Biz13", "Biz17"), ("Biz13", "Biz20"),
    ("Biz13", "Biz21"), ("Biz13", "Biz28"), ("Biz13", "Biz35"), ("Biz13", "Biz36"), ("Biz13", "Biz40"),
    ("Biz13", "Biz43"), ("Biz13", "Biz50"), ("Biz13", "Biz51"), ("Biz14", "Biz15"), ("Biz14", "Biz16"),
    ("Biz14", "Biz17"), ("Biz14", "Biz20"), ("Biz14", "Biz21"), ("Biz14", "Biz28"), ("Biz14", "Biz35"),
    ("Biz14", "Biz36"), ("Biz14", "Biz40"), ("Biz14", "Biz43"), ("Biz14", "Biz50"), ("Biz14", "Biz51"),
    ("Biz15", "Biz48"), ("Biz15", "Biz16"), ("Biz15", "Biz17"), ("Biz15", "Biz20"), ("Biz15", "Biz21"),
    ("Biz15", "Biz28"), ("Biz15", "Biz35"), ("Biz15", "Biz36"), ("Biz15", "Biz40"), ("Biz15", "Biz43"),
    ("Biz15", "Biz50"), ("Biz15", "Biz51"), ("Biz16", "Biz17"), ("Biz16", "Biz20"), ("Biz16", "Biz21"),
    ("Biz16", "Biz28"), ("Biz16", "Biz35"), ("Biz16", "Biz36"), ("Biz16", "Biz40"), ("Biz16", "Biz43"),
    ("Biz16", "Biz50"), ("Biz16", "Biz25"), ("Biz16", "Biz48"), ("Biz17", "Biz20"), ("Biz17", "Biz21"),
    ("Biz17", "Biz28"), ("Biz17", "Biz35"), ("Biz17", "Biz36"), ("Biz17", "Biz40"), ("Biz17", "Biz43"),
    ("Biz17", "Biz50"), ("Biz17", "Biz51"), ("Biz17", "Biz23"), ("Biz17", "Biz27"), ("Biz17", "Biz33"),
    ("Biz17", "Biz37"), ("Biz17", "Biz41"), ("Biz17", "Biz38"), ("Biz17", "Biz46"), ("Biz17", "Biz47"),
    ("Biz18", "Biz22"), ("Biz18", "Biz19"), ("Biz18", "Biz27"), ("Biz18", "Biz29"), ("Biz18", "Biz32"),
    ("Biz18", "Biz37"), ("Biz19", "Biz22"), ("Biz19", "Biz27"), ("Biz19", "Biz29"), ("Biz19", "Biz32"),
    ("Biz19", "Biz37")
]

# Create the graph
G_XO = nx.Graph()
G_XO.add_nodes_from(nodes)
G_XO.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(12, 12))

plt.subplot(2, 2, 1)
nx.draw_random(G_XO, with_labels=True, font_size=7, font_color="black", node_color="skyblue", node_size=500)
plt.title("Random Layout")

plt.subplot(2, 2, 2)
nx.draw_circular(G_XO, with_labels=True, font_color="whitesmoke", font_size=10, node_color="lightgreen", node_size=500)
plt.title("Circular Layout")

plt.subplot(2, 2, 3)
# Use spring layout as a fallback
nx.draw_spring(G_XO, with_labels=True, font_color="whitesmoke", font_size=10, node_color="lightcoral", node_size=500)
plt.title("Spring Layout")

plt.subplot(2, 2, 4)
nx.draw_networkx(G_XO, with_labels=True, font_color="whitesmoke", font_size=10, node_color="lightgoldenrodyellow", node_size=500)
plt.title("NetworkX Layout")

plt.show()

# Print graph metrics
print(f"Radius: {nx.radius(G_XO)}")
print(f"Diameter: {nx.diameter(G_XO)}")
print(f"Eccentricity: {nx.eccentricity(G_XO)}")
print(f"Center: {nx.center(G_XO)}")
print(f"Periphery: {nx.periphery(G_XO)}")
print(f"Density: {nx.density(G_XO)}")
print(f"Degree: {dict(G_XO.degree())}")
