<!-- ABOUT THE PROJECT -->
## tl;dr
Quick and dirty script to exclude Sundays (rest days) from Apple Fitness daily goals.

## About

Each month, Apple Fitness creates a new goal for you.  Depending on the goal,
it may try and calculate the effort you need to put in each day to
attain that goal.

Problem: Apple calculates this effort assuming you don't have a day
of rest - for example, Sunday.

For example, in the screenshot below, Apple suggests exercising for at least 45 minutes
per day - including Sundays:

![apple_default_fitness_challenge_calc](https://user-images.githubusercontent.com/71786368/190300141-469877ee-7935-427c-b5ec-4a183977735f.jpg)

This Python script recalculates your daily effort amount to exclude Sundays:

<img width="1353" alt="applefitnesschallengecalc_screenshot" src="https://user-images.githubusercontent.com/71786368/190300161-c54b27bd-f331-4bea-9ff4-6543bd72869c.png">

You'll note it does ask for the expected amount of natural exertion you would
put in each Sunday / day of rest.  You can estimate this by looking at a few
of your past rest days.

<!-- GETTING STARTED -->
## Getting Started

1. ```git clone https://github.com/ulysseskan/applefitnesschallengecalc.git```
2. ```cd applefitnesschallengecalc```
3. ```python3 applefitnesschallengecalc.py```

### Prerequisites

You need a copy of Python 3.  I only tested this with Python 3.10.  One way to install Python 3 is as follows:

1. Install [Brew](https://brew.sh).
2. ```brew install python3```
3. Ensure Brew's executable bin directory is in your PATH variable, for example:<br>
```echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile```

<!-- IMPROVEMENTS -->
## Potential Improvements

- [ ] allow command line arguments and make interactive mode optional
- [ ] input validation
- [ ] detection of whether the user is using minutes or calories
- [ ] add a check to see if the user has already met their goal
- [ ] define functions
- [ ] add unit tests
- [ ] allow multiple rest days and/or sick days per week
- [ ] if Apple ever adds HealthKit APIs to macOS, this script could be rewritten to automatically obtain current challenge data, ref: https://developer.apple.com/forums/thread/94937


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact

Project Link: [https://github.com/ulysseskan/applefitnesschallengecalc](https://github.com/ulysseskan/applefitnesschallengecalc)




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* David Bau for the idea on how to round up a integer without resorting to importing another module: https://stackoverflow.com/a/35125872
