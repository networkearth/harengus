{% extends "base.html" %}

{% block page %}

{% filter markdown %}

# The Concern

The following graph from a recent [assessment](https://apps-st.fisheries.noaa.gov/sis/docServlet?fileAction=download&fileId=8051) shows a troubling trend in herring stocks today:

<img style="max-width: 50%; height: auto;" src="{{environment}}/static/biomass.png" />

Over the past few years we've predicted exceedingly small numbers of herring. What's this the result of? Let's start by looking at the exploitation of the resource:

<img style="max-width: 50%; height: auto;" src="{{environment}}/static/catch.png" />

What's very interesting in comparing these two graphs is that the level of fishing has not only remained relatively level over the past several decades (since ~1995) but during the period from ~1990 to ~2005 the stock wavered but stayed far above Stock Biomass at MSY. It them dips a bit in the 2010's and then rapidly collapses to the levels seen today (which are the worst ever according to this analysis). Once can also clearly see that year after year fishermen were catching <50% of the overall estimated spawning biomass. Now while this certainly doesn't give the fish much of a chance to rebuild it is also not necessarily an irresponsible amount to take. Yet it seems that in the past few years the age classes have absolutely and decided dropped. 

This points to one of two things - recruitment failed for the resource or we've been wrong on one of these measurements all along. In other words either the stock just hasn't been recruiting or either our stock assessment or catch numbers are terribly wrong. 

To look at recruitment we need to get age based data from somewhere and see how many year one fish are joining the population each year. 


## Notes

- [Commercial Fishing Landings Database](https://foss.nmfs.noaa.gov/apexfoss/f?p=215:200:14533496384056::NO:::)
- [Most Recent Report](https://www.asmfc.org/uploads/file/63cecac3AtlHerring_65thSAW_AssessmentSummaryReport_Aug2018.pdf)
- [Maybe something?](https://www.ices.dk/about-ICES/projects/EU-RFP/EU%20Repository/ICES%20FIshMap/ICES%20FishMap%20species%20factsheet-herring.pdf)
- [Maybe the data?](https://data.noaa.gov/dataset/?q=atlantic+herring&sort=score+desc%2C+metadata_modified+desc)
{% endfilter %}

{% endblock %}