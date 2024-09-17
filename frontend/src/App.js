import React from 'react';
import {BrowserRouter, Routes, Route, Navigate, RouterProvider} from 'react-router-dom';
import MainRouter from './routes/MainRouter';

function App() {
  return (
    <React.StrictMode>
      <RouterProvider router={MainRouter}/>
    </React.StrictMode>
  );
}

export default App;
