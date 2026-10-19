"""PolarLabs batch CLI extension for upstream CUID2 (MIT)."""
import argparse
from cuid2 import Cuid

def generate_batch(count: int = 1, length: int = 24) -> list[str]:
    """Create a bounded batch of collision-resistant IDs with CUID2."""
    if not isinstance(count, int) or isinstance(count, bool) or not 1 <= count <= 10000:
        raise ValueError("count must be between 1 and 10000")
    if not isinstance(length, int) or isinstance(length, bool) or not 2 <= length <= 98:
        raise ValueError("length must be between 2 and 98")
    generator = Cuid(length=length)
    return [generator.generate() for _ in range(count)]

def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="PolarLabs CUID2 batch ID generator")
    parser.add_argument("--count", "-n", type=int, default=1)
    parser.add_argument("--length", "-l", type=int, default=24)
    args = parser.parse_args(argv)
    try:
        values = generate_batch(args.count, args.length)
    except ValueError as exc:
        parser.error(str(exc))
    for value in values:
        print(value)

if __name__ == "__main__":
    main()
