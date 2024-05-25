import React, {useState, useEffect} from "react";
import "semantic-ui-css/semantic.min.css";
import axios from "axios";
import s from "./Car_Title.module.css"
import {Link} from "react-router-dom";
import { Button } from "semantic-ui-react";
import {useContext} from "react";
import {CarTitleContext} from "../../context/globalCarTitle";


const CarTitle_URL = 'http://127.0.0.1:8000/api/car_titles/'

const Car_Title = () => {

    const [CarTitles, setCarTitles] = useState([]);
    const [showAllModels, setShowAllModels] = useState(false);
    const {handleCarTitleClick} = useContext(CarTitleContext)

    const fetchData = async (url) => {
        try {
            const response = await axios.get(CarTitle_URL);
            if (Array.isArray(response.data)) {
                const titles = response.data;
                setCarTitles(titles);
            } else {
                console.error('Данные не являются массивом.');
            }
        } catch (error) {
            console.error('Произошла ошибка при получении данных:', error);
        }
    };

    //хук -- вызываться каждый раз когда обновляется компонента
    useEffect(() => {
        fetchData(CarTitle_URL)
    }, [])

    const toggleShowAllModels = () => {
        setShowAllModels(!showAllModels);
    };

    const displayedCarTitles = showAllModels ? CarTitles : CarTitles.slice(0, 30);

    return (
        <div className={s.width}>
            <h1 className={s.h1}><b>Объявления о продаже автомобилей с пробегом в Беларуси</b></h1>
            <nav>
                <table>
                    {Array.from({length: Math.ceil(CarTitles.length / 5)}).map((_, rowIndex) => (
                        <tr key={rowIndex}>
                            {displayedCarTitles.slice(rowIndex * 5, rowIndex * 5 + 5).map((CarTitle) => (
                                <td className={s.width} key={CarTitle.id}>
                                 <span>
                                <Link to={`/${CarTitle.car_title.toLowerCase()}`}
                                      onClick={() => handleCarTitleClick(CarTitle.car_title)}>
                                    {CarTitle.car_title}
                                </Link>
                                 </span>
                                </td>

                            ))}
                        </tr>
                    ))}
                </table>
            </nav>
            <Button style={{marginTop: '10px', marginBottom: '10px'}} primary onClick={toggleShowAllModels}>
                {showAllModels ? "Оставить 30 моделей" : "Показать все модели"}
            </Button>
        </div>
    );
};

export default Car_Title;
