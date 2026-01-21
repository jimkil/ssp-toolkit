from __future__ import annotations

from pathlib import Path

from loguru import logger


def _find_project_root(
    start: Path, marker_files: tuple[str, ...] = ("pyproject.toml", ".git")
) -> Path:
    current = start.resolve()
    for parent in (current, *current.parents):
        if any((parent / name).exists() for name in marker_files):
            return parent
    # Fallback: assume .../src/tools/<this_file> and root is 3 levels up
    return start.resolve().parents[2]


def setup_logging() -> None:
    """
    Adds:
      - <root>/auditlogs/audit.log
      - <root>/error.log
    """
    root = _find_project_root(Path(__file__).parent)
    audit_dir = root / "auditlogs"
    audit_dir.mkdir(parents=True, exist_ok=True)

    audit_path = audit_dir / "audit.log"
    error_path = root / "error.log"

    logger.remove()

    # Audit sink (everything, adjust level if you want less noise)
    logger.add(
        str(audit_path),
        level="INFO",
        enqueue=True,
        backtrace=True,
        diagnose=False,
    )

    # Error sink (errors and above only)
    logger.add(
        str(error_path),
        level="ERROR",
        enqueue=True,
        backtrace=True,
        diagnose=True,
    )
