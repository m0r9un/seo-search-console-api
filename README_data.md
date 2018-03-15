# Data types with examples

## search_console_property table

Example:

```
id	property_uri	service_account	key_file
1	https://flatfy.com/	google-search-api-flatfy@some-word-numbers.iam.gserviceaccount.com	GoogleAPIsFlatfy.p12
```

## search_console_calendar table

Example:

```
id	date	status
195	2018-03-08	not downloaded
```

date format - yyyy-mm-dd

Choose "not downloaded" status to download data for this day.

## category_data table

Example:

```
category_id	category_name
1	Test category
```

Category - seo category of page. Ex: /rent-flat-kyiv, /rent-flat-odesa = "Rent Flat in City" category

## site_url_data table

Example:

```
id	url	category_id
3	/rent-flat	2
```

id - any id that you use in your data base
category_id - id from category_data
