import React, {createContext, useState} from "react";

export const CarModelContext = createContext();

export const CarModelProvider = ({children}) => {
    const [carModel, setCarModel] = useState('');

    const handleCarModelClick = (model) => {
        setCarModel(model);
    };

    return (
        <CarModelContext.Provider value = {{carModel, handleCarModelClick}}>
            {children}
        </CarModelContext.Provider>
    );
};