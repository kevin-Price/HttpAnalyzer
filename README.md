# Analyze Websites
This is an Azure function that will analyze a specified number of website's headers. 

Given a number of websites to analyze, this function will return its running time, the top 10 most frequest headers, and a percentage of how many times those headers occured.

## How to use
### Azure
Issue a request: ```GET https://httpanalyzer.azurewebsites.net/api/analyze_websites?total_websites=1000```

*It may take up to 30 seconds for the server to respond to your request*

### Locally


## Optional Query Params
- ### "total_websites" : Will specify how many websites to analyze. Defaults to 1000.


## Running locally
If running locally, you will need the following:

- [Python 3.6+](https://www.python.org/)
- [The Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Azure Function Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Ccsharp%2Cbash#v2)


Run ``` func start``` in the analyze_websites directory to start the function host 

Then issue a request

```GET http://localhost:7071/api/analyze_websites?total_websites=1000 ```