import React, {useEffect, useState} from 'react';
import axios from 'axios';
import TablePagination from '@mui/material/TablePagination';
import s from "./Electric_Car.module.css"
import {Button} from "semantic-ui-react";
import "semantic-ui-css/semantic.min.css";
import {NavLink, useNavigate} from "react-router-dom";
import {useGlobal} from "../../context/globalContext";


const Electric_Car = () => {
  const { cars, setPage, page, setRowsPerPage, rowsPerPage, totalItems, getElectricCars } = useGlobal();
  const navigate = useNavigate();

  useEffect(()=> {
    getElectricCars();
  }, [page])

  const handleChangePage = (event, newPage) => {  // pagination
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {  // pagination
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  const carClickHandler = (id)=>{
    navigate(`/cars/${id}`)
  }

  ///

  const TableCell = ({ text, characterLimit }) => {
  const [expanded, setExpanded] = useState(false);

  const handleToggleExpand = () => {
    setExpanded(!expanded);
  };

  const truncatedText = text.slice(0, characterLimit);
  const displayText = expanded ? text : truncatedText;
  const showToggle = text.length > characterLimit;

  return (
    <td>
      {displayText}
      {showToggle && (
        <Button primary onClick={handleToggleExpand} style={{ padding: "0.25rem 0.5rem", fontSize: "0.75rem" }}>
          {expanded ? "Скрыть" : "Показать"}
        </Button>
      )}
    </td>
  );
  };

  return (
      <div>
        <h1></h1>
        <h1></h1>
        {cars.map(car => (

            <table className={s.width} key={car.id}>
              <tr>
                <th rowSpan="2">
                  <center><img src={car.main_car_image} alt="Фото" height="180" width="230"/></center>
                </th>
                <td>
                  <h3>
                    <NavLink to={`/cars/${car.id}`} onClick={() => carClickHandler(car.id)}>
                      {car.car_title}
                    </NavLink>
                  </h3>
                </td>
                <td>
                  <center>
                    <div>{car.year} г., {car.transmission}</div>
                    <div>{car.engine}, {car.fuel}</div>
                    <div>{car.body}</div>
                    <div>{car.mileage} км</div>
                  </center>
                </td>
                <td>
                  <h3>
                    <center style={{background: "#EDDA74"}}>{car.price_byn} р.</center>
                  </h3>
                  <h6>
                    <center>{car.price_usd} $</center>
                  </h6>
                </td>
              </tr>
              <tr>
                <th colSpan="2" style={{fontWeight: "normal"}}>
                  <h5><TableCell text={car.description} characterLimit={135}/></h5>
                </th>
                <td>
                  <h3>
                    <center>{car.city}</center>
                  </h3>
                </td>
              </tr>
            </table>
        ))}
        <TablePagination
            component="div"
            count={totalItems}
            page={page}
            onPageChange={handleChangePage}
            rowsPerPage={rowsPerPage}
            onRowsPerPageChange={handleChangeRowsPerPage}
        />
      </div>
  );
};

export default Electric_Car;
