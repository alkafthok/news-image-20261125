from os import environ
from pathlib import Path

POSTER = Path(__file__).resolve().parent / "entry.png"
DEST = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def place_poster() -> None:
    """Copy the bundled poster to the grading directory, unchanged."""
    data = POSTER.read_bytes()
    if len(data) > 1_048_576:
        raise SystemExit("poster is larger than the 1 MiB limit")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(data)
    if DEST.read_bytes() != data:
        raise SystemExit("poster copy differs from the bundled file")


place_poster()
