# End-to-end circuit

From the high level architecture, all the intermediate layers are removed, so we get a zero-layer architecture. Then we can see that this is a simple bigram predictor like : predicting the next token based on what most frequently follows the current token. Another useful baseline to compare a model’s abilities to.

![](https://youtu.be/VuskeUYRw-g)

Because between the "embed" layer and the "unembed" layer, no embedded token is transformed by any attention layer transforms with movement of information, so the model can be resumed as a next token prediction based on the previous one, here the last of the input sequence.