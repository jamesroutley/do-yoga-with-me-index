# Do yoga with me index

[Do yoga with me] is a website which hosts videos of yoga classes. It's great, but I find its search difficult to use. This repo conatins an index I've built of all videos on the website, with some meta data about duration, difficulty, rating etc.

Here's the [latest index]. The index contains all videos, sorted by publish date. It's not particularly useful on its own - I generally use [xsv] to sort and filter the videos:

- Get the top 5 videos, sorted by number of ratings (a proxy for popularity):

  ```
  $ xsv select 4,5,2,1 results/results-latest.csv | sort -nr | head -n 5 | xsv table
  1155  4.8  Bend and Stretch                                      Melissa Krieger
  954   4.9  Deep Release for the Hips, Hamstrings and Lower Back  David Procyshyn
  935   4.9  Rise and Shine                                        Fiji McAlpine
  830   4.8  Foundations in Flow                                   Fiji McAlpine
  533   4.8  Core Strength and Stretch                             Melissa Krieger
  ```

[Do yoga with me]: https://www.doyogawithme.com/
[latest index]: /results/results-latest.csv
[xsv]: https://github.com/BurntSushi/xsv
