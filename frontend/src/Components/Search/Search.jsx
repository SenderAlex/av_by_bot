import React, {useState, useEffect, useContext} from "react";
import {Button, select} from "semantic-ui-react";
import "semantic-ui-css/semantic.min.css";
import s from './Search.module.css'
import Car from '../Car/Car'
import axios from "axios";
import { useGlobal } from "../../context/globalContext";
import { useNavigate } from "react-router-dom";
import {CarTitleContext} from "../../context/globalCarTitle";


const CarTitle_URL = 'http://127.0.0.1:8000/api/car_titles/'
const CarModel_URL = 'http://127.0.0.1:8000/api/car_models/car_models_by_title/'
const CarGeneration_URL = 'http://127.0.0.1:8000/api/car_generations/car_generations_by_model/'
const CarBody_URL = 'http://127.0.0.1:8000/api/car_bodies/'
const CarTransmission_URL= 'http://127.0.0.1:8000/api/car_transmissions/'
const CarEngineType_URL = 'http://127.0.0.1:8000/api/car_engine_types/'
const CarDrive_URL = 'http://127.0.0.1:8000/api/car_drives/'
const CarEngine_URL = 'http://127.0.0.1:8000/api/car_engines/'
const CarYear_URL = 'http://127.0.0.1:8000/api/car_years/'
const FilteredCar_URL = 'http://127.0.0.1:8000/api/filtered_cars/'

const SearchCar = () => {
    //const {carTitle} = useContext(CarTitleContext) || {};
    //const {carTitle} = props.autobrand || {};

    const {getFilteredCars} = useGlobal();
    const navigate = useNavigate();
    const handleClick = () => {
        navigate('/cars')
    }

    const [CarTitles, setCarTitles] = useState([]);
    const [CarModels, setCarModels] = useState([]);
    const [CarGenerations, setCarGenerations] = useState([]);
    const [CarBody, setCarBody] = useState([]);
    const [CarTransmission, setCarTransmission] = useState([]);
    const [CarEngineType, setCarEngineType] = useState([]);
    const [CarDrive, setCarDrive] = useState([]);
    const [CarEngine, setCarEngine] = useState([]);
    const [CarYear, setCarYear] = useState([]);

    const [selectedTitle, setSelectedTitle] = useState('');
    const [selectedModel, setSelectedModel] = useState('');
    const [selectedGeneration, setSelectedGeneration] = useState('');
    const [selectedYearFrom, setSelectedYearFrom] = useState('');
    const [selectedYearTo, setSelectedYearTo] = useState('');
    const [selectedPriceFrom, setSelectedPriceFrom] = useState('');
    const [selectedPriceTo, setSelectedPriceTo] = useState('');
    const [selectedCarEngineFrom, setSelectedCarEngineFrom] = useState('');
    const [selectedCarEngineTo, setSelectedCarEngineTo] = useState('');
    const [selectedCarTransmission, setSelectedCarTransmission] = useState('');
    const [selectedCarBody, setSelectedCarBody] = useState('');
    const [selectedCarEngineType, setSelectedCarEngineType] = useState('');
    const [selectedCarDrive, setSelectedCarDrive] = useState('');
    const [totalFilteredRecords, setTotalFilteredRecords] = useState(0);
    const [selectedCurrency, setSelectedCurrency] = useState('')


    useEffect(()=>{
      const filteredCarURL = getFilteredCarURL();

        fetchNumberofRecords(filteredCarURL);
    },[selectedTitle, selectedModel, selectedGeneration, selectedYearFrom, selectedYearTo, selectedPriceFrom,
        selectedPriceTo, selectedCarEngineFrom, selectedCarEngineTo, selectedCarTransmission, selectedCarBody,
        selectedCarEngineType, selectedCarDrive])


  const fetchTitle = async (url) => {
    try {
      const response = await axios.get(url);
      if (Array.isArray(response.data)) {
        const titles = response.data;
        setCarTitles(titles);
      } else {
        console.error('Данные о марках авто не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных о марках авто:', error);
    }
  };


  const fetchModel = async (url, car_title) => {
    try {
      const response = await axios.get(url, { params: { car_title } });
      if (Array.isArray(response.data)) {
        const models = response.data;
        setCarModels(models);
      } else {
        console.error('Данные о моделях не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных о моделях:', error);
    }
  };


  const fetchGeneration = async (url, car_model) => {
    try {
      const response = await axios.get(url, {params: {car_model}});
      if (Array.isArray(response.data)) {
        const generations = response.data;
        setCarGenerations(generations);
      } else {
        console.error('Данные о поколениях не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных о поколениях:', error);
    }
  };


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


  const fetchYear = async (url) => {
    try {
      const response = await axios.get(url);
      if (Array.isArray(response.data)) {
        const car_year = response.data;
        setCarYear(car_year);
      } else {
        console.error('Данные не являются массивом.');
      }
    } catch (error) {
      console.error('Произошла ошибка при получении данных:', error);
    }
  };

    const getFilteredCarURL = () => {
        const filterParams = {
            car_title: selectedTitle,
            car_model: selectedModel,
            car_generation: selectedGeneration,
            year_from: selectedYearFrom,
            year_to: selectedYearTo,
            engine_from: selectedCarEngineFrom,
            engine_to: selectedCarEngineTo,
            car_transmission: selectedCarTransmission,
            car_body: selectedCarBody,
            car_engine_type: selectedCarEngineType,
            car_drive: selectedCarDrive,
        };
        const queryString = new URLSearchParams(filterParams).toString();
        return `${FilteredCar_URL}?${queryString}`;
    }

    // Функция для обновления списка моделей при изменении марки
    const handleTitleChange = async (e) => {
      const title = e.target.value;
      setSelectedTitle(title);
      setSelectedModel('');
      setSelectedGeneration('');
      // Загрузка моделей для выбранной марки
      const url = `${CarModel_URL}?car_title=${title}`;
      fetchModel(url, title)
    }

    // Функция для обновления списка поколений при изменении модели
    const handleModelChange = async (e) => {
      const model = e.target.value;
      setSelectedModel(model);
      const filteredCarURL = getFilteredCarURL();
      // Загрузка моделей для выбранной марки
      const url = `${CarGeneration_URL}?car_model=${model}`;
      fetchGeneration(url)
    }

    ///
    const handleGenerationChange = async (e) => {
      const generation = e.target.value;
      setSelectedGeneration(generation)
    }

    const handleYearFromChange = async (e) => {
      const year_from = e.target.options[e.target.selectedIndex].text;
      setSelectedYearFrom(year_from)
    }

    const handleYearToChange = async (e) => {
      const year_to = e.target.options[e.target.selectedIndex].text;
      setSelectedYearTo(year_to)
    }

    const handlePriceFromChange = async (e) => {
      const price_from = e.target.value;
      setSelectedPriceFrom(price_from)
    }

    const handlePriceToChange = async (e) => {
      const price_to = e.target.value;
      setSelectedPriceTo(price_to)
    }

    const handleEngineFromChange = async (e) => {
      const engine_from = e.target.options[e.target.selectedIndex].text;
      setSelectedCarEngineFrom(engine_from)
    }

    const handleEngineToChange = async (e) => {
      const price_to = e.target.options[e.target.selectedIndex].text;
      setSelectedCarEngineTo(price_to)
    }

    const handleCarTransmissionChange = async (e) => {
      const transmission = e.target.options[e.target.selectedIndex].text;
      setSelectedCarTransmission(transmission)
    }

    const handleCarBodyChange = async (e) => {
      const body = e.target.options[e.target.selectedIndex].text;
      setSelectedCarBody(body)
    }

    const handleCarEngineTypeChange = async (e) => {
      const engine_type = e.target.options[e.target.selectedIndex].text;
      setSelectedCarEngineType(engine_type)
    }

    const handleCarDriveChange = async (e) => {
      const drive = e.target.options[e.target.selectedIndex].text;
      setSelectedCarDrive(drive)
    }

    const handleFormSubmit = (event) => {
    event.preventDefault();

    if (
        !selectedTitle &&
        !selectedModel &&
        !selectedGeneration &&
        !selectedYearFrom &&
        !selectedYearTo &&
        !selectedPriceFrom &&
        !selectedPriceTo &&
        !selectedCarEngineFrom &&
        !selectedCarEngineTo &&
        !selectedCarTransmission &&
        !selectedCarBody &&
        !selectedCarEngineType &&
        !selectedCarDrive &&
        !selectedCurrency
    ) {
        // Если ни одно поле не заполнено, показать все автомобили
        // Можно написать функцию для загрузки всех автомобилей и отобразить их
        console.log('Показываем все автомобили');
    } else {
        const queryParams = {
            car_title: selectedTitle,
            car_model: selectedModel,
            car_generation: selectedGeneration,
            year_from: selectedYearFrom,
            year_to: selectedYearTo,
            price_from: selectedPriceFrom,
            price_to: selectedPriceTo,
            engine_from: selectedCarEngineFrom,
            engine_to: selectedCarEngineTo,
            car_transmission: selectedCarTransmission,
            car_body: selectedCarBody,
            car_engine_type: selectedCarEngineType,
            car_drive: selectedCarDrive,
            currency: selectedCurrency
        };
        const queryString = new URLSearchParams(queryParams).toString();
        const url = `${FilteredCar_URL}?${queryString}`;

        getFilteredCars(url)

    }
}

    async function fetchNumberofRecords (url) {
      try {
        const response = await axios.get(url);
         const number_of_records = response.data.count;
         setTotalFilteredRecords(number_of_records)
      } catch (error) {
        console.error('Произошла ошибка при получении данных:', error);
      }
    };

    //хук -- вызываться каждый раз когда обновляется компонента
  useEffect(() => {
      fetchTitle(CarTitle_URL)
      fetchBody(CarBody_URL)
      fetchTransmission(CarTransmission_URL)
      fetchEngineType(CarEngineType_URL)
      fetchDrive(CarDrive_URL)
      fetchEngine(CarEngine_URL)
      fetchYear(CarYear_URL)
      fetchNumberofRecords(FilteredCar_URL)
  }, [])

  ///
  const handleClearSelection = () => {
      setSelectedTitle('');
      setSelectedModel('');
      setSelectedGeneration('');
      setSelectedYearFrom('');
      setSelectedYearTo('');
      setSelectedPriceFrom('');
      setSelectedPriceTo('');
      setSelectedCarEngineFrom('');
      setSelectedCarEngineTo('');
      setSelectedCarTransmission('');
      setSelectedCarBody('');
      setSelectedCarEngineType('');
      setSelectedCarDrive('');
      setSelectedCurrency('');
  }


  return (
      <div>
          <form onSubmit={handleFormSubmit}>
              <nav>
                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="car_title"
                      onChange={handleTitleChange}
                      value={selectedTitle}>
                      <option value="" disabled>Марка автомобиля</option>
                      {Array.isArray(CarTitles) &&
                          CarTitles.sort((a,b) => a.car_title.localeCompare(b.car_title)) &&
                          CarTitles.map(CarTitle => (
                          <option key={CarTitle.id} value={CarTitle.car_title}>{CarTitle.car_title}</option>
                      ))}
                  </select>

                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="car_model"
                      onChange={handleModelChange}
                      value={selectedModel}
                      disabled={!selectedTitle} // Делаем неактивным, если марка не выбрана
                  >
                      <option value="" disabled>Модель автомобиля</option>
                      {Array.isArray(CarModels) &&
                          CarModels.sort((a,b) => a.car_model.localeCompare(b.car_model)) &&
                          CarModels.map(CarModel => (
                          <option key={CarModel.id} value={CarModel.car_model}>{CarModel.car_model}</option>
                      ))}
                  </select>


                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="car_generation"
                      onChange={handleGenerationChange}

                      value={selectedGeneration}
                      disabled={!selectedModel} // Делаем неактивным, если модель не выбрана
                  >
                      <option value="" disabled>Поколение автомобиля</option>
                      {CarGenerations.map(CarGeneration => (
                          <option key={CarGeneration.id}
                                  value={CarGeneration.car_generation}>
                              {CarGeneration.car_generation}
                          </option>
                      ))}
                  </select>
              </nav>

              <nav>
                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="year_from"
                      onChange={handleYearFromChange}
                      value={selectedYearFrom}

                  >
                      <option selected>Год выпуска от</option>
                      {Array.isArray(CarYear) && CarYear.map(Year => (
                          <option key={Year.id} value={Year.car_year}>{Year.car_year}</option>
                      ))}
                  </select>

                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="year_to"
                      onChange={handleYearToChange}
                      value={selectedYearTo}
                  >
                      <option selected>Год выпуска до</option>
                      {Array.isArray(CarYear) && CarYear.map(Year => (
                          <option key={Year.id} value={Year.car_year}>{Year.car_year}</option>
                      ))}
                  </select>

                  <div className="input-group mb-3">

                   <span className="input-group-text" id="inputGroup-sizing-default">
                    <b style={{fontFamily: 'Arial', fontSize: '14px', fontWeight: 'bold'}}>Цена от</b>
                   </span>

                      <input
                          type="text"
                          className="form-control"
                          aria-label="Sizing example input"
                          aria-describedby="inputGroup-sizing-default"
                          name="price_from"
                          onChange={handlePriceFromChange}
                          value={selectedPriceFrom}
                      />
                  </div>

                  <div className="input-group mb-3">

                  <span className="input-group-text" id="inputGroup-sizing-default">
                    <b style={{fontFamily: 'Arial', fontSize: '14px', fontWeight: 'bold'}}>Цена до</b>
                   </span>

                      <input
                          type="text"
                          className="form-control"
                          aria-label="Sizing example input"
                          aria-describedby="inputGroup-sizing-default"
                          name="price_to"
                          onChange={handlePriceToChange}
                          value={selectedPriceTo}
                      />
                  </div>

                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="currency"
                      onChange={(e) => setSelectedCurrency(e.target.value)}
                      value = {selectedCurrency}
                  >
                      <option selected>Валюта</option>
                      <option value="USD">USD</option>
                      <option value="BYN">BYN</option>
                  </select>

                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="engine_from"
                      onChange={handleEngineFromChange}
                      value={selectedCarEngineFrom}
                  >
                      <option selected>Объём от</option>
                      {Array.isArray(CarEngine) && CarEngine.map(Engine => (
                          <option key={Engine.id} value={Engine.car_engine}>{Engine.car_engine}</option>
                      ))}
                  </select>

                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="engine_to"
                      onChange={handleEngineToChange}
                      value={selectedCarEngineTo}
                  >
                      <option selected>Объём до</option>
                      {Array.isArray(CarEngine) && CarEngine.map(Engine => (
                          <option key={Engine.id} value={Engine.car_engine}>{Engine.car_engine}</option>
                      ))}
                  </select>
              </nav>

              <nav>
                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="car_transmission"
                      onChange={handleCarTransmissionChange}
                      value={selectedCarTransmission}
                  >
                      <option selected>Коробка передач</option>
                      {Array.isArray(CarTransmission) && CarTransmission.map(Transmission => (
                          <option key={Transmission.id} value={Transmission.car_transmission}>
                              {Transmission.car_transmission}
                          </option>
                      ))}
                  </select>

                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="car_body"
                      onChange={handleCarBodyChange}
                      value={selectedCarBody}
                  >
                      <option value="">Кузов</option>
                      {Array.isArray(CarBody) && CarBody.map(Body => (
                          <option key={Body.id} value={Body.car_body}>{Body.car_body}</option>
                      ))}
                  </select>

                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="car_engine_type"
                      onChange={handleCarEngineTypeChange}
                      value={selectedCarEngineType}
                  >
                      <option selected>Тип двигателя</option>
                      {Array.isArray(CarEngineType) && CarEngineType.map(EngineType => (
                          <option key={EngineType.id} value={EngineType.car_engine_type}>
                              {EngineType.car_engine_type}
                          </option>
                      ))}
                  </select>

                  <select
                      className="form-select form-select-lg mb-3"
                      aria-label=".form-select-lg example"
                      name="car_drive"
                      onChange={handleCarDriveChange}
                      value={selectedCarDrive}
                  >
                      <option selected>Привод</option>
                      {Array.isArray(CarDrive) && CarDrive.map(Drive => (
                          <option key={Drive.id} value={Drive.car_drive}>{Drive.car_drive}</option>
                      ))}
                  </select>
              </nav>
              <nav>
                  <div>
                      <Button
                          onClick={handleClearSelection}
                          style={{
                              backgroundColor: '#33BD7EEF',
                              color: '#fff',
                          }}
                          type="submit">
                          Очистить
                      </Button>
                  </div>
                  <div>
                      <Button
                          className={s.button}
                          onClick={handleClick}
                          onChange={fetchNumberofRecords}
                          type="submit">
                          Показать {totalFilteredRecords} объявления
                      </Button>
                  </div>
                  <h1></h1>
                  <h1></h1>
              </nav>
          </form>
      </div>
  );
};

export default SearchCar;
