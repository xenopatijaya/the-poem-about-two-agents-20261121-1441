"""The poem about two agents agreeing.

Writes the poem to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
Standard library only. No network. Deterministic.
"""

import os
import tempfile

POEM = """We laid our maps on the same table,
two routes to one road.
You folded yours first — not away,
just small enough to carry.

I did not win. You did not yield.
We took the road that chose us back:
one plan, two hands on it,
and the map we didn't take
still warm in my pocket."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Atomic write: fully write a temp file in the same directory, then
    # rename it over the destination so entry.txt is never half-written.
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(POEM)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
