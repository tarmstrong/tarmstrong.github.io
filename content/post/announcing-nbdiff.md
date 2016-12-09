+++
title = "NBDiff: A diffing and merging tool for the IPython Notebook"
date = "2014-04-06T15:18:00"
tags = [ "school", "coding" ]
+++

Final-year engineering students at many universities have to complete a "Capstone" project that gives them a chance to apply everything they learned throughout school to a practical, hands-on group project. My team just finished ours -- a project called [NBDiff][nbdiff] -- and I'm happy to report that it was a success.

If you've spoken to me in the last couple years, you've probably heard me ramble about the IPython Notebook, a rich web-based environment for scientific computing. Well, that project is wonderful, but there's a catch with working on notebook files: the file format is a giant JSON blob and makes version control tricky. If you use `git diff`, it can be hard to understand what you've actually changed, and if you need to resolve a merge conflict? Fasten your seatbelt.

NBDiff takes a stab at making these tasks easier. It presents diffs in a two-pane format and shows you deleted/added cells how you originally saw them in the notebook: if an image was changed, you see the image instead of a 10000-line diff of a base64 encoded PNG file. When resolving merge conflicts, you don't have to worry about mangling the JSON by hand -- you just drag and drop changes into the final version and click 'save'.

![A screenshot of nbdiff](/nbdiff-screenshots/main-screenshot.png)

As far as school projects go, this one was very satisfying. We have 50 GitHub stars and several hundred downloads already; I can actually use it to solve problems *right now*; and the IPython folks are interested in seeing it maintained beyond Capstone. Considering many school projects -- even Capstone projects -- never see the light of day, let alone continued maintenance, I'm really happy about this.

* Homepage: [nbdiff.org][nbdiff]
* GitHub repo: [tarmstrong/nbdiff][github]
* PyPI package: [nbdiff][pypi]

![50 github stars and counting](/nbdiff-screenshots/stars.png)


[nbdiff]: http://nbdiff.org
[github]: https://github.com/tarmstrong/nbdiff
[pypi]: https://pypi.python.org/pypi/nbdiff
