import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Button } from "semantic-ui-react";
import s from "./Car_description.module.css"
import { NavLink, useSearchParams } from "react-router-dom";
import ImageGallery from 'react-image-gallery';
import "react-image-gallery/styles/css/image-gallery.css";


const API_URL = `http://127.0.0.1:8000/api/cars/`;

const Car_Description = () => {
  const [car, setCar] = useState(null);


  useEffect(() => {
    const arr = window.location.pathname.split('/')
      const id = arr[arr.length-1]


    const fetchData = async (url) => {
      try {
        const response = await axios.get(url);
         const car_select = response.data;
         setCar(car_select)
      } catch (error) {
        console.error('Произошла ошибка при получении данных:', error);
      }
    };

    fetchData(API_URL + id + '/');
  }, []);

  const extractElementsInQuotes = (str) => {
    const regex = /"([^"]+)"/g;
    const elements = [];
    let match;

    while ((match = regex.exec(str)) !== null) {
      elements.push(match[1]);
    }

    return elements;
  };

  const [selectedImage, setSelectedImage] = useState(null);
  const handleImageClick = (image) => {
    setSelectedImage(image)
  };


  return (
    <div>
      {car &&
          <ul>
            <h1></h1>
            <h1 className={s.carHeader}> Продажа {car.car_title} {car.car_model} {car.car_generation}, {car.year} г.
              в {car.city}</h1>

            <div className={s.outerContainer}>
              <div className={s.imageContainer}>
                <ImageGallery
                    items={car.car_images.split(',').map(image => ({
                      original: image,
                      thumbnail: image
                    }))}
                    showFullscreenButton={true}
                    showPlayButton={true}
                    autoPlay={true}
                    infinite={true}
                    lazyload={true}
                    showThumbnails={true}
                    thumbnailPosition="bottom"
                    // thumbnailHeight="5px"
                    // thumbnailWidth="5px"
                />
              </div>

              <div className={s.tableContainer}>
                <table>
                  <tr>
                    <td>
                      <h2 className={s.textCenterBYN}>
                        <center style={{background: "#EDDA74"}}>{car.price_byn} р.</center>
                      </h2>
                      <h3 className={s.textCenterUSD}>
                        <center>{car.price_usd} $</center>
                      </h3>
                      <div>
                        <h1></h1>
                        <h1></h1>
                        <h6 className={s.textCenter2}>
                          <center>
                            {car.year} г., {car.transmission}, {car.engine} л, {car.fuel}, {car.mileage} км
                          </center>
                        </h6>
                      </div>
                      <div><h1></h1></div>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <div>
                        <h6 className={s.textCenter2}>
                          <center>
                            {car.car_body}, {car.car_drive}, {car.car_color} цвет, {car.horse_power}, {car.consumption}
                          </center>
                        </h6>
                      </div>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <center>
                        <Button className={s.button2}>Написать продавцу</Button>
                        <h6></h6>
                        <Button className={s.button}>Показать телефон</Button>
                      </center>
                    </td>
                  </tr>
                </table>
              </div>
            </div>

            <h1></h1>
            <table className={s.width2}>
              <tr>
                <td>
                  <h2>Описание</h2>
                  <h6 className={s.textCenter}>{car.description}</h6>
                </td>
              </tr>
            </table>
            <h1></h1>

            <div className={s.tableWrapper}>
              {extractElementsInQuotes(car.car_options).map((option, index) => {
                const [title, content] = option.split(': ');
                return (
                    <div
                        className={s.tableItem}
                        key={index}>
                      <b><h3>{title}</h3></b>
                      <h6></h6>
                      <h6>{content}</h6>
                    </div>
                );
              })}
            </div>

            <h1></h1>
          </ul>}
    </div>
  );
};

export default Car_Description;

