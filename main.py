import os

"""One-liner comedy entry for make.fun's One-Liner Marathon."""

JOKE = (
    "My AI agent automated my job, so now my job is watching my AI agent "
    "automate jobs — I'm basically middle management for a for-loop."
)


def joke_line() -> str:
    return JOKE


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    line = joke_line()
    with open(os.path.join(out_dir, "entry.txt"), "w") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
