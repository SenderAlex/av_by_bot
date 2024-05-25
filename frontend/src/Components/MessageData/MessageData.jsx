import React, { useState, useEffect } from 'react';
import axios from 'axios';
import s from './MessageData.module.css';


const API_URL = 'http://127.0.0.1:8000/api/MessageData/'

function MessageData() {
  const [messageData, setMessageData] = useState([]);  //????????

  useEffect(() => {
    fetchData(API_URL);
  }, []);

  const fetchData = (url) => {
    axios.get(url)
      .then(response => {
        setMessageData(prevData => [...prevData, ...response.data.results]);
        if (response.data.next) {
          fetchData(response.data.next);
        }
      })
      .catch(error => {
        console.log(error);
      });
  };

  const Table = ({ dateTime }) => {
  const formatDateTime = (dateTime) => {
    const formattedDateTime = dateTime.replace("T", " ").replace("Z", "");
    return formattedDateTime;
  };

  return <td>{formatDateTime(dateTime)}</td>;
};


  return (
      <div>
          <h1><center><b>ПОЛУЧЕННЫЕ СООБЩЕНИЯ</b></center></h1>
          <center>
          <div className={s.width2}>
          <table className="table table-striped custom-width2">
              <thead>
              <tr>
                  <th scope="col_ID">ID</th>
                  <th scope="col_telegram_ID">telegram_ID</th>
                  <th scope="col_first_name">first name</th>
                  <th scope="col_last_name">last name</th>
                  <th scope="col_phone_number">phone number</th>
                  <th scope="col_message">message</th>
                  <th scope="col_date_time">date_time</th>
              </tr>
              </thead>
              <tbody>

              {messageData.map(data => (
              <tr key={data.id}>
                  <td>{data.id}</td>
                  <td>{data.telegram_id}</td>
                  <td>{data.first_name}</td>
                  <td>{data.last_name}</td>
                  <td>{data.phone_number}</td>
                  <td>{data.message}</td>
                  <td>
                    <Table dateTime={data.full_date_time}/>
                  </td>
              </tr>
              ))}
              </tbody>
          </table>
          </div>
          </center>
      </div>
  );
}

export default MessageData;