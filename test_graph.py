"""
Test script to verify graph functionality and shortest path algorithm
"""

import json
import networkx as nx

def load_graph_data():
    """Load the graph data from JSON file"""
    with open('complete_graph_data.json', 'r') as f:
        data = json.load(f)
    return data

def create_graph(data):
    """Create a NetworkX graph from the data"""
    G = nx.DiGraph()
    
    # Add nodes with attributes
    for node in data['nodes']:
        G.add_node(node['name'], node_class=node['class'])
    
    # Add edges with weights
    for edge in data['edges']:
        if 'weight' in edge and edge['weight'] and str(edge['weight']) != 'nan':
            G.add_edge(
                edge['source'], 
                edge['target'], 
                weight=float(edge['weight']),
                edge_type=edge.get('type', 'unknown')
            )
    
    return G

def test_shortest_path(G, source, target):
    """Test shortest path calculation"""
    try:
        path = nx.dijkstra_path(G, source, target, weight='weight')
        path_length = nx.dijkstra_path_length(G, source, target, weight='weight')
        
        print(f"\n{'='*80}")
        print(f"Shortest Path from {source} to {target}")
        print(f"{'='*80}")
        print(f"Total Distance: {path_length:.2f}")
        print(f"Number of Hops: {len(path) - 1}")
        print(f"\nPath:")
        
        for i, node in enumerate(path):
            if i == 0:
                print(f"  START: {node} ({G.nodes[node]['node_class']})")
            elif i == len(path) - 1:
                weight = G[path[i-1]][node]['weight']
                edge_type = G[path[i-1]][node]['edge_type']
                print(f"    └─[{weight}]─> {node} ({G.nodes[node]['node_class']}) - {edge_type}")
                print(f"  END: {node}")
            else:
                weight = G[path[i-1]][node]['weight']
                edge_type = G[path[i-1]][node]['edge_type']
                print(f"    └─[{weight}]─> {node} ({G.nodes[node]['node_class']}) - {edge_type}")
        
        print(f"{'='*80}\n")
        return True
        
    except nx.NetworkXNoPath:
        print(f"\nNo path exists between {source} and {target}")
        return False
    except Exception as e:
        print(f"\nError: {e}")
        return False

def main():
    print("\n🌲 Fraternity Family Tree - Graph Test\n")
    
    # Load data
    try:
        data = load_graph_data()
        G = create_graph(data)
        
        print(f"✅ Graph loaded successfully!")
        print(f"   - Total members: {len(G.nodes())}")
        print(f"   - Total connections: {len(G.edges())}")
        
        # Count edge types
        big_little = sum(1 for _, _, d in G.edges(data=True) if d.get('edge_type') == 'big-little')
        classmate = sum(1 for _, _, d in G.edges(data=True) if d.get('edge_type') == 'classmate')
        
        print(f"   - Big-Little edges: {big_little}")
        print(f"   - Classmate edges: {classmate}")
        
        # Test some interesting paths
        test_cases = [
            ("Neel Gandhi", "Sumesh Rawal"),  # PC to older generation
            ("Sreekar Nagulapalli", "Neel Gandhi"),  # Big to little
            ("Neil Bhagat", "Neel Gandhi"),  # Across many generations
            ("Atul Kamath", "Zahm Siyed"),  # Within same class (Alpha Zeta)
        ]
        
        print("\n" + "="*80)
        print("TESTING SHORTEST PATHS")
        print("="*80)
        
        for source, target in test_cases:
            test_shortest_path(G, source, target)
        
        # Show class statistics
        print("\n" + "="*80)
        print("CLASS STATISTICS")
        print("="*80)
        
        from collections import defaultdict
        class_counts = defaultdict(int)
        for node, data_node in G.nodes(data=True):
            class_counts[data_node.get('node_class', 'Unknown')] += 1
        
        print(f"\n{'Class':<20} {'Weight':<10} {'Members':<10}")
        print("-" * 40)
        for class_name in sorted(class_counts.keys(), key=lambda x: data['classWeights'].get(x, 999)):
            weight = data['classWeights'].get(class_name, 'N/A')
            count = class_counts[class_name]
            print(f"{class_name:<20} {str(weight):<10} {count:<10}")
        
        print("\n✅ All tests completed successfully!\n")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

