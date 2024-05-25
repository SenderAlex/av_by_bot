import React, { useState } from "react";
import { Button } from "semantic-ui-react";
import "semantic-ui-css/semantic.min.css";
import s from './navigation.module.css';
import { Link } from "react-router-dom";
import New_Car from "../New Auto/New_Car";
import { useGlobal } from "../../context/globalContext";
import { useNavigate } from "react-router-dom";


const NavigationMenu = () => {

   const navigate = useNavigate();

    const handleClickNewCar = () => {
        navigate('/new-cars')
    }

    const handleClickElectricCar = () => {
        navigate('/electric-cars')
    }

    const handleClickMileAgeCar = () => {
        navigate('/mileage-cars')
    }


    const handleClickEntrance = () => {
        navigate('/entrance')
    }

  return (
    <div>
      <nav>
        <div className={s.container}>
          <div><Link to='/'><img className={s.logo} src='/logo.png' alt="logo"/></Link></div>
          <div>
            <Button className={s.button} onClick={handleClickNewCar}>Новые авто</Button>
            <Button className={s.button} onClick={handleClickMileAgeCar}>Авто с пробегом</Button>
            <Button className={s.button} onClick={handleClickElectricCar}>Электромобили</Button>
          </div>
        </div>
        <div className={s.buttons_container}>
          <Button className={s.button} onClick={handleClickEntrance}>Войти</Button>
          <Button className={s.button} onClick={handleClickEntrance}>Подать объявление</Button>
        </div>
      </nav>
    </div>
  );
};

export default NavigationMenu;

