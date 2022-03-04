import invoke


@invoke.task
def init(c):
    invoke.run("sh init.sh")


@invoke.task
def delete(c):
    invoke.run("sh delete.sh")


@invoke.task
def build(c):
    invoke.run(
        "poetry export -f requirements.txt --without-hashes --output requirements.txt"
    )
    invoke.run("find app/functions -type d -mindepth 1 -exec cp requirements.txt {} \;")
    invoke.run("poetry run sam build -p -t app/template.yaml")


@invoke.task
def start(c):
    build(c)
    invoke.run(
        "poetry run sam local start-api --env-vars app/env.json --docker-network sam-local-tools_sam-local-tools"
    )
