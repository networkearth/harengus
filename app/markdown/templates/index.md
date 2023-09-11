{% extends "base.html" %}

{% block page %}

{% filter markdown %}

# `herangus`

## What is `herangus`?

Knowledge typically ends up being rather scattered. There are text books that aim to give a comprehensive view but quickly go obsolete. There are papers spread through loads of different journals. There are articles in magazines, pages on websites, technical notes and public comment from government meetings. You get the idea, knowledge scattered all over the place.

So wouldn't it be nice if instead there was just one living document that brought it all together and constantly stayed up to date? Where when someone realized a chapter was missing "poof" it would just appear in everyone's hands? A document who's structure could adapt to the times? 

In other words, what if knowledge could both be centralized and open source? 

They say to start small, so let's give it a go for Atlantic Herring (*Clupea harengus*). This is [`herangus`](https://github.com/networkearth/harengus).

### The [Ontology]({{environment}}/ontology)

All knowledge starts with getting your [ontology](https://en.wikipedia.org/wiki/Ontology) right. Think of this as defining the lexicon we have to use. Ontology is the scaffolding upon which quantitative modeling is laid. 

### The [Modeling]({{environment}}/modeling)

Modeling is how we take our ontology and make it quantitive and precise. It's also how we then go ahead and optimize our actions with respect to the world.

### Getting [Meta]({{environment}}/meta)

Check this out if you're interested in understanding how we go about developing this knowledge base, the ontology, and our modeling. 

{% endfilter %}

{% endblock %}