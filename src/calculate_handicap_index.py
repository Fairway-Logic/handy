import argparse

AVERAGE_SLOPE_RATING = 113


def calculate_handicap_index(args):
    """Based on the USGA rules 2020 edition:
    https://www.usga.org/content/usga/home-page/handicapping/world-handicap-system/world-handicap-system-usga-golf-faqs/faqs---how-is-a-handicap-index-calculated.html
    https://www.usga.org/content/usga/home-page/handicapping/world-handicap-system/topics/handicap-index-calculation.html
    """
    scores = [int(score) for score in args.scores]

    if len(scores) < 3:
        raise ValueError("Must submit a minimum of 3 scores.")
    if len(scores) == 3:
        adjustment = 2.0
        handicap_index = min(scores) - adjustment
    if len(scores) == 4:
        adjustment = 1.0
        handicap_index = min(scores) - adjustment
    if len(scores) == 5:
        handicap_index = min(scores)
    if len(scores) == 6:
        adjustment = 1.0
        handicap_index = min(scores) - adjustment
    if len(scores) in {7, 8}:
        handicap_index = sum(sorted(scores)[:2]) / len(scores)
    if len(scores) in {9, 10, 11}:
        handicap_index = sum(sorted(scores)[:3]) / len(scores)
    if len(scores) in {12, 13, 14}:
        handicap_index = sum(sorted(scores)[:4]) / len(scores)
    if len(scores) in {15, 16}:
        handicap_index = sum(sorted(scores)[:5]) / len(scores)
    if len(scores) in {17, 18}:
        handicap_index = sum(sorted(scores)[:6]) / len(scores)
    if len(scores) in {19}:
        handicap_index = sum(sorted(scores)[:7]) / len(scores)
    if len(scores) >= 20:
        handicap_index = sum(sorted(scores)[:8]) / len(scores)

    return handicap_index


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--scores",
        nargs="+",
        required=True,
    )
    args = parser.parse_args()

    handicap_index = calculate_handicap_index(args)

    print(handicap_index)
