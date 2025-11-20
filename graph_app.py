import streamlit as st
import json
import networkx as nx
import plotly.graph_objects as go
from collections import defaultdict
import pandas as pd

# Page configuration
st.set_page_config(page_title="Fraternity Family Tree", layout="wide", page_icon="🌲")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stTitle {
        font-size: 3rem !important;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .path-info {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_graph_data():
    """Load the graph data from JSON file"""
    with open('complete_graph_data.json', 'r') as f:
        data = json.load(f)
    return data

@st.cache_resource
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

def get_node_positions(G):
    """Calculate node positions using spring layout for better visualization"""
    # Use spring layout with custom parameters for better spacing
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    return pos

def create_plotly_graph(G, pos, highlight_path=None, source_node=None, target_node=None):
    """Create an interactive Plotly visualization of the graph"""
    
    # Create edge traces
    edge_traces = []
    
    # Regular edges
    edge_x = []
    edge_y = []
    edge_hover = []
    
    # Highlighted path edges
    highlight_edge_x = []
    highlight_edge_y = []
    highlight_edge_hover = []
    
    for edge in G.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        weight = edge[2].get('weight', 1)
        edge_type = edge[2].get('edge_type', 'unknown')
        
        # Check if this edge is in the highlighted path
        is_highlighted = False
        if highlight_path and len(highlight_path) > 1:
            for i in range(len(highlight_path) - 1):
                if edge[0] == highlight_path[i] and edge[1] == highlight_path[i+1]:
                    is_highlighted = True
                    break
        
        hover_text = f"{edge[0]} → {edge[1]}<br>Weight: {weight}<br>Type: {edge_type}"
        
        if is_highlighted:
            highlight_edge_x.extend([x0, x1, None])
            highlight_edge_y.extend([y0, y1, None])
            highlight_edge_hover.append(hover_text)
        else:
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
            edge_hover.append(hover_text)
    
    # Regular edges trace
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='text',
        mode='lines',
        name='Edges',
        showlegend=True
    )
    
    # Highlighted path edges trace
    highlight_edge_trace = go.Scatter(
        x=highlight_edge_x, y=highlight_edge_y,
        line=dict(width=4, color='#ff0000'),
        hoverinfo='text',
        mode='lines',
        name='Shortest Path',
        showlegend=True
    )
    
    # Create node traces
    node_x = []
    node_y = []
    node_text = []
    node_color = []
    node_size = []
    
    class_colors = {
        'Mu': '#e6194b', 'Nu': '#3cb44b', 'Xi': '#ffe119', 'Omicron': '#4363d8',
        'Pi': '#f58231', 'Rho': '#911eb4', 'Sigma': '#46f0f0', 'Tau': '#f032e6',
        'Upsilon': '#bcf60c', 'Phi': '#fabebe', 'Chi': '#008080', 'Psi': '#e6beff',
        'Alpha Alpha': '#9a6324', 'Alpha Beta': '#fffac8', 'Alpha Gamma': '#800000',
        'Alpha Delta': '#aaffc3', 'Alpha Epsilon': '#808000', 'Alpha Zeta': '#ffd8b1',
        'Unknown': '#000000'
    }
    
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        
        node_class = G.nodes[node].get('node_class', 'Unknown')
        node_text.append(f"{node}<br>Class: {node_class}")
        
        # Color based on class
        node_color.append(class_colors.get(node_class, '#000000'))
        
        # Size based on whether it's source, target, or in path
        if node == source_node or node == target_node:
            node_size.append(25)
        elif highlight_path and node in highlight_path:
            node_size.append(18)
        else:
            node_size.append(12)
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=[n.split()[0] for n in G.nodes()],  # Show first name only
        textposition="top center",
        textfont=dict(size=8),
        marker=dict(
            size=node_size,
            color=node_color,
            line=dict(width=2, color='white'),
        ),
        hovertext=node_text,
        name='Members',
        showlegend=True
    )
    
    # Create figure
    fig = go.Figure(data=[edge_trace, highlight_edge_trace, node_trace])
    
    fig.update_layout(
        title=dict(text="Fraternity Family Tree Graph", font=dict(size=20)),
        showlegend=True,
        hovermode='closest',
        margin=dict(b=20, l=5, r=5, t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white',
        height=800
    )
    
    return fig

def calculate_shortest_path(G, source, target):
    """Calculate the shortest path between two nodes using Dijkstra's algorithm"""
    try:
        path = nx.dijkstra_path(G, source, target, weight='weight')
        path_length = nx.dijkstra_path_length(G, source, target, weight='weight')
        
        # Get edge details along the path
        path_details = []
        for i in range(len(path) - 1):
            edge_data = G[path[i]][path[i+1]]
            path_details.append({
                'from': path[i],
                'to': path[i+1],
                'weight': edge_data['weight'],
                'type': edge_data['edge_type']
            })
        
        return path, path_length, path_details
    except nx.NetworkXNoPath:
        return None, None, None

def main():
    st.title("🌲 Fraternity Family Tree Visualization")
    
    # Load data
    try:
        data = load_graph_data()
        G = create_graph(data)
        
        st.success(f"✅ Graph loaded successfully! {len(G.nodes())} members, {len(G.edges())} connections")
        
        # Sidebar for controls
        st.sidebar.header("🔍 Find Shortest Path")
        st.sidebar.markdown("---")
        
        # Get list of all members
        all_members = sorted(list(G.nodes()))
        
        # Member selection
        col1, col2 = st.sidebar.columns(2)
        with col1:
            source_member = st.selectbox(
                "From:",
                all_members,
                index=all_members.index("Neel Gandhi") if "Neel Gandhi" in all_members else 0,
                key="source"
            )
        
        with col2:
            target_member = st.selectbox(
                "To:",
                all_members,
                index=all_members.index("Sumesh Rawal") if "Sumesh Rawal" in all_members else 1,
                key="target"
            )
        
        # Calculate shortest path
        path = None
        path_length = None
        path_details = None
        
        if source_member and target_member and source_member != target_member:
            path, path_length, path_details = calculate_shortest_path(G, source_member, target_member)
        
        # Display path information in sidebar
        if path:
            st.sidebar.markdown("---")
            st.sidebar.markdown("### 📊 Path Information")
            st.sidebar.metric("Total Distance", f"{path_length:.1f}")
            st.sidebar.metric("Hops", len(path) - 1)
            
            st.sidebar.markdown("### 🛤️ Path Steps")
            for i, detail in enumerate(path_details, 1):
                st.sidebar.markdown(f"""
                **Step {i}:**  
                {detail['from']} → {detail['to']}  
                Weight: {detail['weight']} | Type: {detail['type']}
                """)
        elif source_member == target_member:
            st.sidebar.warning("⚠️ Please select different members")
        elif source_member and target_member:
            st.sidebar.error("❌ No path exists between these members")
        
        # Main content area
        tab1, tab2, tab3 = st.tabs(["📈 Graph Visualization", "📋 Graph Statistics", "👥 Members List"])
        
        with tab1:
            # Calculate positions
            pos = get_node_positions(G)
            
            # Create and display graph
            fig = create_plotly_graph(G, pos, path, source_member, target_member)
            st.plotly_chart(fig, use_container_width=True)  # plotly_chart still uses use_container_width
            
            # Display path summary below graph
            if path and len(path) > 1:
                st.markdown(f"""
                <div class="path-info">
                    <h3>🎯 Shortest Path Found!</h3>
                    <p><strong>From:</strong> {source_member} ({G.nodes[source_member]['node_class']})</p>
                    <p><strong>To:</strong> {target_member} ({G.nodes[target_member]['node_class']})</p>
                    <p><strong>Total Distance:</strong> {path_length:.2f}</p>
                    <p><strong>Path:</strong> {' → '.join(path)}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with tab2:
            st.header("Graph Statistics")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Members", len(G.nodes()))
            with col2:
                st.metric("Total Connections", len(G.edges()))
            with col3:
                big_little_edges = sum(1 for _, _, d in G.edges(data=True) if d.get('edge_type') == 'big-little')
                st.metric("Big-Little Edges", big_little_edges)
            with col4:
                classmate_edges = sum(1 for _, _, d in G.edges(data=True) if d.get('edge_type') == 'classmate')
                st.metric("Classmate Edges", classmate_edges)
            
            # Class distribution
            st.subheader("Members by Class")
            class_counts = defaultdict(int)
            for node, data_node in G.nodes(data=True):
                class_counts[data_node.get('node_class', 'Unknown')] += 1
            
            class_df = pd.DataFrame([
                {'Class': k, 'Members': v, 'Weight': data['classWeights'].get(k, None)}
                for k, v in sorted(class_counts.items(), key=lambda x: data['classWeights'].get(x[0], 999))
            ])
            
            st.dataframe(class_df, width='stretch')
        
        with tab3:
            st.header("All Members")
            
            # Create members dataframe
            members_data = []
            for node in sorted(G.nodes()):
                node_class = G.nodes[node].get('node_class', 'Unknown')
                in_degree = G.in_degree(node)
                out_degree = G.out_degree(node)
                members_data.append({
                    'Name': node,
                    'Class': node_class,
                    'Weight': data['classWeights'].get(node_class, None),
                    'Bigs': in_degree,
                    'Littles': out_degree
                })
            
            members_df = pd.DataFrame(members_data)
            st.dataframe(members_df, width='stretch', height=600)
            
    except FileNotFoundError:
        st.error("❌ Error: 'complete_graph_data.json' file not found!")
        st.info("Please make sure the graph data file is in the same directory as this script.")
    except Exception as e:
        st.error(f"❌ Error loading graph: {str(e)}")
        st.exception(e)

if __name__ == "__main__":
    main()


