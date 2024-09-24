import React, { useState } from 'react';
import { Form, Button, Col, Row } from 'react-bootstrap';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { format } from 'date-fns';

function DateTimeRangePicker({ onStartDateChange, onEndDateChange }) {
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [formattedStrDate, setFormattedStrDate] = useState('');
  const [formattedEndDate, setFormattedEndDate] = useState('');

  const isoFormat = date => {
    const inputDate = new Date(date);

    inputDate.setUTCDate(inputDate.getUTCDate());
    console.log(inputDate.toISOString());
    return inputDate.toISOString();
};

  const handleStartDate = (date) => {
    setStartDate(date);
    onStartDateChange(isoFormat(date));
    console.log(startDate)
  };
  const handleEndDate = (date) => {
    setEndDate(date);
    onEndDateChange(isoFormat(date));
    console.log(endDate)
  };

  return (
    <Form className='mt-3 mb-5'>
      <Form.Group as={Row} controlId="formDateRange" className='mb-2'>
        <Col sm={6}>
        <Form.Label sm={2}>
          From Date
        </Form.Label>
          <DatePicker
            selected={startDate}
            onChange={handleStartDate}
            showTimeSelect
            dateFormat="Pp"
            placeholderText="Select start date and time"
            className="form-control"
          />
        </Col>
        <Col sm={6}>
        <Form.Label sm={2}>
          To Date
        </Form.Label>
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
    </Form>
  );
}

export default DateTimeRangePicker;
