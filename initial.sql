-- create bus stop table
CREATE TABLE IF NOT EXISTS N bus_stop (
  bus_stop_id INT PRIMARY KEY AUTO_INCREMENT,
  bus_stop_name varchar(100) NOT NULL,
  lat float NOT NULL,
  lon float NOT NULL
  population INT DEFAULT 0
);

-- create route table
CREATE TABLE IF NOT EXISTS route (
    id INT PRIMARY KEY AUTO_INCREMENT,
    route_number INT NOT NULL,
    name varchar(200) NOT NULL
);

-- create bus table
CREATE TABLE IF NOT EXISTS bus (
    id INT NOT NULL AUTO_INCREMENT,
    bus_number INT NOT NULL,
    bus_stop_id INT NOT NULL,
    route_id INT NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (bus_number),
    FOREIGN KEY (bus_stop_id) REFERENCES bus_stop(bus_stop_id),
    FOREIGN KEY (route_id) REFERENCES route(id)
);

-- create open meteo table
CREATE TABLE IF NOT EXISTS open_meteo (
    id INT NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    bus_stop_id INT NOT NULL,
    temperature FLOAT NOT NULL,
    windspeed FLOAT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (bus_stop_id) REFERENCES bus_stop(bus_stop_id)
);

-- create Aqicn table
CREATE TABLE IF NOT EXISTS aqi (
  id INT NOT NULL AUTO_INCREMENT,
  ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  bus_stop_id INT NOT NULL,
  value FLOAT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (bus_stop_id) REFERENCES bus_stop(bus_stop_id)
);

-- create IQAir table
CREATE TABLE IF NOT EXISTS iqair (
  id INT NOT NULL AUTO_INCREMENT,
  ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  bus_stop_id INT NOT NULL,
  temperature FLOAT NOT NULL,
  humidity FLOAT NOT NULL,
  wind_speed FLOAT NOT NULL,
  pm25_value FLOAT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (bus_stop_id) REFERENCES bus_stop(bus_stop_id)
);