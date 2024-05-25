import React, { useState, useEffect } from 'react';
import {useContext} from "react";
import {CarTitleContext} from "../../context/globalCarTitle";
import {Link} from "react-router-dom";
import s from "./Car_Model.module.css"
import {CarModelContext} from "../../context/globalCarModel";
import SearchCar from "../Search/Search";

const CarModel_URL = 'http://127.0.0.1:8000/api/car_models/car_models_by_title/?car_title='


const Car_Model = () => {
    const [carModels, setCarModels] = useState([]);
    const {carTitle} = useContext(CarTitleContext);
    const {handleCarModelClick} = useContext(CarModelContext)

    useEffect(() => {
        fetch(CarModel_URL + carTitle)
            .then(response => response.json())
            .then(data => setCarModels(data));
    }, [carTitle]);

    return (
        <div>
            <h2>Модели автомобилей марки {carTitle}</h2>
            <table className={s.tableWrapper}>
                {Array.from({length: Math.ceil(carModels.length / 6)}).map((_, rowIndex) => (
                    <tr key={rowIndex}>
                        {carModels && carModels.slice(rowIndex * 6, rowIndex * 6 + 6).map((carModel) => (
                            <td className={s.width} key={carModel.id}>
                                    <span>
                                        <Link to={`/${carTitle.toLowerCase()}/${carModel.car_model.toLowerCase()}`}
                                              onClick={() => handleCarModelClick(carModel.car_model)}
                                        >
                                            {carModel.car_model}
                                        </Link>
                                    </span>
                            </td>
                        ))}
                    </tr>
                ))}
            </table>
            {/*<SearchCar autobrand={carTitle}/>*/}
        </div>
    );
}

export default Car_Model;

