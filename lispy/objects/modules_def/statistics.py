import statistics
from lispy.error import lispy_function

@lispy_function("stats:mean", ["list"])
def statistics_mean(args):
    return statistics.mean(args[0])

@lispy_function("stats:median", ["list"])
def statistics_median(args):
    return statistics.median(args[0])

@lispy_function("stats:mode", ["list"])
def statistics_mode(args):
    return statistics.mode(args[0])

@lispy_function("stats:variance", ["list"])
def statistics_variance(args):
    return statistics.variance(args[0])