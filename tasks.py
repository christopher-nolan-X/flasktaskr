from invoke import task
from invocations.console import confirm


# push

@task
def test(c):
	result = c.run("nosetests -v", warn=True)
	if result.failed and not confirm("Tests failed. Continue?"):
		print("Aborted at user request.")

@task
def commit(c):
	message = input("Enter a git commit message: ")
	c.run("git add . && git commit -m '{}'".format(message))

@task
def push(c):
	c.run("git push origin master")

@task
def prepare(c):
	test(c)
	commit(c)
	push(c)


# deploy

# def pull(c):
# 	c.run("git pull origin master")

@task
def heroku(c):
	c.run("git push heroku master")

@task
def heroku_test(c):
	c.run("heroku run nosetests -v")

@task
def deploy(c):
	# pull()
	test()
	commit()
	heroku()
	heroku_test()

@task
def rollback(c):
	c.run("heroku rollback")