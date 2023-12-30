# 2024-solar-eclipse

This repo has tools to generate a list of airports that are in the path of
totality for the 2024 Solar Eclipse. The list it generates is in CSV and
includes the airport name, coordinates, and the duration of totality.

## Requirements

Download [this data file](https://datahub.io/core/airport-codes) as CSV into
this directory. It will be named `airport-codes.csv`.

```
$ wget -q https://datahub.io/core/airport-codes/r/airport-codes.csv
```

## How to use

`airports.txt` is a list of airports that were selected manually by overlaying
the path of totality onto VFR sectional charts. Other airports are in the path
of totality, but these are the ones I found most compelling as options I want
to consider visiting for the eclipse. You can adjust the list as you see fit.

Run the `generatecsv.py` script.

```
$ ./generatecsv.py
```

That command will generate CSV that can be imported into your favorite
spreadsheet software.
