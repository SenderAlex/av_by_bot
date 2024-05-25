import Car from "./Components/Car/Car";
import MessageData from "./Components/MessageData/MessageData";
import NavigationMenu from "./Components/Navigation/Navigation";
import SearchCar from "./Components/Search/Search";
import New_Car from "./Components/New Auto/New_Car";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";
import Car_Description from "./Components/Car_Description/Car_Description";
import { GlobalProvider } from "./context/globalContext";
import Electric_Car from "./Components/ElectricCar/Electric_Car";
import MileAgeCar from "./Components/MileAgeCar/MileAgeCar";
import Car_List from "./Components/Car_Title/Car_Title";
import FormDataComponent from "./Components/Registration/Registration";
import Entrance_User from "./Components/User_Entrance/Entrance_User";
import Submit_Ad from "./Components/Submit_Ad/Submit_Ad";
import Car_Title from "./Components/Car_Title/Car_Title";
import Car_Model from "./Components/Car_Model/Car_Model";
import {CarTitleProvider} from "./context/globalCarTitle";
import {CarModelProvider} from "./context/globalCarModel";
import Car_Generation from "./Components/Car_Generation/Car_Generation";

const App = (props) => {
  return (
    <GlobalProvider>
      <BrowserRouter>
        <div className='app-wrapper'>
          <NavigationMenu/>
          <CarTitleProvider>
            <CarModelProvider>
          <Routes>
            <Route path="/" element={<Car_Title/>}/>
            <Route path="/:CarTitles" element={<Car_Model />}/>
            <Route path="/:CarTitles/:CarModels" element={<Car_Generation />}/>
          </Routes>
            </CarModelProvider>
          </CarTitleProvider>
          <SearchCar/>
          {/*<MessageData/>*/}
          <div className='app-wrapper-content'>
            <Routes>
              {/*<Route path="/new_car/:id" element={()=> <div>test</div>}/>  /!*<NavLink to='/New_Car'>New_Car</NavLink>!!!!!!*!/*/}
              <Route path="/registration" element={<FormDataComponent/>}/>
              <Route path="/entrance" element={<Entrance_User/>}/>
              <Route path="/cabinet" element={<Submit_Ad/>}/>
              <Route path="/cars" element={<Car/>}/> {/*<NavLink to='/New_Car'>New_Car</NavLink>!!!!!!*/}
              <Route path="/cars/:id" element={<Car_Description/>}/>
              <Route path="/new-cars" element={<New_Car/>}/> {/*<NavLink to='/New_Car'>New_Car</NavLink>!!!!!!*/}
              <Route path="/electric-cars" element={<Electric_Car/>}/>
              <Route path="/mileage-cars" element={<MileAgeCar/>}/>
            </Routes>
          </div>
        </div>
      </BrowserRouter>
    </GlobalProvider>
  )
}
export default App;




