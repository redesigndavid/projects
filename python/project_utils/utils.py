import os
import subprocess

# auxiliary
def run_cmd(cmd):
    """wrapper to for running commands."""
    return subprocess.call(cmd, env=os.environ, shell=True)


def mkdirs(dirs, path_to):
    """convenient failure free mkdir utility."""
    for dir in dirs:
        path = os.path.join(path_to, dir)
        if not os.path.exists(path):
            os.makedirs(path)


def get_projects_base():
    """return a path to where projects are stored."""
    return os.path.join(os.path.expanduser('~'), 'projects')


def get_project_path(projname):
    """build project path and return it."""
    return os.path.join(get_projects_base(), projname)


def get_generics_path():
    """return path to generics."""
    return os.path.join(get_project_path('projects'), 'generics')


def list_projects():
    """return a list of available projects."""
    project_basedir = get_projects_base()
    projects = []
    for project in os.listdir(project_basedir):
        environmentfile = os.path.join(project_basedir,
                                       project,
                                       '.environment')
        if os.path.exists(environmentfile):
            projects.append(project)
    return projects
