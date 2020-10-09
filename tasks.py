from invoke import task


@task
def test(c):
    c.run('pytest')


@task
def lint(c):
    c.run('flake8 . --count --show-source --statistics')
