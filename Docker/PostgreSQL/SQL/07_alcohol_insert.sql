COPY 
    alcohol 
FROM 
    '/docker-entrypoint-initdb.d/cocktail_data.csv' 
WITH 
    CSV HEADER Delimiter ',';