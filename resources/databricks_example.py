from databricks.sdk import WorkspaceClient

# Initialisiere den Databricks-Client (nutzt automatisch die Databricks-Extension für VS Code)
db_client = WorkspaceClient()

# Definiere das Notebook als eine einfache Python-Zelle
notebook_content = """
# Databricks Notebook
print('Hello from Databricks Notebook!')
"""

# Speicher das Notebook in Databricks
workspace_path = "/Users/<your-username>/example_notebook"
db_client.workspace.import_(
    path=workspace_path, format="SOURCE", language="PYTHON", content=notebook_content.encode("utf-8")
)
print(f"Notebook wurde hochgeladen nach {workspace_path}")

# Erstelle und starte einen Job für das Notebook
job_config = {
    "name": "ExampleNotebookJob",
    "tasks": [
        {
            "task_key": "RunNotebook",
            "notebook_task": {"notebook_path": workspace_path},
            "new_cluster": {"spark_version": "11.3.x-scala2.12", "node_type_id": "Standard_DS3_v2", "num_workers": 1},
        }
    ],
}

job = db_client.jobs.create(**job_config)
print(f"Job {job.job_id} wurde erstellt und das Notebook wird ausgeführt.")
