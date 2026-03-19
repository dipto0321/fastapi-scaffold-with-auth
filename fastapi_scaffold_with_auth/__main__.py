"""CLI entry point for fastapi_scaffold_with_auth."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def _project_root() -> Path:
    """Return repository root when installed from source or wheel."""
    return Path(__file__).resolve().parents[1]


def _copy_template(destination: Path) -> None:
    """Copy the bundled example project into destination."""
    source = _project_root() / "example_project"
    if not source.exists():
        raise FileNotFoundError("Template source 'example_project' not found.")

    shutil.copytree(source, destination)


def build_parser() -> argparse.ArgumentParser:
    """Build CLI parser."""
    parser = argparse.ArgumentParser(
        prog="python -m fastapi_scaffold_with_auth",
        description="Scaffold a FastAPI project with auth boilerplate.",
    )

    subparsers = parser.add_subparsers(dest="command")

    scaffold = subparsers.add_parser(
        "scaffold",
        help="Create a new project from the bundled template.",
    )
    scaffold.add_argument("name", help="Directory name for the new project.")
    scaffold.add_argument(
        "--force",
        action="store_true",
        help="Overwrite destination if it already exists.",
    )

    return parser


def cmd_scaffold(name: str, force: bool) -> int:
    """Handle scaffold command."""
    destination = Path.cwd() / name

    if destination.exists():
        if not force:
            print(
                f"Error: destination '{destination}' already exists. "
                "Use --force to overwrite.",
                file=sys.stderr,
            )
            return 1
        shutil.rmtree(destination)

    try:
        _copy_template(destination)
    except Exception as exc:
        print(f"Error: failed to scaffold project: {exc}", file=sys.stderr)
        return 1

    print(f"Created project at: {destination}")
    print("Next steps:")
    print(f"  cd {name}")
    print("  uv venv && source .venv/bin/activate")
    print("  uv pip install -e '.[dev]'")
    print("  alembic upgrade head")
    print("  fastapi dev app/main.py")
    return 0


def main() -> int:
    """CLI main."""
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "scaffold":
        return cmd_scaffold(args.name, args.force)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
