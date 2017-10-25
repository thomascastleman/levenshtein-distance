# levenshtein-distance
Find Levenshtein distance between two strings

This approach first finds the optimal mapping of indices of shared characters between the two strings, if any exist<br>
i.e. <code>"cat"</code> and <code>"chant"</code> share the set of characters <code>{'c', 'a', 't'}</code><br><br>
This was accomplished recursively, where the shared character <code>'c'</code> would be found and then the same method run on the remaining substrings <code>"at"</code> and <code>"hant"</code>
<br><br>
This example would yield a mapping of <code>{ 0 : 0, 2 : 1, 4 : 2 }</code>, where the index of <code>'c'</code> in "chant" as well as "cat" is 0. The index of <code>'a'</code> in "chant" is 2, and 1 in "cat", and so on.
<br><br>
From this mapping, buffered versions of each string can be constructed such that the two may be placed next to each other and all of the shared characters will align. Such buffers are constructed by inserting extra space into the string<br>
i.e.
<pre>
c * a * t
c h a n t
</pre>
The alignment of buffers can then be examined and the number of disagreements between characters from either buffer counted to determine edit distance, in this case 2 (<code>'h' != *</code>, <code>'n' != *</code>)
