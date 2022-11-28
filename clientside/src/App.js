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

function App() {
  const [origin, setOrigin] = useState('')
  const [destination, setDestination] = useState('')
  const [busstops, setBusstops] = useState([])
  const [displayInsertButton, setInsertButton] = useState(false)
  const apiClient = new ApiClient("/talai-api/v1")
  const api = new DefaultApi(apiClient)

  const insertPopulation = (e) => {
    e.preventDefault()
    api.controllerPutPopulation(origin.busstopId, () => setInsertButton(false))
  }

  const changeOriginHandler = (event) => {
    event.preventDefault()
    setOrigin(event.target.value)
    setInsertButton(true)
  }

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
      <div className="pt-10 md:pt-20 md:px-14 md:flex md:space-x-3">
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
                  <MenuItem key={busstop.busstopId} value={busstop}>
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
                  <MenuItem key={busstop.busstopId} value={busstop}>
                    {busstop.name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
