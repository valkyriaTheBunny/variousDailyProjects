import random

def toss_biased(bias: str) -> int:
    if bias != 'tails' and bias != 'heads':
        raise ValueError("Entered value should be 'heads' or 'tails'")
    if bias == 'tails':
        result = random.random()
        return 0 if result <= 0.6 else 1
    else:
        result = random.random()
        return 1 if result <= 0.6 else 0


def main() -> None:
    print(toss_biased('tails'))

if __name__ == '__main__':
    main()