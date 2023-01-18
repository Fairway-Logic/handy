import argparse

AVERAGE_SLOPE_RATING = 113


def calculate_course_handicap(args):
    """Based on the USGA rules 2020 edition:
    https://www.usga.org/content/usga/home-page/handicapping/roh/Content/rules/6%201%20Course%20Handicap%20Calculation.htm
    """
    return round(
        args.handicap_index * (args.slope_rating / AVERAGE_SLOPE_RATING)
        + (args.course_rating - args.course_par)
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-hi",
        "--handicap_index",
        type=float,
        required=True,
    )
    parser.add_argument(
        "-sr",
        "--slope_rating",
        type=float,
        required=True,
    )
    parser.add_argument(
        "-cr",
        "--course_rating",
        type=float,
        required=True,
    )
    parser.add_argument(
        "-cp",
        "--course_par",
        type=int,
        required=True,
    )
    args = parser.parse_args()

    course_handicap = calculate_course_handicap(args)

    print(course_handicap)
