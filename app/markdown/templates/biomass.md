{% extends "base.html" %}

{% block page %}

{% filter markdown %}

# One Fish, Two Fish

So how do we get this graph?

<img style="max-width: 25%; height: auto;" src="{{environment}}/static/biomass.png" />

From the [assessment](https://apps-st.fisheries.noaa.gov/sis/docServlet?fileAction=download&fileId=8051) we know that:

> This assessment of the Atlantic Herring (Clupea harengus) stock is a management track assessment of the existing
> 2020 management track assessment conducted using the ASAP model.

So what is this ASAP model? Well let's go back to the [source](https://sedarweb.org/documents/s12rd06-a-flexible-forward-age-structured-assessment-program/)!

## ASAP (Age Structured Assessment Program)

### The Central Equation

We start with an equation that should be relatively familiar:

$$N_{a,y}=N_{a-1,y-1}e^{-Z_{a-1,y-1}}$$

This is the classic instantenous mortality equation that shows up in a lot of forward projection models. Let's talk through the notation. First $a$ is the age class (1, 2, 3, etc.), $y$ is the year (1996, 1997, 1998, etc.), $Z$ is the combination of fishing $F$ and natural $M$ mortality and $N$ is a number of fish. So $N_{a,y}$ is the number of fish in age class $a$ in year $y$. And $Z_{a-1,y-1}$ is the mortality of age class $a-1$ year $y-1$. 

So the above equation is just saying how a specific cohort shrinks in number from age $a-1$ in year $y-1$ to age $a$ in year $y$. Simple as that.

#### An Addendum

Now typically folks won't actually calculate *all* fo the ages. Rather once fish get to some "largest" age class they're treated as one big pool with all the older fish. This "largest" age class is designated by $A$ and so the equivalent equation has to include how the fish already in the age class are dying off which gives us:

$$N_{A,y} = N_{A-1, y-1}e^{-Z_{A-1, y-1}}+N_{A,y-1}e^{-Z_{A,y-1}}$$

Now obviously given the purpose of this model is to allow us to predict biomass the $N_{a,y}$ are going to come out of this process. However the natural question arises - how are we going to get the $Z_{a,y}$?

### Mortality

Mortality, as with most fisheries models, decomposes into two components:

$$Z_{a,y}=F_{a,y}+M_{a,y}$$

which as we mentioned are the fishing $F$ and natural $M$ mortality respectively. Now $M$ doesn't get broken down anymore than this, but $F$ does. Specifically we know that there are different fleets with different levels of selectivity. So for each gear type $g$ we have specific mortality for this age group in this year - $F_{a,y,g}$. 

$$F_{a,y}=\sum_g F_{a,y,g}$$

#### Selectivity

So where do we get these $F_{a,y,g}$ from? Well first we start with the notion of selectivity - $S_{a,y,g}$. In ASAP the selectivities that are nonzero (i.e. the gear $g$ catches those age groups) are set to average to one and are required to be positive. This doesn't have much of a real interpretation, but rather just seems to be a way to keep the optimization process itself from wilding out of control. To tie these all back together when computing $F_{a,y,g}$ we have another parameter $\mathcal{F}_{y,g}$ which is called the fishing mortality multiplier because we multiply it by the selectivity $S_{a,y,g}$ to get $F_{a,y,g}$:

$$F_{a,y,g}=S_{a,y,g}\mathcal{F}_{y,g}$$

This just leaves us in a position where we have an interpretable selectivity value later once this model has been fit. Because the $S_{a,y,g}$ don't have to sum to one $\mathcal{F}_{y,g}$ shouldn't be taken as the overall mortality for that year and gear class.

Now the model actually puts some constraints on these $S$. Specifically it either considers the $S$ to be constant over $y$ or that the change in selectivity is constrained to be a random walk. Specifically that:

$$S_{a,y+\tau,g}=S_{a,y,g}e^{N(0,s_{g}^2)}$$

where N(0,s_{g}^2) is a draw from the normal distribution centered at 0 with variance $s_{g}^2$. So if we do want to allow variability in selectivity, this adds some additional parameters. 

### Recruitment

Okay so far so good. However we have a bit of a problem. We can calculate $N_{a,y}$ given the previous year $N_{a-1,y-1}$ but what happens when there is no previous year, i.e. $a=1$? In other words, how are we dealing with recruitment? Well the assumption that this model makes is that recruitment is just always some deviation from an average value of some kind.

$$N_{1,y}=\bar{N_1}e^{N(0, s^2_{N_y})}$$

Where $N(0, s^2_{N_y})$ is a draw from a normal distribution with mean 0 and variance $s^2_{N_y}$. Note we've just introduced two parameters $N_1$ which is just a constant and $s^2_{N_y}$ which is also just a constant (the subscript here just indicates it's used over years not that it's varying by year). 

### Initialization

Now the last equation tells us how to start a totally new cohort but what about cohorts that already exist at the beginning of our time series? For example what if a fish is 4 years old at the beginning of our analysis $a_{4,1}$? Well for ASAP we start by making the assumption that things have been in a steady state before our analysis and therefore the $N_{1,1}$ represents where each age class started and $Z_{a,1}$ i.e. the mortality at year 1 is the same mortality for all prior years. This would give us:

$$N_{a,1}=N_{1,1}e^{-\sum_{i=1}^{a-1} Z_{i,1}} \space for \space a < A$$

$$N_{A,1}=\frac{N_{1,1}e^{-\sum_{i=1}^{A-1} Z_{i,1}}}{1-e^{-Z_{A,1}}} \space for \space a = A$$

However this a pretty wild assumption so we allow some deviation from this the same way we did for recruitment:

$$N_{a,1}=N_{1,1}e^{-\sum_{i=1}^{a-1} Z_{i,1}}e^{N(0,s^2_{N_a})} \space for \space a < A$$

$$N_{A,1}=\frac{N_{1,1}e^{-\sum_{i=1}^{A-1} Z_{i,1}}}{1-e^{-Z_{A,1}}}e^{N(0,s^2_{N_A})} \space for \space a = A$$

### The Outcomes

Alright so what does the paper say you get from all of this? Well you get at a minimum:

- $N_{a,1}$ (initial populations)
- $N_{1,y}$ (recruits)
- $N_{a,y}$ (population abundances)
- $\mathcal{F}_{y,g}$ (fish mortality multipliers)
- $S_{a,y,g}$ (selectivity)

So where is $M_{a,y,g}$? Well that's just an input to the model. And what data are we using to fit all of this? Well using catch statistics of course! Specifically we can compute catch as:

$$C_{a,y,g}=\frac{N_{a,y}F_{a,y,g}(1-e^{-Z_{a,y}})}{Z_{a,y}}$$

Which is just the proportion of fish that died due to fishing mortality of that gear type rather than having died to natural mortality. However fish are rarely counted. Instead they are weighed. So we need a relationship between age and weight. And to do that we use another input to the model $W_{a,y}$ which is the weight of a fish in age class $a$ in year $y$. 

We can also calculate indices of abundance $I_{u,y}$ which take a catchability coefficient $q_{u,y}$ (which is estimated, not given) and relate our other estimated parameters with:

$$I_{u,y}=q_{u,y}\sum_{a(u_{start})}^{a(u_{end})}S_{u,a,y}N^*_{a,y}$$

The $*$ above $N$ just indicates it may be weight or count. From here an objective is setup to more or less calculate the likelihood of estimates given some assumptions about how all of these are distributed. 

But let's stop here for a moment and consider what we've got so far. We're passing in the following:

- $I_{u,y}$ (indices of abundance)
- $C_{a,y,g}$ (catches)
- $W_{a,y}$ (weights)
- $M_{a,y,g}$ (mortality)

and getting everything else... 

What should immediately jump out to you is that at no point are we actually measuring how many fish are in the ocean whatsoever. We are 100% predicting that number and the fishing mortality and the recruitment based off of this one model. Now this is fine if our inputs are good and our assumptions are as well. So let's walk back through those and consider if these things makes sense.

# Questions

- Ages are really what selectivity is based on
- Age is usually determined from growth
- Interesting to have just one mean and not to link it to stock size at all
- Steady state is an interesting assumption...
- Assumed $M$ seems a bit odd
- Weights are going to get wild...
  
{% endfilter %}

{% endblock %}