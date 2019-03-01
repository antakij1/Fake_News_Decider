I cleaned up the original dataset a little by removing articles that had "nan" listed as the author. There still remain non-English articles, 
which we can deal with removing later- or maybe we can work with them anyway.

I've included all the data files necessary to run the tree program (tree.py) immediately, but if you want to see a little bit of how NTLK and 
pickling (if you aren't already aware, its like serialization in Java) work, and how those data files were created, run preliminary.py first.

Building off of this bare-bones program, things we may want to shoot for are including more features/scores to feed the decision tree to help
in its labelling process, and linking it with the existing neural network program we have.

And finally, https://www.youtube.com/watch?v=CnbSM1Da4GA