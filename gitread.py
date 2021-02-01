#from github import Github
from git import Repo
import os
import datetime
import git
import knowledge_base


def git(reponame):
	#g = Github(base_url="https://github.com/HrishikeshVish")
	giturl = knowledge_base.getGitUrl(reponame)
	if giturl:

		try:
			Repo.clone_from(giturl+reponame, reponame)
			repo = Repo(reponame)
			o = repo.remotes.origin
			o.pull()

			master = repo.head.reference
			print(master.log())
			"""for repo in g.get_user().get_repos():
			print(repo.name)
			"""
		except:
			repo = Repo(reponame)
			o = repo.remotes.origin
			o.pull()

			master = repo.head.reference

			print(master.log())
	else:
		pass
