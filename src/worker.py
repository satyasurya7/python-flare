import sys
sys.path.insert(0, './vendor')


from fastapi import FastAPI, Request
from workers import WorkerEntrypoint


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        import asgi

        return await asgi.fetch(app, request.js_object, self.env)


app = FastAPI()


@app.get("/")
async def root():
    message = "This is an example of FastAPI with Jinja2 - go to /hi/<name> to see a template rendered"
    return {"message": message}