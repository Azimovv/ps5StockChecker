# ps5StockChecker
selenium script to periodically check multiple sites for stock of the PS5


Make sure to add the appropriate chromedriver version to your PATH otherwise this won't work: https://chromedriver.chromium.org/downloads

Can repurpose this for any stock you want to keep track of.
Just change the url and its corresponding xpath for whatever you want to keep track of,
in this case the 'add to cart' button.


This isn't perfect, but seems to work well for Amazon and Walmart, Target is a bit iffy.
BestBuy and GameStop don't seem to be working, could fix it if you change the element that's searched for
to the id or class associated with the 'add to cart' button
