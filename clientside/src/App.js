import './App.css'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import Navbar from './components/Navbar'
import InputLabel from '@mui/material/InputLabel'
import MenuItem from '@mui/material/MenuItem'
import FormControl from '@mui/material/FormControl'
import Select from '@mui/material/Select'
import Button from '@mui/material/Button'
import React, { useState, useEffect } from 'react'
import DefaultApi from './generated/src/api/DefaultApi'
import ApiClient from './generated/src/ApiClient'
import CustomLineChart from './components/CustomLineChart'
import CustomBarChart from './components/CustomBarChart'

function App() {
  const [origin, setOrigin] = useState('')
  const [destination, setDestination] = useState('')
  const [busstops, setBusstops] = useState([])
  const [weatherBusstop, setWeatherBusstop] = useState('')
  const [displayInsertButton, setInsertButton] = useState(false)
  const [weatherData, setWeatherData] = useState('')
  const [populationData, setPopulationData] = useState('')
  const [populationBusstop, setPopulationBusstop] = useState('')
  const [aqiBusstop, setAqiBusstop] = useState('')
  const [aqiData, setAqiData] = useState('')
  const [takableBus, setTakableBus] = useState('')

  let api = undefined
  if (window.location.href.includes('localhost')) {
    api = new DefaultApi()
  } else {
    const apiClient = new ApiClient('/talai-api/v1')
    api = new DefaultApi(apiClient)
  }

  const insertPopulation = (e) => {
    e.preventDefault()
    api.controllerPutPopulation(origin.id, () => setInsertButton(false))
  }

  const changeOriginHandler = (event) => {
    event.preventDefault()
    setOrigin(event.target.value)
    setInsertButton(true)
  }

  const changeWeatherHandler = (event) => {
    event.preventDefault()
    setWeatherBusstop(event.target.value)
  }

  const changePopulationHandler = (event) => {
    event.preventDefault()
    setPopulationBusstop(event.target.value)
  }

  const changeAqiHandler = (event) => {
    event.preventDefault()
    setAqiBusstop(event.target.value)
  }

  const createWeatherChart = async (sensorBusstop) => {
    if (sensorBusstop === undefined || sensorBusstop === '') return
    const resp = await fetch('/graphql', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      },
      body: JSON.stringify({
        query: `
        {
          busstopTemperature(stopId: ${sensorBusstop.id}) {
            amount,
            timestamp
          }
        }`
      })
    })
    var json = await resp.json()
    var table = json.data
    return table
  }

  const createAqiChart = async (sensorBusstop) => {
    if (sensorBusstop === undefined || sensorBusstop === '') return
    const resp = await fetch('/graphql', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      },
      body: JSON.stringify({
        query: `
        {
          busstopAqi(stopId: ${sensorBusstop.id}) {
            amount,
            timestamp
          }
        }`
      })
    })
    var json = await resp.json()
    var table = json.data
    return table
  }

  const createPopulationChart = async () => {
    if (populationBusstop === undefined || populationBusstop === '') return
    const resp = await fetch('/graphql', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      },
      body: JSON.stringify({
        query: `
        {
          population(stopId: ${populationBusstop.id}) {
            timestamp,
            amount
          }
        }`
      })
    })
    var json = await resp.json()
    var table = json.data
    setPopulationData(table.population)
  }

  const findBus = async (event) => {
    event.preventDefault()
    const resp = await fetch('/graphql', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      },
      body: JSON.stringify({
        query: `
        {
          bus(stopIdOrigin: ${origin.id}, stopIdDest: ${destination.id}) {
            routeNumber
          }
        }`
      })
    })
    var json = await resp.json()
    var table = json.data
    console.log(table.bus)
    let availableBus = ''
    table.bus.forEach((bus) => (availableBus += bus.routeNumber + ', '))
    if (availableBus === '') availableBus = 'Cannot take only 1 bus to go there'
    setTakableBus(availableBus.slice(0, -2))
  }

  useEffect(() => {
    createAqiChart(aqiBusstop).then((val) => {
      if (val !== undefined) setAqiData(val.busstopAqi)
    })
  }, [aqiBusstop])

  useEffect(() => {
    createPopulationChart()
  }, [populationBusstop])

  useEffect(() => {
    createWeatherChart(weatherBusstop).then((val) => {
      if (val !== undefined) setWeatherData(val.busstopTemperature)
    })
  }, [weatherBusstop])

  useEffect(() => {
    api.controllerGetBusstops((err, data, res) => {
      setBusstops(data)
    })
  }, [])

  return (
    <div className="">
      <link
        rel="stylesheet"
        href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
        integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
        crossOrigin=""
      />
      <Navbar />
      <div className="py-6 md:pt-20 md:px-14 md:flex md:space-x-3">
        <div className="h-[60vh] w-[100vw] md:w-[65vw]">
          <MapContainer
            center={[13.848584, 100.571825]}
            zoom={16}
            scrollWheelZoom={false}
            style={{ height: '100%', width: '100%' }}
          >
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker
              position={[
                destination.lat ?? 13.848584,
                destination.lon ?? 100.571825
              ]}
            >
              <Popup>{destination.name ?? 'Please select destination'}</Popup>
            </Marker>
            <Marker
              position={[origin.lat ?? 13.848584, origin.lon ?? 100.571825]}
            >
              <Popup>{origin.name ?? 'Please select starting point'}</Popup>
            </Marker>
          </MapContainer>
        </div>
        <div className="md:w-[25vw] mt-8 md:mt-0 flex items-center">
          <div className="space-y-3 w-full text-center">
            <h1>Direction from:</h1>
            <FormControl className="w-5/6" size="small">
              <InputLabel id="demo-select-small">Origin</InputLabel>
              <Select
                labelId="demo-select-small"
                id="demo-select-small"
                value={origin}
                label="origin"
                onChange={changeOriginHandler}
              >
                {busstops.map((busstop) => (
                  <MenuItem key={busstop.id} value={busstop}>
                    {busstop.name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
            {displayInsertButton && (
              <Button variant="contained" onClick={insertPopulation}>
                {"I'M HERE"}
              </Button>
            )}
            <h1>To</h1>
            <FormControl className="w-5/6" size="small">
              <InputLabel id="demo-select-small">Destination</InputLabel>
              <Select
                labelId="demo-select-small"
                id="demo-select-small"
                value={destination}
                label="destination"
                onChange={(e) => setDestination(e.target.value)}
              >
                {busstops.map((busstop) => (
                  <MenuItem key={busstop.id} value={busstop}>
                    {busstop.name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
            {origin !== '' && destination !== '' && (
              <Button variant="contained" onClick={findBus}>
                {'FIND BUS'}
              </Button>
            )}
            <p>Take bus number: </p>
            {takableBus}
          </div>
        </div>
      </div>
      <div className="py-6 md:px-14 text-center md:text-left space-y-3">
        <div className="text-xl font-semibold">Temperature history</div>
        <FormControl className="w-2/6" size="small">
          <InputLabel id="demo-select-small">Location</InputLabel>
          <Select
            labelId="demo-select-small"
            id="demo-select-small"
            value={weatherBusstop}
            label="location"
            onChange={changeWeatherHandler}
          >
            {busstops.map((busstop) => (
              <MenuItem key={busstop.id} value={busstop}>
                {busstop.name}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
        {weatherData !== '' && (
          <CustomLineChart
            data={weatherData}
            xName="timestamp"
            yName="amount"
          />
        )}
      </div>
      <div className="py-6 md:px-14 text-center md:text-left space-y-3">
        <div className="text-xl font-semibold">Population Density</div>
        <FormControl className="w-2/6" size="small">
          <InputLabel id="demo-select-small">Location</InputLabel>
          <Select
            labelId="demo-select-small"
            id="demo-select-small"
            value={populationBusstop}
            label="location"
            onChange={changePopulationHandler}
          >
            {busstops.map((busstop) => (
              <MenuItem key={busstop.id} value={busstop}>
                {busstop.name}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
        {populationData !== '' && (
          <CustomBarChart
            data={populationData}
            xName="timestamp"
            yName="amount"
          />
        )}
      </div>
      <div className="py-6 md:px-14 text-center md:text-left space-y-3">
        <div className="text-xl font-semibold">PM2.5 History</div>
        <FormControl className="w-2/6" size="small">
          <InputLabel id="demo-select-small">Location</InputLabel>
          <Select
            labelId="demo-select-small"
            id="demo-select-small"
            value={aqiBusstop}
            label="location"
            onChange={changeAqiHandler}
          >
            {busstops.map((busstop) => (
              <MenuItem key={busstop.id} value={busstop}>
                {busstop.name}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
        {aqiData !== '' && (
          <CustomLineChart data={aqiData} xName="timestamp" yName="amount" />
        )}
      </div>
    </div>
  )
}

export default App
