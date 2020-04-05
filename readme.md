# Reverse Collatz (ReColl)

This has been an attempt to efficiently calculate all the values in a collatz sequence. In order to achieve this, it is being done in reverse. This allows you to safely assume that the odd value that results in the current value has been computed already, and you can also safely assume that the value that one will resolve into if the current value is even has been computed. For instance, when the value is `10`, since the iteration starts at 1 and increments the value upwards we know that both `3` and `5` have already been evaluated and due to the linear evaluation order we can safely compute their indices. The reason why we are interested in `3` and `5` is because `3*3+1=10` and `10/2=5`.