import os

JOKE = (
    "I told my agent to automate my job, and it did — "
    "now I get paid to watch it get paid."
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
