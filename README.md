# Craiglist Scraper
This scraper is set to continously scrape craigslist for your provided filter word *ie. banjo* and text you any time there is a new post.

## Syntax
```
python3 main.py https://sfbay.craigslist.org/d/musical-instruments/search/msa banjo
```

## Problems
* Does not filter through previous sent text, yet. I have not implemented the loop because it will send same listings.
* Would like to change the url grab to typical search, however needs to have a cap. Do not want to send 1,200 text for the search result of guitar.