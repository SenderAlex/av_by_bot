import React, { useEffect, useState } from "react";
import axios from "axios";

const GlobalContext = React.createContext();

const API_URL = 'http://127.0.0.1:8000/api/filtered_cars/'

function GlobalProvider(props) {
  const [cars, setCars] = useState([]);
  const [totalItems, setTotalItems] = useState(0);  // pagination
  const [page, setPage] = useState(1);  // pagination
  const [rowsPerPage, setRowsPerPage] = useState(25);  // pagination

  async function getCars(limit) {
    try {
      const response = await axios.get(API_URL, {
        params: {
          page: page, // pagination
          limit: limit,
        },
      });
      setCars(response.data.results); // устанавливаем новый список данных
      setTotalItems(response.headers['x-total_count']); // сохраняем общее количество элементов data.length
    } catch (error) {
      console.log(error);
    }
  };


  async function getNewCars(limit) {
    try {
      const response = await axios.get(API_URL, {
        params: {
          page: page, // pagination
          limit: limit,
        },
      });
      if (Array.isArray(response.data.results)) {
        const newCars = response.data.results.filter(car => car.year >= 2024);
        setCars(newCars); // устанавливаем новый список данных
      setTotalItems(response.headers['x-total_count']); // сохраняем общее количество элементов data.length
      } else {
        console.error('Данные не являются массивом.');
      }
    } catch (error) {
      console.log(error);
    }
  };


  async function getElectricCars(limit) {
    try {
      const response = await axios.get(API_URL, {
        params: {
          page: page, // pagination
          limit: limit,
        },
      });
      if (Array.isArray(response.data.results)) {
        const electricCars = response.data.results.filter(car => car.engine.toLowerCase() === 'электро');
        setCars(electricCars); // устанавливаем новый список данных
      setTotalItems(response.headers['x-total_count']); // сохраняем общее количество элементов data.length
      } else {
        console.error('Данные не являются массивом.');
      }
    } catch (error) {
      console.log(error);
    }
  };


  async function getMileAgeCars(limit) {
    try {
      const response = await axios.get(API_URL, {
        params: {
          page: page, // pagination
          limit: limit,
        },
      });
      if (Array.isArray(response.data.results)) {
        const mileageCars = response.data.results.filter(car => car.year <= 2023);
        setCars(mileageCars); // устанавливаем новый список данных
      setTotalItems(response.headers['x-total_count']); // сохраняем общее количество элементов data.length
      } else {
        console.error('Данные не являются массивом.');
      }
    } catch (error) {
      console.log(error);
    }
  };

  async function getFilteredCars(url) {
    try {
      const response = await axios.get(url, );
      console.log(response)
      setCars(response.data.results); // устанавливаем новый список данных
      setTotalItems(response.data.count); // сохраняем общее количество элементов data.length
    } catch (error) {
      console.log(error);
    }
  };


  return (
    <GlobalContext.Provider
      value={{
        cars: cars,
        totalItems: totalItems,
        page: page,
        rowsPerPage: rowsPerPage,
        setPage: (v) => setPage(v),
        setRowsPerPage: (v) => setRowsPerPage(v),
        getCars: getCars,
        getNewCars: getNewCars,
        getElectricCars: getElectricCars,
        getMileAgeCars: getMileAgeCars,
        getFilteredCars: getFilteredCars,
      }}>
      {props.children}
    </GlobalContext.Provider>
  );
}

function useGlobal() {
  const context = React.useContext(GlobalContext);
  if (context === undefined) {
    throw new Error('useGlobal must be used within GlobalProvider');
  }

  return context;
}

export { useGlobal, GlobalProvider };