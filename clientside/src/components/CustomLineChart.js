import React from 'react'
import { LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Line } from 'recharts'
import PropTypes from 'prop-types'


const CustomLineChart = ({ data, xName, yName }) => {
  if (data === undefined || xName === undefined || yName === undefined) return
  return (
    <LineChart
      width={730}
      height={250}
      data={data}
      margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey={xName} />
      <YAxis />
      <Tooltip />
      <Line type="monotone" dataKey={yName} stroke="#8884d8" />
    </LineChart>
  )
}

export default CustomLineChart
