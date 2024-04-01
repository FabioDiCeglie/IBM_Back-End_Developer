# DYNAMIC CODE ANALYSIS

Copy and paste the following commands in the terminal window to fetch Juice Shop's docker image, and then run the application.

``` 
docker pull bkimminich/juice-shop
docker run --rm -p 3000:3000 bkimminich/juice-shop 
```

# Lunch the Juice Shop UI

# Run OWASP ZAP

``` docker pull owasp/zap2docker-stable ```

``` docker run -t owasp/zap2docker-stable zap-baseline.py -t https://dcfabio96-3000.theiadocker-2-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/ ```

# Interpret the scan results

You can use the numbers next to the vulnerability names to read about the alert on the ZAP Proxy Web site. Using the following URL:


``` https://www.zaproxy.org/docs/alerts/{NUMBER} ```

As a developer, your task would be to look up the vulnerability, look at each URL listed as being vulnerable, and then fix the vulnerabilities in the code one by one.

# Check the results and fix the issues