from invoke import task

@task
def start(ctx):
    ctx.run('python3 src/__init__.py', pty=True)