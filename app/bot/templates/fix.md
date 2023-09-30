{% extends "base.html" %}

{% block page %}

{% filter markdown %}

# What To Do About Herring

As lovely as it would be to suddenly have access to loads of new instrumentation and data the fact of the matter is that we have to make due with the data we have. At the end of the day decisions have to be made *now*. 

So, what do we do?

Well let's go back to basics - what, ultimately, do we need? We need an estimate of the net natural change in stock that we can expect each year. Why this? Because this net change represents the overall pool from which we can take - if we go over this net change (which we're assuming is positive) then the stock gets smaller and smaller year after year. If we go too far below it we risk people's livelihoods. So we don't want to know how *many* fish are in the sea directly - we want to know how much that number is given to change. 

So how do we get this? Well what do we have? From the assessment reports we know that we have catch data, effort data, some indices of abundance, some fishery independent trawl data, and some limited weight, age, and old larval survey data. So how are we going to back out natural change if we don't have recruitment or predation data? Well, very broadly speaking, the number of fish one year to the next is given by:

$$S_{y+1} = S_{y} - F_{y} - M_{y} + R_{y}$$

Which means we've got 4 different components - $S$ stock size, $F$ fishing mortality, $M$ natural mortality, and $R$ recruitment. If we let $N=R-M$ then we really have three things to estimate which means that if we can estimate two of them we can get the last one. 

What's excellent is we definitely have $F$ and thanks to the trawl surveys and the fact that catches technically are a form of sampling we have the beginning of a sense for $S$ as well. However there is a problem - we don't really know what's going on where these samples aren't being taken and there's a danger that fishermen are simply following the fish (and thereby giving us a sense that there are more fish than there really are).

Thankfully we still have the trawl data and not all fishermen are 100% efficient at finding fish. Therefore we are getting biased sampling, but not completely biased to the point of useless. What we need to do though is be able to connect these "samples" to other more objective features we can then use to map out what we think the stock really looks like.

And this is where we can pull in another kind of data - oceanographic and climate data. Herring are forage fish which means they are really close to the bottom of the food chain. And the bottom of the food chain that they do feed on is largely dictated by temperatures, currents, and sunlight. So we should be able to build population distribution models (and possibly even migration models) based off of our biased sampling and oceanographic data. 

Alright once we've got a way to estimate $S$ each year and we've got records of $F$ each year we can get a sense of $N$ each year as well. At this point we then need to relate $N$ back to features we can predict with today (because remember that's the whole point of this escapade). So at this point we leave out a whole bunch of years to act as validation and start looking for what kind of model can predict $N$. 

Then once we've got a prediction of $N$ (and some bounds on that estimate) we can then provide an estimate of how much can be taken given how quickly we want the stock to rebuild. 

However our job is not done. We've now got hypotheses as well as things we just simply could not predict - we should setup the fishing and science of the following years to progressively test and refine these hypotheses and provide the instrumentation data we need so that we can get robust models for herring in the long run. 
  
{% endfilter %}

{% endblock %}