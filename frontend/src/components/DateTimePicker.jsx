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

  const handleStartDate = (date) => {
    const dateIsoFormat = new Date(date).toISOString();
    setStartDate(date);
    setFormattedStrDate(dateIsoFormat);
  };
  const handleEndDate = (date) => {
    const dateIsoFormat = new Date(date).toISOString();
    setEndDate(date);
    setFormattedEndDate(dateIsoFormat);
  };

  return (
    <Form className='my-5'>
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
