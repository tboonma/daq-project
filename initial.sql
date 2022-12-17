-- create bus stop table
CREATE TABLE IF NOT EXISTS bus_stop (
  id INT PRIMARY KEY AUTO_INCREMENT,
  bus_stop_id varchar(50) NOT NULL UNIQUE,
  bus_stop_name varchar(100) NOT NULL UNIQUE,
  lat float NOT NULL,
  lon float NOT NULL,
  verified BOOLEAN NOT NULL DEFAULT FALSE
);

-- create route table
CREATE TABLE IF NOT EXISTS `route` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    bus_number INT NOT NULL,
    bus_stop_id INT NOT NULL,
    FOREIGN KEY (bus_stop_id)
      REFERENCES bus_stop(id)
      ON DELETE CASCADE
);

-- create open meteo table
CREATE TABLE IF NOT EXISTS open_meteo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    bus_stop_id INT NOT NULL,
    temperature FLOAT NOT NULL,
    windspeed FLOAT NOT NULL,
    FOREIGN KEY (bus_stop_id)
      REFERENCES bus_stop(id)
      ON DELETE CASCADE
);

-- create Aqicn table
CREATE TABLE IF NOT EXISTS aqi (
  id INT PRIMARY KEY AUTO_INCREMENT,
  ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  bus_stop_id INT NOT NULL,
  value FLOAT NOT NULL,
  FOREIGN KEY (bus_stop_id)
    REFERENCES bus_stop(id)
    ON DELETE CASCADE
);

-- create IQAir table
CREATE TABLE IF NOT EXISTS iqair (
  id INT PRIMARY KEY AUTO_INCREMENT,
  ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  bus_stop_id INT NOT NULL,
  temperature FLOAT NOT NULL,
  humidity FLOAT NOT NULL,
  wind_speed FLOAT NOT NULL,
  pm25_value FLOAT NOT NULL,
  FOREIGN KEY (bus_stop_id)
    REFERENCES bus_stop(id)
    ON DELETE CASCADE
);

-- create population table
CREATE TABLE IF NOT EXISTS population (
  id INT PRIMARY KEY AUTO_INCREMENT,
  ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  bus_stop_id INT NOT NULL,
  FOREIGN KEY (bus_stop_id)
    REFERENCES bus_stop(id)
    ON DELETE CASCADE
);

-- create weather table
CREATE TABLE IF NOT EXISTS weather (
  id INT PRIMARY KEY AUTO_INCREMENT,
  ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  bus_stop_id INT NOT NULL,
  sensor VARCHAR(100) NOT NULL,
  source VARCHAR(100) NOT NULL,
  value FLOAT NOT NULL,
  FOREIGN KEY (bus_stop_id)
    REFERENCES bus_stop(id)
    ON DELETE CASCADE
);
