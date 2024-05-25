
import React, { useState } from 'react';
import axios from 'axios';
import s from "../User_Entrance/Entrance_User.module.css";
import {Button, Modal} from "semantic-ui-react";
import {NavLink, useNavigate} from "react-router-dom";
import ReCAPTCHA from "react-google-recaptcha";  // библиотека google recaptcha


const APIRegister_URL = 'http://127.0.0.1:8000/api/login/'

const Entrance_User = () => {
    const [formData, setFormData] = useState({email: '', password: ''})
    const [message, setMessage] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const [modalWindow, setModalWindow] = useState(false)
    const navigate = useNavigate()

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post(APIRegister_URL, formData)
            .then(response => {
                console.log(response.data);
                // console.log('Data sent successfully');
                setMessage(response.data.message)
                setModalWindow(true)
                setFormData({email: '', password: ''})
                setErrorMessage('')
                navigate('/cabinet')
            })
            .catch(error => {
                console.error('Failed to send data:', error);
                setErrorMessage(error.response.data)
                setModalWindow(true)
            });
    };

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});
    }

    const handleClickRegistration = () => {
        navigate('/registration')
    }


    return (
        <div className={s.registrationWrapper}>
            <form className={s.registrationForm} onSubmit={handleSubmit}>
                <div className={s.componentContainer}>
                    <input type="email" className="form-control" placeholder="Enter your e-mail"
                           name="email" onChange={handleChange} value={FormData.email}/>
                </div>

                <div className={s.componentContainer}>
                    <input type="password" className="form-control" placeholder="Enter your password"
                           name="password" onChange={handleChange} value={FormData.password}/>
                </div>
                <h5></h5>

                <center>

                    <button type="submit" className={s.button} >Войти</button>
                </center>
                <h1>{message}</h1>
                <h6>
                    <NavLink to={`/registration`} onClick={handleClickRegistration}>
                        <b>Регистрация</b>
                    </NavLink>
                </h6>
                <h7>для тех, кто первый раз на сайте</h7>


            </form>

            <Modal open={modalWindow} onClose={() => setModalWindow(false)} closeIcon
                   style={{ width: '400px', height: 'auto' }}>
                <Modal.Header>{errorMessage ? 'Ошибка' : 'Успех'}</Modal.Header>
                {/*<Modal.Header>Ошибка</Modal.Header>*/}

                <Modal.Content>
                     {errorMessage && <div>{errorMessage.error}</div>}
                </Modal.Content>

                <Modal.Actions>
                    <Button color='black' onClick={() => setModalWindow(false)}>Close</Button>
                </Modal.Actions>
            </Modal>

        </div>
    );
};

export default Entrance_User;
