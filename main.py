import os


def count_open_tabs():
    buckets = {
        "research tabs": 61,
        "reference docs": 34,
        "video pages": 18,
        "shopping pages": 14,
        "everything else": 10,
    }
    tally = 0
    for bucket_count in buckets.values():
        tally += bucket_count
    return tally


def main():
    total = count_open_tabs()
    text = "{}".format(total)
    digits_only = text.isdigit()
    if digits_only is False:
        raise ValueError("tab count is not numeric")
    if not 1 <= len(text) <= 5:
        raise ValueError("tab count length out of range")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, mode="w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
