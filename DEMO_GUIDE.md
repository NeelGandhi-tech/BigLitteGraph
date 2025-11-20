# Demo Guide for Video Recording

## Quick Start for Demo

### 1. Starting the App (30 seconds)

```bash
cd "/Users/neelgandhi/Desktop/Brother code"
streamlit run graph_app.py
```

The app will automatically open in your browser at `http://localhost:8501`

### 2. Demo Script for Video (2-3 minutes)

#### Introduction (15 seconds)
"Hi everyone! Tonight I'm sharing my fraternity family tree visualization app. This interactive tool shows all our Big-Little relationships and class connections, and can find the shortest path between any two members."

#### Show the Graph (30 seconds)
- **Point out the visualization**: "Here you can see the complete graph with all members as nodes"
- **Hover over nodes**: "Each node represents a member, color-coded by their class"
- **Hover over edges**: "Edges show connections - either Big-Little relationships or within-class connections"
- **Zoom and pan**: "The graph is fully interactive - you can zoom and pan to explore"

#### Demonstrate Shortest Path (60 seconds)
1. **Example 1: Big to Little**
   - Select "Sreekar Nagulapalli" (From) and "Neel Gandhi" (To)
   - "Here we can see a direct Big-Little connection with a distance of 14"
   
2. **Example 2: Across Generations**
   - Select "Neil Bhagat" (From) and "Neel Gandhi" (To)
   - "This path goes through 7 hops across multiple generations and classes"
   - "The red highlighted path shows the optimal route"
   - Show the step-by-step breakdown in the sidebar

3. **Example 3: Within Class**
   - Select two members from Alpha Zeta (e.g., "Atul Kamath" to "Reyansh Pallikonda")
   - "Members of the same class are connected alphabetically"

#### Show Additional Features (30 seconds)
- **Statistics Tab**: 
  - Click "Graph Statistics"
  - "Here we have metrics about the entire family tree"
  - Show members by class table
  
- **Members List Tab**:
  - Click "Members List"
  - "A searchable directory of all members with their class information"

#### Wrap Up (15 seconds)
"The app uses Dijkstra's algorithm to find the shortest weighted path between any two members. The weights are based on class seniority - Mu has weight 1, and Alpha Zeta (our PC) has weight 18. The code is available in the GitHub repository I'm sharing. Thanks for watching!"

## Key Features to Highlight

✅ **Interactive Graph Visualization**
- Zoom, pan, hover for details
- Color-coded by class
- Clear Big-Little and classmate relationships

✅ **Shortest Path Finder**
- Select any two members
- Algorithm finds optimal route
- Visual highlighting of path
- Detailed step-by-step breakdown

✅ **Graph Statistics**
- Total members and connections
- Distribution by class
- Edge type breakdown

✅ **Member Directory**
- Complete searchable list
- Class information
- Big/Little counts

## Recording Tips

### Screen Recording (Mac)
- **Press**: `Cmd + Shift + 5`
- Select "Record Selected Portion" or "Record Entire Screen"
- Click "Record"
- When done, click Stop button in menu bar or press `Cmd + Control + Esc`
- Video saves to Desktop

### During Recording
- Use cursor to point at interesting features
- Speak clearly and at a moderate pace
- Don't rush - take time to show the features
- If you make a mistake, just start over!

### Good Practices
- Close unnecessary tabs/windows
- Use fullscreen for the app (browser)
- Make sure your browser is maximized
- Disable notifications before recording

## Test Paths to Demonstrate

| From | To | Why It's Interesting |
|------|----|--------------------|
| Sreekar Nagulapalli | Neel Gandhi | Direct Big-Little (your big!) |
| Neil Bhagat | Neel Gandhi | Long path across generations |
| Kshitij Shah | Atul Kamath | Nu to Alpha Zeta (oldest to newest) |
| Atul Kamath | Zahm Siyed | Within same class (alphabetical) |

## After Demo

1. **Push to GitHub** (if you haven't already):
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/fraternity-family-tree.git
   git push -u origin main
   ```

2. **Share in Dailies**:
   - Post the GitHub repository link
   - Attach or link the demo video
   - Brief description of what you built

## Troubleshooting During Demo

**If app won't start:**
```bash
# Check if another instance is running
pkill -f "streamlit run"
# Try again
streamlit run graph_app.py
```

**If graph looks messy:**
- Use the graph controls to zoom out
- Refresh the page (browser)

**If path isn't found:**
- Remember: Graph is directed (Big → Little)
- Try reversing the selection
- Some paths may not exist

---

Good luck with your demo! 🎉





