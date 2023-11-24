from pathlib import Path
import shutil
import nox

nox.options.reuse_existing_virtualenvs = True

@nox.session
def ctt(session: nox.Session):
    session.install("copier-template-tester")
    
    for directory in [".ctt/defaults"]:
        if Path(directory).is_dir():
            session.log(f"Removing directory: {directory}")
            shutil.rmtree(directory)

    session.run("ctt")
