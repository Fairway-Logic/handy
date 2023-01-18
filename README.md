# Handy

A handy set of golf handicap tools.

## Usage

### Calculate Course Handicap

```
  -h, --help            show this help message and exit
  -hi HANDICAP_INDEX, --handicap_index HANDICAP_INDEX
  -sr SLOPE_RATING, --slope_rating SLOPE_RATING
  -cr COURSE_RATING, --course_rating COURSE_RATING
  -cp COURSE_PAR, --course_par COURSE_PAR
```

To generate an 18-hole course handicap for a course like Schneiter's Bluff, you would run the following:

```bash
python3 calculate_course_handicap.py -hi 15 -sr 120 -cr 70.8 -cp 72
```

### Calculate Handicap Index

```
  -h, --help            show this help message and exit
  -s SCORES [SCORES ...], --scores SCORES [SCORES ...]
```

To generate a handicap index, pass in a list of your scores from your most recent (up to 20) 18-hole games:

```bash
python3 calculate_handicap_index.py -s 83 60 62 90 67 56 75 60 23 74 70 77 76 75 74 73 69 90 98 68
```
