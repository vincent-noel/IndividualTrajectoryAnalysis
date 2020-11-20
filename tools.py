import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib as mpl
import matplotlib.pyplot as plt

def load_trajs(path, outputs):

    trajs = []
    all_states = set()
    with open(path + "/res_traj.txt", "r") as res_traj:
        id_trajectory = 0
        states = []
        for line in res_traj.readlines():
                if line.startswith("Trajectory"):
                    if id_trajectory > 0:
                        trajs.append(states)
                        states = []
                    id_trajectory = int(line.split("#")[1])

                elif line.startswith(" istate"):
                    state = line.split("\t")[1].strip()
                    state_array = " -- ".join(sorted([node for node in state.split(" -- ") if node in outputs]))
                    if state_array == '':
                        state_array = "<nil>"

                    all_states.add(state_array)
                    states.append(state_array)

                elif line == "\n":
                    pass

                else:
                    state = line.split("\t")[1].strip()
                    state_array = " -- ".join(sorted([node for node in state.split(" -- ") if node in outputs]))

                    if state_array == '':
                        state_array = "<nil>"

                    if (len(states) == 0 or states[len(states)-1] != state_array):
                        all_states.add(state_array)                    
                        states.append(state_array)
    return trajs, all_states

def draw_graph_from_pandas(data):
    G = nx.from_pandas_adjacency(data,  create_using=nx.DiGraph())

    edge_colors = [edge['weight'] for _, edge in G.edges.items()]

    pos = graphviz_layout(G, prog="sfdp")
    plt.figure(figsize=(8,4), dpi=100)

    nx.draw(G, pos, with_labels=True, edgelist=[])

    edges = nx.draw_networkx_edges(
        G,
        pos,
        arrowstyle="->",
        arrowsize=10,
        edgelist=G.edges().keys(),
        edge_color=edge_colors,
        edge_cmap=plt.cm.Blues,
        width=2,
        connectionstyle='arc3, rad = 0.1'
    )

    pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Blues)
    pc.set_array(edge_colors)
    plt.colorbar(pc)
    plt.show()

def visit(node, array, proba, paths_dict, probas, ids_state, nb_loops):

    array.append(node)

    nonzeros = {ids_state[ind]:probas.loc[node,:].iloc[ind] for ind in probas.loc[node, :].to_numpy().nonzero()[0]}
    for state in sorted(nonzeros, key=nonzeros.get, reverse=True):

        if state == '<nil>':
            paths_dict[proba*nonzeros[state]] = array
        
        elif array.count(state) < nb_loops+1:
            visit(state, []+array, proba*nonzeros[state], paths_dict, probas, ids_state, nb_loops)
            
def compute_circuits(probas, ids_state, node, nb_loops):
    paths_dict = {}
    visit('<nil>', [], 1, paths_dict, probas, ids_state, nb_loops)
    return paths_dict
