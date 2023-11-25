from pathlib import Path
import shutil
import stat
from typing import Any
import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session
def book(session: nox.Session):
    session.install("copier", "copier-template-tester")

    root = Path(".ctt/defaults")
    if root.is_dir():
        session.log(f"Removing directory: {root}")
        shutil.rmtree(root, onerror=on_rm_error)

    session.run("ctt", silent=True)

    with session.chdir(root):
        session.run(
            "git",
            "init",
            external=True,
            silent=True,
        )

        session.run(
            "git",
            "commit",
            "--allow-empty",
            "-m",
            "Initial commit",
            external=True,
            silent=True,
        )

        session.run(
            "copier",
            "copy",
            "gh:object-Object/hexdoc-hexcasting-template",
            ".",
            "--answers-file",
            ".hexdoc-template-inputs.yml",
            "--skip",
            ".gitignore",
            "--defaults",
            silent=True,
        )

        session.install(".[dev]")

        session.run("hexdoc", "serve")


def on_rm_error(func: Any, path: str, exc_info: Any):
    # from: https://stackoverflow.com/questions/4829043/how-to-remove-read-only-attrib-directory-with-python-in-windows
    path_ = Path(path)
    path_.chmod(stat.S_IWRITE)
    path_.unlink()
