# Awesome-gee-community-datasets 

## Flowchart for the STAC specification used with the community datasets

``` mermaid
graph LR
  B[Community Datasets JSON] --> C{title, sample code, type, id, provider, tags};
  A[Community Datasets CSV] --> C{title, sample code, type, id, provider, tags};
  C --> D[additional JSONs to describe corresponding datasets in the catalog];
```

## Flowchart for the project markdown files that are rendering on the github.io site

``` mermaid
graph LR
  A[Overarching Category] --> B{Markdown file for the page};
  B --->|Render on github.io site| C[Description, Citation, Earth Engine Snippet, DOI, License];
```

However, this information varies slightly for each dataset:
- some are missing key info such as the DOI 
- others include different additional specific information on the dataset that are an exception from the norm
- additionally, the descriptions vary heavily in detail between the datasets 

It appears that the user is contributing this information for the project file when they submit their dataset to be included in the project. There are procedures for submitting datasets, including what info to include; however, it seems that this isn't being strictly adhered to. 

*Question: are the contributors also providing the information for the JSON files? because these seem much more correctly standardized to the STAC specification guidelines*


