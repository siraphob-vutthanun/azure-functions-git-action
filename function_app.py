import json

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="hello", methods=["GET", "POST"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name")

    if not name:
        try:
            body = req.get_json()
        except ValueError:
            body = None

        if isinstance(body, dict):
            name = body.get("name")

    payload = {
        "message": f"Hello{name and f', {name}' or ''}!",
        "usage": {
            "get": "/api/hello?name=Copilot",
            "post": {"name": "Copilot"},
        },
    }

    return func.HttpResponse(
        body=json.dumps(payload),
        status_code=200,
        mimetype="application/json",
    )
