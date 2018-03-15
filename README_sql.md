## Data base creation
Заменить DataBase на название вашей базы MySQL 
### Таблица с данными из Search Console

```sql
CREATE TABLE DataBase.search_console_data (
  date date NOT NULL,
  url varchar(255) NOT NULL,
  query varchar(255) NOT NULL,
  clicks int(11) DEFAULT NULL,
  impressions int(11) DEFAULT NULL,
  ctr double DEFAULT NULL,
  `position` double DEFAULT NULL,
  category_id int(11) DEFAULT NULL,
  PRIMARY KEY (date, url, query)
)
ENGINE = INNODB
AVG_ROW_LENGTH = 152
CHARACTER SET utf8
COLLATE utf8_general_ci;
```

### Календарик пинарик для отслеживания сполного скачивания данных по стране в случае возникновения ошибок API

```sql
CREATE TABLE DataBase.search_console_calendar (
  id int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  date date NOT NULL,
  status enum ('not downloaded', 'downloaded', 'expired') DEFAULT NULL,
  PRIMARY KEY (id, date)
)
ENGINE = INNODB
AUTO_INCREMENT = 195
AVG_ROW_LENGTH = 84
CHARACTER SET utf8
COLLATE utf8_general_ci;
```

### Общая таблица с данными для подключения к API

```sql
CREATE TABLE DataBase.search_console_property (
  id int(10) NOT NULL AUTO_INCREMENT,
  property_uri varchar(255) NOT NULL,
  service_account varchar(255) DEFAULT NULL,
  key_file varchar(255) DEFAULT NULL,
  PRIMARY KEY (id, property_uri)
)
ENGINE = INNODB
AUTO_INCREMENT = 38
AVG_ROW_LENGTH = 442
CHARACTER SET utf8
COLLATE utf8_general_ci;
```

### Таблица с списком SEO категорий

```sql
CREATE TABLE DataBase.category_data (
  category_id int(11) NOT NULL AUTO_INCREMENT,
  category_name varchar(255) NOT NULL,
  PRIMARY KEY (category_id)
)
ENGINE = INNODB
AVG_ROW_LENGTH = 152
CHARACTER SET utf8
COLLATE utf8_general_ci;
```

### Таблица с списком страниц и связи с SEO категориями

```sql
CREATE TABLE DataBase.site_url_data (
  page_id int(11) NOT NULL,
  url varchar(255) NOT NULL,
  category_id int(11) NOT NULL,
  PRIMARY KEY (page_id)
)
ENGINE = INNODB
AVG_ROW_LENGTH = 152
CHARACTER SET utf8
COLLATE utf8_general_ci;
```
