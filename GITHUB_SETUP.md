# GitHub Repository Setup Guide

## Step 1: Create a Private GitHub Repository

1. Go to [GitHub](https://github.com) and log in to your account

2. Click the **"+"** icon in the top-right corner and select **"New repository"**

3. Configure your repository:
   - **Repository name**: `fraternity-family-tree` (or your preferred name)
   - **Description**: "Interactive visualization of fraternity Big-Little family tree with shortest path finder"
   - **Visibility**: Select **"Private"** ⚠️ (Important!)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)

4. Click **"Create repository"**

## Step 2: Link Your Local Repository to GitHub

After creating the repository, GitHub will show you instructions. Follow these steps:

```bash
cd "/Users/neelgandhi/Desktop/Brother code"

# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/fraternity-family-tree.git

# Verify the remote was added
git remote -v

# Push your code to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Invite Collaborators (Share the Repository)

To share the private repository with specific people:

1. Go to your repository on GitHub: `https://github.com/YOUR_USERNAME/fraternity-family-tree`

2. Click on **"Settings"** (top menu of the repository)

3. In the left sidebar, click **"Collaborators and teams"**

4. Click **"Add people"** (green button)

5. Enter the GitHub username or email of the person you want to share with

6. Select their permission level:
   - **Read**: Can view and clone the repository
   - **Write**: Can view, clone, and push changes
   - **Admin**: Full control

7. Click **"Add [username] to this repository"**

8. They will receive an email invitation to access the repository

## Step 4: Share the Repository Link

Once you've invited collaborators, share this link format with them:
```
https://github.com/YOUR_USERNAME/fraternity-family-tree
```

## Alternative: Generate a Personal Access Token (PAT)

If you have trouble pushing with HTTPS, you may need to create a Personal Access Token:

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name (e.g., "Fraternity Tree App")
4. Select scopes: Check **"repo"** (full control of private repositories)
5. Click "Generate token"
6. **COPY THE TOKEN IMMEDIATELY** (you won't see it again!)
7. Use this token as your password when pushing to GitHub

## Quick Commands Reference

```bash
# Check current status
git status

# Add new/modified files
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push

# Pull latest changes
git pull

# View commit history
git log --oneline
```

## Repository URL for Dailies

After pushing to GitHub, your repository URL will be:
```
https://github.com/YOUR_USERNAME/fraternity-family-tree
```

Post this link in your dailies tonight! 🎉

## Cloning the Repository (For Others)

Once collaborators have access, they can clone the repository:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/fraternity-family-tree.git

# Navigate to the directory
cd fraternity-family-tree

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run graph_app.py
```

## Troubleshooting

### Authentication Issues
If you get authentication errors:
- Use SSH instead: Configure SSH keys and use `git@github.com:YOUR_USERNAME/fraternity-family-tree.git`
- Or use a Personal Access Token (see above)

### Push Rejected
If `git push` is rejected:
```bash
git pull --rebase origin main
git push
```

### Need to Update Remote URL
```bash
git remote set-url origin https://github.com/NEW_USERNAME/fraternity-family-tree.git
```

## Security Note

⚠️ **Important**: This is a PRIVATE repository containing personal information. Do not:
- Make it public
- Share the link with unauthorized people
- Post code snippets publicly that contain member names
- Commit any sensitive credentials or API keys

---

**Questions?** Check the [GitHub Docs](https://docs.github.com) or reach out for help!





