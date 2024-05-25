import React, {createContext, useState} from "react";

export const CarTitleContext = createContext();

export const CarTitleProvider = ({children}) => {
    const [carTitle, setCarTitle] = useState('');

    const handleCarTitleClick = (title) => {
        setCarTitle(title);
    };

    return (
        <CarTitleContext.Provider value = {{carTitle, handleCarTitleClick}}>
            {children}
        </CarTitleContext.Provider>
    );
};