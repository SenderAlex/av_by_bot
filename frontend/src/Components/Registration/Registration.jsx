
import React, { useState } from 'react';
import axios from 'axios';
import s from "../Registration/Registration.module.css";
import {Button, Modal} from "semantic-ui-react";


const APIRegister_URL = 'http://127.0.0.1:8000/api/car_registration/'


const FormDataComponent = () => {
    const [formData, setFormData] = useState({username: '', email: '', password: ''})
    const [message, setMessage] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const [modalWindow, setModalWindow] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post(APIRegister_URL, formData)
            .then(response => {
                console.log(response.data);
                console.log('Data sent successfully');
                setMessage(response.data.message)
                setModalWindow(true)
                setFormData({username: '', email: '', password: ''})
                setErrorMessage('')
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


    return (
        <div className={s.registrationWrapper}>
        <form className={s.registrationForm} onSubmit={handleSubmit}>
            <div className={s.componentContainer}>
                <input type="text" className="form-control" placeholder="Enter your name"
                name="username" onChange={handleChange} value={modalWindow ? '' : FormData.username}/>
            </div>

            <div className={s.componentContainer}>
                <input type="email" className="form-control" placeholder="Enter your e-mail"
                name="email" onChange={handleChange} value={modalWindow ? '' : FormData.email}/>
            </div>

            <div className={s.componentContainer}>
                <input type="password" className="form-control" placeholder="Enter your password"
                name="password" onChange={handleChange} value={modalWindow ? '' : FormData.password}/>
            </div>
             <center>
            <button type="submit" className={s.button}>Зарегистрироваться</button>
             </center>
        </form>

            <Modal open={modalWindow} onClose={() => setModalWindow(false)}
                   closeIcon style={{ width: '400px', height: 'auto' }}>
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

export default FormDataComponent;
