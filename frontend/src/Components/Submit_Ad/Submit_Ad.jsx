
import React, {useEffect, useState} from 'react';
import axios from 'axios';
import s from "../Submit_Ad/Submid_Ad.module.css";
import {Button, Modal, select} from "semantic-ui-react";
import {NavLink, useNavigate} from "react-router-dom";


const CarTitle_URL = 'http://127.0.0.1:8000/api/car_titles/'
const CarModel_URL = 'http://127.0.0.1:8000/api/car_models/car_models_by_title/'
const CarGeneration_URL = 'http://127.0.0.1:8000/api/car_generations/car_generations_by_model/'

const CarTransmission_URL= 'http://127.0.0.1:8000/api/car_transmissions/'
const CarEngine_URL = 'http://127.0.0.1:8000/api/car_engines/'
const CarEngineType_URL = 'http://127.0.0.1:8000/api/car_engine_types/'
const CarBody_URL = 'http://127.0.0.1:8000/api/car_bodies/'
const CarDrive_URL = 'http://127.0.0.1:8000/api/car_drives/'
const APICar_URL = 'http://127.0.0.1:8000/api/car-create/'  //?????

const FormCarDataComponent = () => {
    const [formData, setFormData] = useState({car_title: '', car_model: '',
        car_generation: '', car_vin: '', main_car_image: '', car_images: '', year: '', transmission: '',
        engine: '', fuel: '', car_body: '', car_drive: '', car_color: '', horse_power: '', consumption: '',
        mileage: '', price_byn: '', price_usd: '', description: '', car_options: '', http_link: ''})
    const [message, setMessage] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const [modalWindow, setModalWindow] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post(APICar_URL, formData)
            .then(response => {
                console.log(response.data);
                console.log('Data sent successfully');

                if (response.status === 201) {
                    setMessage('Ваше объявление о продаже авто успешно добавлено!!')
                    setModalWindow(true)
                    setFormData({
                        car_title: '', car_model: '', car_generation: '', car_vin: '', main_car_image: '',
                        car_images: '', year: '', transmission: '', engine: '', fuel: '', car_body: '', car_drive: '',
                        car_color: '', horse_power: '', consumption: '', mileage: '', price_byn: '', price_usd: '',
                        description: '', car_options: '', http_link: ''
                    })}
                    setErrorMessage('')
                })
            .catch(error => {
                console.error('Failed to send data:', error);
                setErrorMessage(error.response.data)
                setModalWindow(true)
            });
    };

    const [CarTitle, setCarTitle] = useState([]);
    const fetchCarTitle = async (url) => {
    try {
      const response = await axios.get(url);
      if (Array.isArray(response.data)) {
        const title = response.data;
        setCarTitle(title);
      } else {
        console.error('Данные не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных:', error);
    }
  };

    const [CarModel, setCarModel] = useState([]);
    const fetchCarModel = async (url, car_title) => {
    try {
      const response = await axios.get(url, { params: { car_title } });
      if (Array.isArray(response.data)) {
        const models = response.data;
        setCarModel(models);
      } else {
        console.error('Данные о моделях не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных о моделях:', error);
    }
  };


    const [CarGeneration, setCarGeneration] = useState([]);
    const fetchCarGeneration = async (url, car_model) => {
    try {
      const response = await axios.get(url, { params: { car_model } });
      if (Array.isArray(response.data)) {
        const generations = response.data;
        setCarGeneration(generations);
      } else {
        console.error('Данные о моделях не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных о моделях:', error);
    }
  };

    const [selectedTitle, setSelectedTitle] = useState('')
    // Функция для обновления списка моделей при изменении марки
    const handleTitleChange = async (e) => {
      const title = e.target.value;
      setSelectedTitle(title);
      setSelectedModel('');
      setSelectedGeneration('');
      // Загрузка моделей для выбранной марки
      const url = `${CarModel_URL}?car_title=${title}`;
      fetchCarModel(url, title)
    }

    const [selectedModel, setSelectedModel] = useState('')
    // Функция для обновления списка поколений при изменении одели
    const handleModelChange = async (e) => {
      const model = e.target.value;
      setSelectedModel(model);
      setSelectedGeneration('');
      // Загрузка моделей для выбранной марки
      const url = `${CarGeneration_URL}?car_model=${model}`;
      fetchCarGeneration(url, model)
    }

    const [selectedGeneration, setSelectedGeneration] = useState('')
    const handleGenerationChange = async (e) => {
      const generation = e.target.value;
      setSelectedGeneration(generation)
    }


    const [CarTransmission, setCarTransmission] = useState([]);
    const fetchTransmission = async (url) => {
    try {
      const response = await axios.get(url);
      if (Array.isArray(response.data)) {
        const transmission = response.data;
        setCarTransmission(transmission);
      } else {
        console.error('Данные не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных:', error);
    }
  };


    const [CarEngine, setCarEngine] = useState([]);
    const fetchEngine = async (url) => {
    try {
      const response = await axios.get(url);
      if (Array.isArray(response.data)) {
        const engine = response.data;
        setCarEngine(engine);
      } else {
        console.error('Данные не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных:', error);
    }
  };


    const [CarEngineType, setCarEngineType] = useState([]);
    const fetchEngineType = async (url) => {
    try {
      const response = await axios.get(url);
      if (Array.isArray(response.data)) {
        const engine_type = response.data;
        setCarEngineType(engine_type);
      } else {
        console.error('Данные не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных:', error);
    }
  };


    const [CarBody, setCarBody] = useState([]);
    const fetchBody = async (url) => {
    try {
      const response = await axios.get(url);
      if (Array.isArray(response.data)) {
        const body = response.data;
        setCarBody(body);
      } else {
        console.error('Данные не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных:', error);
    }
  };


    const [CarDrive, setCarDrive] = useState([]);
    const fetchDrive = async (url) => {
    try {
      const response = await axios.get(url);
      if (Array.isArray(response.data)) {
        const drive = response.data;
        setCarDrive(drive);
      } else {
        console.error('Данные не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных:', error);
    }
  };

    useEffect(() => {
        fetchCarTitle(CarTitle_URL)
        fetchCarModel(CarModel_URL)
        fetchCarGeneration(CarGeneration_URL)
        fetchTransmission(CarTransmission_URL)
        fetchEngine(CarEngine_URL)
        fetchEngineType(CarEngineType_URL)
        fetchBody(CarBody_URL)
        fetchDrive(CarDrive_URL)
    }, [])

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});
    }

    return (
        <div className={s.registrationWrapper}>
            <form className={s.registrationForm} onSubmit={handleSubmit}>
                <h1></h1>
                <h1>Новое объявление о продаже автомобиля</h1>

                <select className="form-select form-select-lg mb-3" aria-label=".form-select-lg example"
                        name='car_title'
                        onChange={(e) => {
                            handleTitleChange(e);
                            handleChange(e);
                        }}
                        value={modalWindow ? 'Марка авто' : FormData.car_title}>
                    <option value="" selected disabled>Марка авто</option>
                    {Array.isArray(CarTitle) &&
                        CarTitle.sort((a, b) => a.car_title.localeCompare(b.car_title)) &&
                        CarTitle.map(Title => (
                            <option key={Title.id}
                                    value={Title.car_title}>{Title.car_title}</option>
                        ))}
                </select>

                <select className="form-select form-select-lg mb-3" aria-label=".form-select-lg example"
                        name='car_model'
                        onChange={(e) => {
                            handleModelChange(e);
                            handleChange(e);
                        }}
                        value={modalWindow ? 'Модель авто' : FormData.car_model}
                        disabled={!selectedTitle} // Делаем неактивным, если марка не выбрана
                    >
                    <option value="" selected disabled>Модель авто</option>
                    {Array.isArray(CarModel) &&
                        CarModel.sort((a, b) => a.car_model.localeCompare(b.car_model)) &&
                        CarModel.map(Model => (
                            <option key={Model.id}
                                    value={Model.car_model}>{Model.car_model}</option>
                        ))}
                </select>

                <select className="form-select form-select-lg mb-3" aria-label=".form-select-lg example"
                        name='car_generation'
                        onChange={handleChange}
                        value={modalWindow ? 'Поколение авто' : FormData.car_model}
                        disabled={!selectedModel} // Делаем неактивным, если марка не выбрана
                >
                    <option value="" selected disabled>Поколение авто</option>
                    {Array.isArray(CarGeneration) &&
                        CarGeneration.sort((a, b) => a.car_generation.localeCompare(b.generation)) &&
                        CarGeneration.map(Generation => (
                            <option key={Generation.id}
                                    value={Generation.car_generation}>{Generation.car_generation}</option>
                        ))}
                </select>

                <div className={s.componentContainer}>
                    <input type="text" className={`form-control ${s.customInput}`} placeholder="Введите VIN авто"
                           name="car_vin" onChange={handleChange} value={modalWindow ? '' : FormData.car_vin}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="url" className={`form-control ${s.customInput}`}
                           placeholder="Вставьте главную фотографию" name="main_car_image"
                           onChange={handleChange} value={modalWindow ? '' : FormData.main_car_image}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="url" className={`form-control ${s.customInput}`} placeholder="Вставьте фотографии"
                           name="car_images" onChange={handleChange} value={modalWindow ? '' : FormData.car_images}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="number" className={`form-control ${s.customInput}`} placeholder="Напишите год выпуска"
                           name="year" onChange={handleChange} value={modalWindow ? '' : FormData.year}/>
                </div>

                <p></p>
                <select className="form-select form-select-lg mb-3" aria-label=".form-select-lg example"
                        name='transmission' onChange={handleChange}
                        value={modalWindow ? 'Коробка передач' : FormData.transmission}>
                    <option value="" selected disabled>Коробка передач</option>
                    {Array.isArray(CarTransmission) && CarTransmission.map(Transmission => (
                        <option key={Transmission.id}
                                value={Transmission.car_transmission}>{Transmission.car_transmission}</option>
                    ))}
                </select>

                <select className="form-select form-select-lg mb-3" aria-label=".form-select-lg example"
                        name="engine" onChange={handleChange}
                        value={modalWindow ? 'Объём в литрах' : FormData.engine}>
                    <option value="" selected disabled>Объём в литрах</option>
                    {Array.isArray(CarEngine) && CarEngine.map(Engine => (
                        <option key={Engine.id} value={Engine.car_engine}>{Engine.car_engine}</option>
                    ))}
                </select>

                <select className="form-select form-select-lg mb-3" aria-label=".form-select-lg example"
                        name="fuel" onChange={handleChange}
                        value={modalWindow ? 'Тип двигателя' : FormData.fuel}>
                    <option value="" selected disabled>Тип двигателя</option>
                    {Array.isArray(CarEngineType) && CarEngineType.map(EngineType => (
                        <option key={EngineType.id}
                                value={EngineType.car_engine_type}>{EngineType.car_engine_type}</option>
                    ))}
                </select>

                <select className="form-select form-select-lg mb-3" aria-label=".form-select-lg example"
                        name="car_body" onChange={handleChange}
                        value={modalWindow ? 'Кузов' : FormData.car_body}>
                    <option value="" selected disabled>Кузов</option>
                    {Array.isArray(CarBody) && CarBody.map(Body => (
                        <option key={Body.id} value={Body.car_body}>{Body.car_body}</option>
                    ))}
                </select>

                <select className="form-select form-select-lg mb-3" aria-label=".form-select-lg example"
                        name="car_drive" onChange={handleChange}
                        value={modalWindow ? 'Привод' : FormData.car_drive}>
                    <option value="" selected disabled>Привод</option>
                    {Array.isArray(CarDrive) && CarDrive.map(Drive => (
                        <option key={Drive.id} value={Drive.car_drive}>{Drive.car_drive}</option>
                    ))}
                </select>

                <div className={s.componentContainer}>
                    <input type="text" className={`form-control ${s.customInput}`} placeholder="Напишите цвет авто"
                           name="car_color" onChange={handleChange} value={modalWindow ? '' : FormData.car_color}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="text" className={`form-control ${s.customInput}`}
                           placeholder="Напишите количество л.с." name="horse_power"
                           onChange={handleChange} value={modalWindow ? '' : FormData.horse_power}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="text" className={`form-control ${s.customInput}`}
                           placeholder="Напишите расход на 100 км" name="consumption"
                           onChange={handleChange} value={modalWindow ? '' : FormData.consumption}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="number" className={`form-control ${s.customInput}`}
                           placeholder="Напишите пробег авто" name="mileage"
                           onChange={handleChange} value={modalWindow ? '' : FormData.mileage}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="number" className={`form-control ${s.customInput}`}
                           placeholder="Напишите цену в бел. рублях" name="price_byn"
                           onChange={handleChange} value={modalWindow ? '' : FormData.price_byn}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="number" className={`form-control ${s.customInput}`}
                           placeholder="Напишите цену в долларах" name="price_usd"
                           onChange={handleChange} value={modalWindow ? '' : FormData.price_usd}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="text" className={`form-control ${s.customInput}`}
                           placeholder="Введите город, где находится авто" name="city"
                           onChange={handleChange} value={modalWindow ? '' : FormData.city}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="text" className={`form-control ${s.customInput}`} placeholder="Описание авто"
                           name="description" onChange={handleChange} value={modalWindow ? '' : FormData.description}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="text" className={`form-control ${s.customInput}`} placeholder="Комплектация авто"
                           name="car_options" onChange={handleChange} value={modalWindow ? '' : FormData.car_options}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="url" className={`form-control ${s.customInput}`} placeholder="Ссылка на авто"
                           name="http_link" onChange={handleChange} value={modalWindow ? '' : FormData.http_link}/>
                </div>

                <center>
                    <button type="submit" className={s.button}>Опубликовать объявление</button>
                </center>
                <h1></h1>
            </form>

            <Modal open={modalWindow} onClose={() => setModalWindow(false)} closeIcon
                   style={{width: '400px', height: 'auto'}}>
                <Modal.Header>{errorMessage ? 'Ошибка' : 'Успех'}</Modal.Header>

                <Modal.Content>
                    <div>{errorMessage ? errorMessage.error : message}</div>
                </Modal.Content>

                <Modal.Actions>
                    <Button color='black' onClick={() => setModalWindow(false)}>Close</Button>
                </Modal.Actions>
            </Modal>

        </div>
    );
};

export default FormCarDataComponent;
