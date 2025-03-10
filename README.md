# Unicon CLI Tool Template

This repository is a template using the custom Unicon CLI Tool. It provides a foundation to create and customize your own projects.

## Setup Instructions

## 1. Install Visual Studio Code.

## 2. Install Docker Desktop.

## 3. Install the following Visual Studio Code extensions:
    - Docker
    - Dev Containers

## 4. Create your own repository using the template  
   Go to GitHub and click the "Use this template" button to create your own repository based on this template and clone it to a local folder afterwards.

   ### Cloning a GitHub Repository Using Visual Studio Code

   Follow the steps below to clone a GitHub repository using Visual Studio Code (VS Code):

   #### Prerequisites
   - **Visual Studio Code** installed on your computer.
   - **Git** installed on your computer.
   - **GitHub Account** (optional, but needed if you're cloning private repositories).

   #### Step 1: Open Visual Studio Code
   1. Launch **Visual Studio Code**.

   #### Step 2: Open the Command Palette
   1. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) to open the **Command Palette**.

   #### Step 3: Clone the Repository
   1. In the Command Palette, type **Git: Clone** and select it from the list of options.
   2. Alternatively, click on the **Source Control** icon on the left sidebar and then select **Clone Repository**.

   #### Step 4: Provide the Repository URL
   1. You will be prompted to enter the **repository URL**.
      - Go to the GitHub repository page in your browser.
      - Click on the **Code** button and copy the URL (HTTPS or SSH).
      - Paste the URL into VS Code when prompted.

   #### Step 5: Choose a Folder for the Clone
   1. After pasting the URL, you will be prompted to choose a local folder where you want to clone the repository.
   2. Select or create a folder on your computer to store the repository.

   #### Step 6: Open the Cloned Repository
   1. Once the repository is cloned, VS Code will ask if you want to open the cloned repository. Click **Open** to open the repository in VS Code.

   #### Step 7: Verify the Cloning Process
   1. Check the **Explorer** pane in VS Code to see if the repository files are listed.
   2. You should now be able to make changes, commit, and push updates to the cloned repository using VS Code's built-in Git features.


   #### Additional Notes:
   - If you encounter any authentication prompts, use your **GitHub credentials** or an **SSH key** (for private repositories).
   - To push changes, use the **Source Control** tab in VS Code or run Git commands from the integrated terminal.

   That's it! You have successfully cloned a GitHub repository using Visual Studio Code.


## 5. Start Docker Desktop  
   Make sure Docker Desktop is installed and running on your computer.

## 6. Build and open the program in the Docker container  
   Open Visual Studio Code and press Ctrl + Shift + P to open the command palette. Search for the command "Dev Containers: Rebuild and Reopen in Container" and select it.

## 7. Create a profile  
   Once the container is built, open a new terminal (by clicking the "+" icon on the right of the console or by pressing "Ctrl + Shift + ö") and type `unicon` in the console and follow the instructions to create a profile.

## 8. Log into a Databricks profile  
   To log into a Databricks profile, click on the Databricks extension icon on the left side of Visual Studio Code and select "Log in". Then choose the profile you want to log in with.
   Afterwarts click on "Clusters" and select the cluster you want to use.
   Then select "venv" and click on the "default_python_venv" or select a custom one.

## Modify Python venv and Databricks-Connect Version

To modify the Python version of your virtual environment (venv) and update `databricks-connect` for a different Databricks cluster, follow these steps:

0. Find the Required Python and Databricks-Connect Versions
   Refer to the official documentation to identify the specific Python and `databricks-connect` versions required for each Databricks Runtime:  
   - Databricks Runtime Release Notes: https://docs.databricks.com/aws/en/release-notes/runtime/  
   - Databricks Connect Release Notes: https://docs.databricks.com/aws/en/release-notes/dbconnect/

1. Update the Dockerfile
   Open `.devcontainer/Dockerfile` and modify the Python version for the Docker container. For example, change the line:  
   FROM python:3.12  
   to  
   FROM python:3.10

2. Modify the Python Version for the Virtual Environment
   Update the command for creating the venv. Change the line in `.devcontainer/Dockerfile`:  
   RUN uv venv --python '>=3.12' ...  
   to  
   RUN uv venv --python '==3.10' ...

3. Update the `databricks-connect` Version
   In `.devcontainer/requirements.txt`, modify the `databricks-connect` version. Change the version to match the one required for your selected runtime, for example:  
   databricks-connect==13.3.5

4. Rebuild the Container
   After modifying the Dockerfile and requirements, rebuild the container to apply the changes. You can then select the new cluster to use with your updated Python environment and Databricks Connect version.

## Incorporate Changes from the Template

   If you want to update your project with the latest changes from the template repository, follow these steps. This ensures that your project remains up to date while keeping your modifications intact.

   ### Step 1: Add the Template Repository as a Remote (If Not Already Done)
   If you haven't already added the template as a remote ("template" beeing the name), add it by running:
   ```
   git remote add template https://github.com/wladimirbix/VSC-Development-Environment
   ```
   Verify that the remote has been added:
   ```
   git remote -v
   ```

   ### Step 2: Fetch the Latest Changes from the Template
   Pull the latest changes from the template repository:
   ```
   git fetch template
   ```
   This will download all updates from the template but won't apply them yet.

   ### Step 3: Compare the Changes Before Applying
   Before applying the changes, you can check the differences between your branch and the template:
   ```
   git diff main template/main
   ```

   ### Step 4: Rebase Your Code on Top of the Template
   To apply the template updates while preserving your own changes:
   ```
   git rebase template/main
   ```
   This will attempt to apply your changes on top of the latest template updates.

   ### Step 5: Resolving Merge Conflicts in VS Code
   If there are conflicts, VS Code will highlight them automatically. Follow these steps to resolve them:
   1. Open VS Code and check the Source Control (Git) panel (`Ctrl + Shift + G`).
   2. Look for files marked with `conflict`.
   3. Open a conflicted file; VS Code will show options like:
      - Accept Current Change: Keeps your version.
      - Accept Incoming Change: Uses the template's version.
      - Accept Both Changes: Merges both versions.
   4. Manually edit the file if needed and remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
   5. After resolving all conflicts, stage the changes:
      ```
      git add .
      ```
   6. Continue the rebase:
      ```
      git rebase --continue
      ```

   If you want to cancel the rebase at any point:
   ```
   git rebase --abort
   ```

   ### Step 6: Push the Updated Code
   Once the rebase is complete, push your updated branch:
   ```
   git push origin main --force
   ```
   **Warning:** This will overwrite the remote branch with the rebased version.

   Now your project includes the latest updates from the template while keeping your own changes.


## Important Notes

- The `resources` folder contains code templates.
- The `src` folder is where the user's code goes.
- The `test` folder contains automated tests.
- The `tmp` folder contains temporary files and cache files.

### Custom Project Dependencies

If you need to install additional Python packages specific to your project, add them to the `.devcontainer/requirements.txt` file. 

These dependencies will be installed during the Docker build process. 

#### Example:
To add a package, that isnt already in the `requirements.txt` simply include it in the file, like so:

requests==2.26.0 
matplotlib>=3.4.0
pandas
NumPy

Once added, rebuild the container to install these custom dependencies.


## Useful and Commonly Used VSC Shortcuts

### General:
- Command Palette: `Ctrl + Shift + P` (Windows/Linux) / `Cmd + Shift + P` (Mac)
- Open Settings: `Ctrl + ,` (Windows/Linux) / `Cmd + ,` (Mac)
- Toggle Sidebar: `Ctrl + B` (Windows/Linux) / `Cmd + B` (Mac)

### File Management:
- New File: `Ctrl + N` (Windows/Linux) / `Cmd + N` (Mac)
- Open File: `Ctrl + O` (Windows/Linux) / `Cmd + O` (Mac)
- Save File: `Ctrl + S` (Windows/Linux) / `Cmd + S` (Mac)
- Close File: `Ctrl + W` (Windows/Linux) / `Cmd + W` (Mac)

### Editing:
- Cut Line: `Ctrl + X` (Windows/Linux) / `Cmd + X` (Mac)
- Copy Line: `Ctrl + C` (Windows/Linux) / `Cmd + C` (Mac)
- Paste: `Ctrl + V` (Windows/Linux) / `Cmd + V` (Mac)
- Undo: `Ctrl + Z` (Windows/Linux) / `Cmd + Z` (Mac)
- Redo: `Ctrl + Y` (Windows/Linux) / `Cmd + Shift + Z` (Mac)
- Find: `Ctrl + F` (Windows/Linux) / `Cmd + F` (Mac)
- Replace: `Ctrl + H` (Windows/Linux) / `Cmd + Option + F` (Mac)

### Navigation:
- Go to File: `Ctrl + P` (Windows/Linux) / `Cmd + P` (Mac)
- Go to Definition: `F12`
- Go to Line: `Ctrl + G` (Windows/Linux) / `Cmd + G` (Mac)

### Multi-Cursor and Selection:
- Add Cursor Below: `Ctrl + Alt + Down Arrow` (Windows/Linux) / `Cmd + Option + Down Arrow` (Mac)
- Add Cursor Above: `Ctrl + Alt + Up Arrow` (Windows/Linux) / `Cmd + Option + Up Arrow` (Mac)
- Select All Occurrences: `Ctrl + Shift + L` (Windows/Linux) / `Cmd + Shift + L` (Mac)

### Code Formatting and Refactoring:
- Format Document: `Shift + Alt + F` (Windows/Linux) / `Shift + Option + F` (Mac)
- Rename Symbol: `F2`
- Quick Fix: `Ctrl + .` (Windows/Linux) / `Cmd + .` (Mac)

### Terminal:
- Toggle Terminal: `Ctrl + ` (Windows/Linux) / `Cmd + ` (Mac)
- Create New Terminal: `Ctrl + Shift + ` (Windows/Linux) / `Cmd + Shift + ` (Mac)

### Debugging:
- Start Debugging: `F5`
- Step Over: `F10`
- Step Into: `F11`
- Step Out: `Shift + F11`

### Miscellaneous:
- Zen Mode: `Ctrl + K Z` (Windows/Linux) / `Cmd + K Z` (Mac)
- Toggle Comment: `Ctrl + /` (Windows/Linux) / `Cmd + /` (Mac)

