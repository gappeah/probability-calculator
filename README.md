I created a Hat class in prob_calculator.py that takes a variable number of arguments that specify the number of balls of each colour that are in the hat. I also created a draw method that accepts an argument indicating the number of balls to draw from the hat. This method removes balls at random from contents and returns those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

I also created an experiment function in prob_calculator.py that accepts the following arguments:

* hat: A hat object containing balls that should be copied inside the function.
* expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment.
* num_balls_drawn: The number of balls to draw out of the hat in each experiment.
* num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The experiment function returns a probability.

For example, if I wanted to determine the probability of getting at least two red balls and one green ball when I draw five balls from a hat containing six black, four red, and three green. To do this, I would perform N experiments, count how many times M I get at least two red balls and one green ball, and estimate the probability as M/N. Each experiment consisted of starting with a hat containing the specified balls, drawing several balls, and checking if I got the balls I was attempting to draw.

Here is what I would call the experiment function based on the example above with 2000 experiments:

```python
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Since this is based on random draws, the probability will be slightly different each time the code is run.

I wrote my code in prob_calculator.py. For development, I used main.py to test my code. Click the "run" button and main.py will run.

The unit tests for this project are in test_module.py. We imported the tests from test_module.py to main.py for convenience. The tests would run automatically whenever I hit the "run" button.
