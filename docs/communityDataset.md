# Awesome-gee-community-datasets 


``` mermaid
graph LR
  A[Overarching Category] --> B{Markdown file for the page};
  B --->|Render on github.io site| C[Description, Citation, Earth Engine Snippet, DOI, License];
```
``` mermaid
graph LR
  B[Community Datasets JSON] --> C{title, sample code, type, id, provider, tags};
  A[Community Datasets CSV] --> C{title, sample code, type, id, provider, tags};
  C --> D[additional JSONs to describe corresponding datasets in the catalog];
```
