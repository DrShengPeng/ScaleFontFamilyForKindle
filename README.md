# ScaleFontFamilyForKindle
Scale font size to make kindle reading more comfortable

# Motivation
On recent kindle models with newer firmware, the font size selector has 14 ticks. These correpond to point sizes: 21 24 25 28 <strong>32 34 37</strong> 42 46 51 58 66 75 87. The three consecutive sizes in bold provide the most gradual gradation amongst all the 12 3-tuple choices. So the goal is to maximize the comfortableness of reading at size #6 (34), with fine tuning  avaiable on both sides. Target x-height of 490 seems to be working great. 510 makes size 6 and 7 a little too big for my taste. Play with the target x-height so the end result will match your preference.

# Usage
Say, there is 4 fonts of the same typeface in the same folder, all reasonaly named like myfont-\*.otf. Invoke the command like this:
<pre>
<code>
[CMD] myfont-roman.otf
</code>
</pre>
This will scale the roman font, as well as the related italic and bold variants, using the same factor which is determined by the ratio between the x-height and its target value.
