08/02-03-04-05-06-07/2015

* Objective

    * Use Volpiano to correct the OMR data; Auto/semi-automatically/semi-manually

* To-Do

    * Speak with Jerome/Blanchette for a good algorithm

    * Study Statistics of local pairwise sequences (BLAST Results)

    * Check out Algorithms on strings, trees and sequences: Computer Science and Computational Biology + Handbook of Exact String Matching Algorithms

        * [http://www.torrentmob.com/ebooks/41282-algorithms-on-strings-trees-and-sequences-computer-science-and-computational-biology-by-dan-gusfield.html](http://www.torrentmob.com/ebooks/41282-algorithms-on-strings-trees-and-sequences-computer-science-and-computational-biology-by-dan-gusfield.html)

    * Check out **BioPython pairwise2,** nwalign, swalign, **scikit-bio**,** alignment** or other modules

        * (Checkout Rosetta Code for Javascript) if not -> implement it in javascript

        * Seems like python has Biopython has EMBOSS package

    * Write a script that automatically loads String set to compare on web and obtains results

        * [http://www.quora.com/Is-it-possible-to-write-a-Python-script-for-opening-a-browser-and-logging-into-a-website-How-could-you-do-it](http://www.quora.com/Is-it-possible-to-write-a-Python-script-for-opening-a-browser-and-logging-into-a-website-How-could-you-do-it)

    * Study local vs global alignment algorithm and determine which one fits best for my purposes + Matrix music pitch comparison

    * write unit tests for modules

* Issues Encountered

    * Problem Areas to Consider (Extraction, Conversion, Comparison, Display)

        * Extraction of pitches from respective file formats

            * Volpiano is divided in chants but sometimes do contain incomplete chants at the bottom (Observed a single case like that)

            * MEI contains notes regardless of incomplete chants

        * Fair comparison and formatting pitches 

            * MEI’s clef incorporates clef changes -> pitch changes

            * Volpiano disregards clef elements other than Chant’s starting clef

                * Maybe compare based on integers representing relative notes with respect to keys ( might need octave attribute )

                * Add mei method that would extract sequence of melodies divided according to their clefs

                    * Check out change in intervals ? Roman numerals ?

        * Alignment Algorithm

            * Global vs Local Alignment ? Or are there any better solution

        * Display possible correction on an Interface -

* Tasks Accomplished

    * Query CSV File using Python csv module to get all volpiano chants on one page

    * Extract all pitches in one page using ElementTree Parser in Python

    * Sent Email to request consultation with Jerome (BioInformatics Professor)

    * Added feature to extract last change of previous page and first chant of next page

    * Scripts & Tools that outputs sequence of notes to compare has been completed

    * Get the missing mei_files: salz_153r and salz_173r are missing

    * Check why some volpiano strings have less notes than the CF counter-part.

    * Investigated whether it would be necessary to start an interval based comparison for note module.

* Tests & Results

    * Biopython alignment matrix does not have score between certain keys ex. (g, d) 

    * matrix alignment does not require strings to be capitalized

    * When there is simply no match at all, it does not print or return anything ex (a, b)

    * not all matrix can support every key pair combination

* Misc![image alt text](image_0.png)

08/10-11-12-13-14/2015

* Objective

    * Use Volpiano to correct the OMR data; Auto/semi-automatically/semi-manually

* To-Do

    * Check out **BioPython Emboss**

        * Try writing out my own matrix file and see if it works

        * Check out see alternate output is possible so that I can redirect, manipulate or parse the output string somehow. String IO, Seq IO, AlignIO

        * Write proper script that output stuff to results directory

        * easier way of inputting the fasta files: asis

            * [http://emboss.sourceforge.net/docs/themes/SequenceFormats.html#why](http://emboss.sourceforge.net/docs/themes/SequenceFormats.html#why)

    * Make Biopython pairwise a separate module

    * Study local vs global alignment algorithm and determine which one fits best for my purposes

    * Try different parameters for gap extent and gap open, or just match mismatch to obtain the kind of alignments that I want based on (handmade alignments) test data test and applying that secondary data test.

    * Construct the Substitution Matrix for music pitch comparison

    * Write unit tests for modules

        * Google Technical Developement Guide

        * Nose (Python Learn the Hard Way) - Project Tree Chapter

        * Pyunit

    * Construct a proper project tree structure for Orga

        * [http://learnpythonthehardway.org/book/ex46.html](http://learnpythonthehardway.org/book/ex46.html)

        * [http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application](http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application)

        * Settings.py, setup.py, config.py, requirements.txt ...etc

    * Using D3 or interactive data visualization tutorials, create an interface or at least a static web page that displays the pitches to be corrected.

    * Read Introduction to Computational Biology: an evolutionary approach. 

* Tasks Accomplished

    * Fix bugs in compare.py

    * for volpiano module, return an object containing the names of the previous and next chants of the queried image file

    * Decided to not use nwalign, swalign or aligment (premature and undocumented products with ok..API

    * Rosetta Code did not have Javascript implementation of sequence alignment algorithm…

    * try optimized algorithm for scikit-bio (local alignment) to see if the format is better

    * Studied Pairwise2 package, scikit-bio package

    * Speak with Jerome/Blanchette for a good algorithm

    * Make Biopython pairwise a separate module

    * Check out BioPython Emboss

* Tests & Results

    * Scikit-bio

        * Requires strings to be in uppercase for default sub matrix (protein ver.)

        * for nucleotide specific local alignments, upper case does not work for certain invalid character combination (R, F and D for example)

        * Hard coded substitution matrix can be feasible

        * length of local align is the shortest subsequence aligned

        * length of global align is the longest sequence queried initally

        * optimized smith-waterman algorithm does not print/return a complete alignment between two sequences, therefore making it unusable.

        * Matrix format is a pair of keys mapped to a score

    * Emboss

        * Sequence analysis is definitely much more detailed and it provides much greater information than any of the modules I’ve used so far.

        * Matrix files are located in /usr/local/Cellar/emboss/6.6.0/shared/Emboss/data

        * Emboss matrix recognizes lower_case characters

        * It’s also possible to write your own matrix file by following the format of other matrices. However, if insufficient character combinations or provided, for the characters that are not part of the matrix, the resulting output of the alignment will be strange.

        * to print result on screen: set outfile to ‘stdout’ and run the command line returning to arguments ex. stdout, stderr = water_cline(). Finally, make sure to print stdout + stderr

        * needle/water can also compare is case agnostic (doesn’t care if the strings are in upper case or lower case)

        * easier way of inputting the fasta files: asis

            * [http://emboss.sourceforge.net/docs/themes/SequenceFormats.html#why](http://emboss.sourceforge.net/docs/themes/SequenceFormats.html#why)

* Misc

    * Meeting Notes w/ Professor Jerome

    * Questions 

        * Is the algorithm good enough for my purposes, are there other algorithms that I have not considered ?

        * Local vs Global; how much are the default constraints imposed by the selection of either local or global alignment algorithm influences output or the kind of alignments I get ? gap extend, gap open, Matrix type

        * What is the role of the substitution matrix in most popular alignment programs, and how should I construct one based on musical pitches represented by seven characters. That may or may not represent the exact matching absolute pitches or relative pitches but similar diatonic/melodic sequence 1-2-1-5-3 etc

        * Combining intervalic analysis with absolute pitch detection analysis and alignment to further filter wrong notes vs good notes.

    * Answer

        * Dahoff Matrices 

        * PAM matrices for trusted alignments 

        * Bernhard Haubold and Thomas Wiehe*. Introduction to Computational Biology: An Evolutionary Approach* , Burkhauser Basel, 2007

        * Have two set data and try different parameters to obtain the alignment I’m looking for

        * Go simple first; use +1 or -1 (Something like that)

        * [http://www.cs.mcgill.ca/~jeromew/comp561/](http://www.cs.mcgill.ca/~jeromew/comp561/)

        * Bernhard Haubold and Thomas Wiehe*. Introduction to Computational Biology: An Evolutionary Approach* , Burkhauser Basel, 2007

        * [http://link.springer.com/book/10.1007%2F3-7643-7387-3](http://link.springer.com/book/10.1007%2F3-7643-7387-3)

08/17-20-22-23/2015

* Objective

    * Use Volpiano to correct the OMR data; Auto/semi-automatically/semi-manually

* To-Do

    * Study local vs global alignment algorithm and determine which one fits best for my purposes

        * Difference between [ : ], [ | ], [ . ] symbols for alignment outfile

        * Try different parameters for gap extent and gap open, or just match mismatch to obtain the kind of alignments that I want based on (handmade alignments) test data test and applying that secondary data test.

    * Implement Local | Global Alignment Algorithm in Python/javascript 

    * Construct the Substitution Matrix for music pitch comparison

    * Write unit tests for modules

        * Google Technical Developement Guide

        * Nose (Python Learn the Hard Way) - Project Tree Chapter

        * Pyunit

    * Construct a proper project tree structure for Orga

        * [http://learnpythonthehardway.org/book/ex46.html](http://learnpythonthehardway.org/book/ex46.html)

        * [http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application](http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application)

        * Settings.py, setup.py, config.py, requirements.txt ...etc

    * **Using D3 or interactive data visualization tutorials, create an interface or at least a static web page that displays the pitches to be corrected.**

    * Read Introduction to Computational Biology: an evolutionary approach. 

    * Add license boilerplate for each of my file

* Tasks Accomplished

    * Completed script that outputs results

* Tests & Results

    * Local Alignment has higher % for similarity, identity and lower % in gaps.

    * Local Alignment output strings are stripped out of region that have large gaps, and does not show all the notes the original sequence is supposed to contain

    * Metrics are disucssed here [http://emboss.sourceforge.net/docs/themes/AlignFormats.html#sim](http://emboss.sourceforge.net/docs/themes/AlignFormats.html#sim)

    * When you want an alignment that covers the whole length of both sequences, use [needle. ](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/needle.html)

    * When you are trying to find the best region of similarity between two sequences, use [water.](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/water.html)

* Misc

