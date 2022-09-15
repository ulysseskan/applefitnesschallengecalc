<!-- ABOUT THE PROJECT -->
## About

Each month, Apple Fitness creates a new goal for you.  Depending on the goal,
it may also try and calculate the effort you need to put in each day to
attain that goal.

Problem: Apple calculates this effort assuming you don't have a day
of rest - for example, Sunday.

For example, in the screenshot below, Apple suggests exercising for at least 45 minutes
per day - including Sundays.

[apple_default_fitness_challenge_calc.jpg]

This quick and dirty python script recalculates your daily effort amount
to exclude Sundays:

[applefitnesschallengecalc_screenshot.png]

You'll note it does ask for the expected amount of natural exertion you would
put in each Sunday / day of rest.  You can figure this out by looking at a few
of your past rest days.

<!-- GETTING STARTED -->
## Getting Started

1. ```git clone https://github.com/ulysseskan/applefitnesschallengecalc.git```
2. ```cd applefitnesschallengecalc```
3. ```python3 applefitnesschallengecalc.py```

### Prerequisites

You need a copy of Python 3.  I only tested this with Python 3.10.

1. Install [Brew](https://brew.sh).
2. ```brew install python3```
3. Ensure Brew's executable bin directory is in your PATH variable, for example:<br>
```echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile```

<!-- IMPROVEMENTS -->
## Improvements that could be made

- [ ] input validation
- [ ] detection of whether the user is using minutes or calories
- [ ] add a check to see if the user has already met their goal
- [ ] define functions (not sure this is really needed for such a small script)
- [ ] add unit tests
- [ ] if Apple ever adds HealthKit APIs to macOS, this script could be rewritten to use it, ref: https://developer.apple.com/forums/thread/94937


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact

Project Link: [https://github.com/ulysseskan/applefitnesschallengecalc](https://github.com/ulysseskan/applefitnesschallengecalc)




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* David Bau for the idea on how to round up a integer without resorting to importing another module: https://stackoverflow.com/a/35125872
