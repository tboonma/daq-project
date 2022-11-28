import React from 'react'
import { BarChart, CartesianGrid, XAxis, YAxis, Tooltip, Bar } from 'recharts'

const CustomBarChart = ({ data, xName, yName }) => {
  if (data === undefined || xName === undefined || yName === undefined) return
  return (
    <BarChart width={730} height={250} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey={xName} />
      <YAxis />
      <Tooltip />
      <Bar dataKey={yName} fill="#8884d8" />
    </BarChart>
  )
}

export default CustomBarChart
