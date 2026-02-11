
# Azure Functions (Python) + GitHub Actions

Minimal Azure Functions (Python) project with an HTTP trigger and a GitHub Actions workflow that deploys to an Azure Function App running on Linux (serverless/Consumption).

## Local run

Prereqs:
- Python 3.11
- Azure Functions Core Tools v4 (`func`)

Steps:
1. Create/activate a virtualenv.
2. Install deps: `pip install -r requirements.txt`
3. Start: `func start`

Test:
- `GET http://localhost:7071/api/hello?name=Copilot`

## Deploy (GitHub Actions)

This repo includes a workflow: `.github/workflows/azure-functions-deploy.yml`.

In your GitHub repo settings, add secrets:
- `AZURE_FUNCTIONAPP_NAME`: your Azure Function App name
- `AZURE_FUNCTIONAPP_PUBLISH_PROFILE`: publish profile XML for that Function App

Then push to the `main` branch (or run the workflow manually).

## Project entrypoint

Azure Functions discovers the app in `function_app.py`.

