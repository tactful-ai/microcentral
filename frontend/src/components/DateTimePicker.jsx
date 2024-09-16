import React, { useState } from 'react';
import { Form, Button, Col, Row } from 'react-bootstrap';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { format } from 'date-fns';
import { data } from '../utils/data';

function DateTimeRangePicker() {
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [formattedStrDate, setFormattedStrDate] = useState('');
  const [formattedEndDate, setFormattedEndDate] = useState('');

  const formatDate = (date) => {
    return date ? format(date, 'MM/dd/yyyy, h:mm a') : '';
  };
  
  const handleStartDate = (date) => {
    setStartDate(date);
    setFormattedStrDate(formatDate(date));
  };
  const handleEndDate = (date) => {
    setEndDate(date);
    setFormattedEndDate(formatDate(date));
  };
  
  const handleTest = () => {
    console.log(formattedStrDate, formattedEndDate)
  }

  return (
    <Form className='my-3'>
      <Form.Group as={Row} controlId="formDateRange" className='mb-2'>
        <Form.Label column sm={2}>
          From
        </Form.Label>
        <Col sm={10}>
          <DatePicker
            selected={startDate}
            onChange={handleStartDate}
            showTimeSelect
            dateFormat="Pp"
            placeholderText="Select start date and time"
            className="form-control"
          />
        </Col>
      </Form.Group>

      <Form.Group as={Row} controlId="formDateRange" className='mb-5'>
        <Form.Label column sm={2}>
          To
        </Form.Label>
        <Col sm={10}>
          <DatePicker
            selected={endDate}
            onChange={handleEndDate}
            showTimeSelect
            dateFormat="Pp"
            placeholderText="Select end date and time"
            className="form-control"
          />
        </Col>
      </Form.Group>
        {/* <Button onClick={()=>handleTest()}>test</Button> */}
    </Form>
  );
}

export default DateTimeRangePicker;
