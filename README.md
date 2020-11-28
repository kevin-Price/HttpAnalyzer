# Analyze Websites
This is an Azure serverless function that will analyze a specified number of website's headers. 

Given a number of websites to analyze, this function will return its running time, the top 10 most frequest headers, and a percentage of how many times those headers occured.

*Note this is limited to local usage due to cloud hosting cost*

## Running locally
To run locally, you will need the following:

- [Python 3.6+](https://www.python.org/)
- [Azure Function Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Ccsharp%2Cbash#v2)

Run ``` source .venv/bin/activate ``` in the program root

Run ``` func start``` in the analyze_websites directory to start the function host 

Finally, issue the request ```GET http://localhost:7071/api/analyze_websites?total_websites=1000 ```

## Optional Query Params
- ### "total_websites" : Will specify how many websites to analyze. Defaults to 1000.
