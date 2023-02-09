# Challenge Summary
<!-- Description of the challenge -->
Write a function called repeated word that finds the first word to occur more than once in a string
Arguments: string
Return: string

## Whiteboard Process
<!-- Embedded whiteboard image -->
![whiteboard](whiteboard.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Time - O(n^2) as I go through the list twice, once to break it up, once for comparison
- Space - O(1) as we don't create anything new, we just alter the given string

## Solution
<!-- Show how to run your code, and examples of it in action -->

just `pytest teat/test_hashable_repeated_word.py`
