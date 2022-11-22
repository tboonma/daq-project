-- create bus stop table
CREATE TABLE bus_stop (
  bus_stop_id INT PRIMARY KEY AUTO_INCREMENT,
  bus_stop_name varchar(100) NOT NULL,
  lat float NOT NULL,
  lon float NOT NULL
  population INT DEFAULT 0
)

-- create route table
CREATE TABLE route (
    id INT PRIMARY KEY AUTO_INCREMENT,
    route_number INT NOT NULL,
    name varchar(200) NOT NULL
)

-- create bus table
CREATE TABLE bus (
    id INT NOT NULL AUTO_INCREMENT,
    bus_number INT NOT NULL,
    bus_stop_id INT NOT NULL,
    route_id INT NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (bus_number),
    FOREIGN KEY (bus_stop_id) REFERENCES bus_stop(bus_stop_id),
    FOREIGN KEY (route_id) REFERENCES route(id)
)

-- create open meteo table
CREATE TABLE open_meteo (
    id INT NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    bus_stop_id INT NOT NULL,
    temperature FLOAT NOT NULL,
    windspeed FLOAT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (bus_stop_id) REFERENCES bus_stop(bus_stop_id)
)

-- create Aqicn table
CREATE TABLE aqi (
  id INT NOT NULL AUTO_INCREMENT,
  ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  bus_stop_id INT NOT NULL,
  value FLOAT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (bus_stop_id) REFERENCES bus_stop(bus_stop_id)
)