import React, { useState, useEffect } from 'react';
import {useContext} from "react";
import {CarModelContext} from "../../context/globalCarModel";
import {Link} from "react-router-dom";
import s from "./Car_Generation.module.css"
import {CarTitleContext} from "../../context/globalCarTitle";

const CarGeneration_URL = 'http://127.0.0.1:8000/api/car_generations/car_generations_by_model/?car_model='

const Car_Generation = () => {
    const [generations, setGenerations] = useState([]);
    const {carTitle} = useContext(CarTitleContext);
    const {carModel} = useContext(CarModelContext);

    useEffect(() => {
        fetch(CarGeneration_URL + carModel)
            .then(response => response.json())
            .then(data => setGenerations(data));
    }, [carModel]);

    return (
        <div>
            <h2>Поколения автомобилей марки {carModel}</h2>
            <table className={s.tableWrapper}>
                {Array.from({length: Math.ceil(generations.length / 6)}).map((_, rowIndex) => (
                    <tr key={rowIndex}>
                        {generations && generations.slice(rowIndex * 6, rowIndex * 6 + 6).map((generation) => (
                            <td className={s.width} key={generation.id}>
                                    <span>
                                        <Link to={`/${carTitle.toLowerCase()}/${carModel.toLowerCase()}
                                        /${generation.car_generation.toLowerCase()}`}
                                        >
                                            {generation.car_generation}
                                        </Link>
                                    </span>
                            </td>
                        ))}
                    </tr>
                ))}
            </table>
        </div>
    );
}

export default Car_Generation;