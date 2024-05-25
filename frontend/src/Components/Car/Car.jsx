import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TablePagination from '@mui/material/TablePagination';
import s from './Car.module.css';
import { Button } from "semantic-ui-react";
import "semantic-ui-css/semantic.min.css";
import { NavLink, useNavigate } from "react-router-dom";
import { useGlobal } from "../../context/globalContext";

const Car = () => {
  const { cars, setPage, page, setRowsPerPage, rowsPerPage, totalItems, getCars } = useGlobal();
  const navigate = useNavigate();

  useEffect(()=> {
    getCars(rowsPerPage);
  }, [page, rowsPerPage])

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

  const TableCell = ({ text, characterLimit }) => {
    const [expanded, setExpanded] = useState(false);

    const handleToggleExpand = () => {
      setExpanded(!expanded);
    };

    if (!text) {
      return <td></td>
    }
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

    <div className={s.width}>
      {Array.isArray(cars) && cars.map(data => (
        <table className={s.listing_item__wrap} key={data.id}>
          <tr>
            <th rowSpan="2">
              <center><img src={data.main_car_image} alt="Фото" height="180" width="230"/></center>
            </th>
            <td>
              <h3>
                <center><NavLink to={`/cars/${data.id}`}>{data.car_title}</NavLink></center>
              </h3>
            </td>
            <td>
              <center>
                <div>{data.year} г., {data.transmission}</div>
                <div>{data.engine}, {data.fuel}</div>
                <div>{data.body}</div>
                <div>{data.mileage} км</div>
              </center>
            </td>
            <td>
              <h3>
                <center style={{ background: "#EDDA74" }}>{data.price_byn} р.</center>
              </h3>
              <h6>
                <center>{data.price_usd} $</center>
              </h6>
            </td>
          </tr>
          <tr>
            <th colSpan="2" style={{ fontWeight: "normal" }}>
              <h5><TableCell text={data.description} characterLimit={135}/></h5>
            </th>
            <td>
              <h3>
                <center>{data.city}</center>
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
}

export default Car;