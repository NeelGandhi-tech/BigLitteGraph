# Fraternity Family Tree Visualization

An interactive web application to visualize the Big-Little family tree and class connections within the fraternity, with shortest path calculation between any two members.

## Features

- 🌲 **Interactive Graph Visualization**: Visual representation of all members connected through Big-Little relationships and within-class connections
- 🔍 **Shortest Path Finder**: Calculate and visualize the shortest path between any two members using Dijkstra's algorithm
- 📊 **Statistics Dashboard**: View comprehensive statistics about the family tree
- 👥 **Member Directory**: Browse all members with their class information
- 🎨 **Color-Coded Classes**: Each class has a unique color for easy identification
- ⚡ **Real-time Updates**: Interactive selections update the graph in real-time

## Graph Structure

### Edge Weights
The graph uses a weighted edge system where:
- **Mu** (oldest class) = Weight 1
- **Nu** = Weight 2
- **Xi** = Weight 3
- **Omicron** = Weight 4
- **Pi** = Weight 5
- **Rho** = Weight 6
- **Sigma** = Weight 7
- **Tau** = Weight 8
- **Upsilon** = Weight 9
- **Phi** = Weight 10
- **Chi** = Weight 11
- **Psi** = Weight 12
- **Alpha Alpha** = Weight 13
- **Alpha Beta** = Weight 14
- **Alpha Gamma** = Weight 15
- **Alpha Delta** = Weight 16
- **Alpha Epsilon** = Weight 17
- **Alpha Zeta** (PC) = Weight 18

### Edge Types
1. **Big-Little Relationships**: Directed edges from big to little with weights based on the target's class
2. **Classmate Connections**: Sequential connections within each class in alphabetical order (A → B → C)

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

1. **Clone or navigate to the repository**
   ```bash
   cd "/Users/neelgandhi/Desktop/Brother code"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify files**
   Make sure these files are present:
   - `graph_app.py` (main application)
   - `complete_graph_data.json` (graph data)
   - `requirements.txt` (dependencies)

4. **Run the application**
   ```bash
   streamlit run graph_app.py
   ```

5. **Access the app**
   The app will automatically open in your default browser at `http://localhost:8501`

## Usage

### Finding Shortest Paths

1. Open the app in your browser
2. Use the sidebar on the left to select:
   - **From**: Starting member
   - **To**: Target member
3. The graph will automatically update to show:
   - The shortest path highlighted in red
   - Source and target nodes enlarged
   - Path details in the sidebar (distance, hops, step-by-step breakdown)

### Exploring the Graph

- **Graph Visualization Tab**: Interactive graph with zoom, pan, and hover capabilities
  - Hover over nodes to see member names and classes
  - Hover over edges to see connection details (weight, type)
  
- **Graph Statistics Tab**: Overview of the entire family tree
  - Total members and connections
  - Big-Little vs. Classmate edge counts
  - Distribution of members by class

- **Members List Tab**: Searchable table of all members
  - Filter by name or class
  - See number of bigs and littles for each member

## Data Structure

The `complete_graph_data.json` file contains:
- **nodes**: Array of members with their class information
- **edges**: Array of connections (big-little and classmate) with weights
- **classWeights**: Mapping of class names to weights
- **summary**: Overall statistics

## Technologies Used

- **Streamlit**: Web application framework
- **NetworkX**: Graph data structure and algorithms (Dijkstra's shortest path)
- **Plotly**: Interactive graph visualization
- **Pandas**: Data manipulation and display

## Troubleshooting

### Port Already in Use
If port 8501 is already in use, run:
```bash
streamlit run graph_app.py --server.port 8502
```

### Module Not Found Errors
Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Graph Not Displaying
- Clear Streamlit cache: Press 'C' in the terminal running the app
- Refresh the browser page
- Check that `complete_graph_data.json` is in the same directory

## Project Structure

```
Brother code/
├── graph_app.py                 # Main Streamlit application
├── complete_graph_data.json     # Graph data (nodes, edges, weights)
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── nodes.csv                    # Source data: member list
├── big_little_relationships.csv # Source data: family tree
├── within_class_edges.csv       # Source data: class connections
└── class_summary.csv            # Source data: class info
```

## Contributing

This is a private project for fraternity use. For questions or issues, contact the repository owner.

## License

Private - All Rights Reserved

---

**Created by:** Neel Gandhi  
**Date:** November 2024  
**Purpose:** Visualizing fraternity family tree connections and relationships

