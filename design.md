# Structure of the code
The project consists of three interacting components: AL itself, a simple "world" of blocks and
other objects that may be moved around, and a GUI visualization.


# AL's language faculty
In generative linguistics the natural language faculty is conventionally divided into two
subsystems: the lexicon that contains all the "memorized" information about individual linguistic
items, such as the conjugations of verbs and inflections of nouns, and the rules that are used to
generate and interpret linguistic expressions. This basic dichotomy informs the structure of AL's
artificial language faculty.

Linguistic analysis is divided into five progressive stages: phonetic, phonological, morphological, syntactic, and semantic. For simplicity it is usually assumed that each stage feeds the next (e.g., the morphological stage takes as its input the product of the phonological analysis).

As AL uses a textual interface, the phonetic and phonological stages are inapplicable. Morphological analysis is the analysis of the structure of words. In AL's limited vocabulary, knowledge of nominal pluralization and verb conjugation is probably sufficient.

Syntax, the hierarchical and linear arrangement of words, is exponentially more complicated than morphology. Sentence structure is commonly modeled with context-free grammars, but Chomsky (1957) shows that context-free and probably even context-sensitive grammars are inadequate for natural language syntax. In theoretical linguistics, syntax is commonly represented with syntax trees (often binary) that encode relationships of hierarchy and constituency.

To my knowledge relatively little work has gone into computational semantics, unsurprisingly given that modern methods of syntactic analysis are still quite rudimentary. A central question is how the semantic meaning of an utterance can be represented as a data structure.

Further, beyond analyzing the utterances of its human conversation partner, AL will need to produce its own utterances, a process akin to analysis in reverse, beginning at the desired semantic interpretation and ending at the phonetic (or in AL's case, textual) output. For now this aspect of AL will probably be limited to assenting to commands (or objecting if they are impossible) and answering questions, which removes the need for any social or pragmatic considerations.

## Analysis

### Morphological

At the morphological stage, character strings will need to be matched with their corresponding entry in AL's lexicon. Verbal conjugations are redundant in English and can be ignored in the analysis stage. Nominal pluralization should be simple to detect and can be represented as a simple boolean switch.

### Syntactic

AL must be capable of understanding at least three simple sentences structure: imperative commands, declarative sentences, and questions.

### Semantic

What data structure can be used for semantic information?

## Production