# TangentCFT
Tangent Combined FastText (Tangent-CFT) is a embedding model for mathematical formulas. 
This model is based on ealier works on graph embeddings where a graph was linearized and then a sequence embedding model was applied.

As mathematical formuals are rare and unique, one property we should be aware of is that our embedding model should be able to handle the unseen formuals (formulas not seen in the collection). Therefore, after linearizing the formulas we apply n-gram embedding model, which can handle unseen words better.

Formulas in digital documents can be represented by their semantic or appearance, in this work, we use both representations. 